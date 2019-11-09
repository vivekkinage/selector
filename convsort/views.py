from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from .models import job,cvs
import datetime
import smtplib
from .models import REGISTRATIONS
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import re



# Create your views here.
tempo = REGISTRATIONS.objects.all()
info={'user_id':9999999999999999999999999999999999999999999999999999999}
def home(request):
    return render(request,"index.html",{})


def register(request):
    context={}
    if request.method=='POST':
        data = request.POST

        r = REGISTRATIONS(name = data['name'], birthday = data['birthday'], gender = data['gender'], email = data['email'], password=data['password'], phone = data['phone'])
        r.save()
        context={'display':"Registered Successfully!"}
        return render(request,'login.html',{})
    return render(request,'register.html',context)

def reg(request):
    return render(request,"register.html",{})

def login(request):
    global info
    if request.method=='POST':
        print("in login")
        data=request.POST
        em_id = data['email']
        ps = data['password']
        print('\n\n\n\n\n\n\n\ndekh:',ps)
        var = REGISTRATIONS.objects.filter(email=em_id)
        print('\n\n\n\n\n\nvar:',var)
        id=len(var)
        if id!=0:
            for i in var:
                if i.password==ps:
                    print('\n\n\n\nsuccesfull!!!!!!!!!!!!!!!!')
                    info = {'user_id':i.user_key,'user_name':i.name}
                    print('\n\n\n\n\n\nuser Key:',info['user_id'])
                    return redirect('/',request)



    return render(request,'login.html',{})


def Home(request,job):
    return render(request,'index.html',{'job':job})



def download(request, path):
    file_path = path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def upload(request,job_id):
    global info
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print('\n\n\n\n\n\nuser id:',info['user_id'])
        jb=job.objects.filter(id=job_id)
        new_cvs=cvs(name=info['user_name'],date=datetime.datetime.now(),job=jb[0].name,jid=job_id,path=uploaded_file.name,uid=info['user_id'],skills=extract_text_from_pdf('media/'+uploaded_file.name))
        new_cvs.save()
    return redirect('/',request)

def jobs(request):
    global info
    if info['user_id']!=9999999999999999999999999999999999999999999999999999999:
        all=job.objects.all()
        print(all)
        return render(request, 'jobs.html', {'jobs':all})
    else:
        return redirect('/login/',request)


def admin_jobs(request):
    all=job.objects.all()
    print(all)
    return render(request, 'admin_job.html', {'jobs':all})

def add_job(request):
    if request.method=='POST':
        data=request.POST
        new_job=job(name=data['name'],description=data['description'],skills=data['skills'])
        new_job.save()
        all=job.objects.all()
        print(all)
        return render(request, 'admin_job.html', {'jobs':all})

def delete_job(request,id):
    find_job=job.objects.filter(id=int(id))
    find_job.delete()
    all=job.objects.all()
    print(all)
    return redirect('/admin_jobs',request)

def admins(request):
    cv=cvs.objects.filter(status=0)
    print(len(cv))
    for i in cv:
        print(i.name)
    return render(request,'dashboard.html',{'cv':cv})

def shortlist(request):
    cv=cvs.objects.all()
    jb=job.objects.all()
    skill_list=[]
    print('\n\n\n\n\n',skill_list)
    for i in cv:
        lst1=i.skills.lower().split(',')
        jb=job.objects.filter(id=i.jid)
        skill_list=[]
        
        lst=jb[0].skills.lower().split(' ')
        skill_list.extend(lst)
        for i in range(skill_list.count('')):
            skill_list.remove('')
        print(lst1)
        print('\n\nskill list:',skill_list)
        for j in skill_list:
            for k in lst1:
                if j in k:
                    print('found :',j)
                    select(request,i.uid)
    cv=cvs.objects.filter(status=1)
    return render(request,'shortlist.html',{'cv':cv})



def select(request,uid,jid):
    cv=cvs.objects.filter(uid=uid,jid=jid)
    jb=job.objects.filter(id=cv[0].jid)
    obj=REGISTRATIONS.objects.filter(user_key=uid)
    cv.update(status=1,job=jb[0].name)
    print('\n\n\n\n\n',cv[0].name)
    # creates SMTP session
    '''s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("miniproject2504@gmail.com", "@Miniproject123")

    # message to be sent
    message = 'Hello '+cv[0].name+',\nCongratulations you have been selected for the job '+cv[0].job+'.\nYou can join from next week.\nThank you'

    # sending the mail
    s.sendmail("miniproject2504@gmail.com", obj[0].email, message)

    # terminating the session
    s.quit()'''
    cv=cvs.objects.filter(status=0)
    return render(request,'dashboard.html',{'cv':cv})


def reject(request,uid,jid):
    cv=cvs.objects.filter(uid=uid,jid=jid)
    cv.delete()
    return redirect('/shortlist',request)


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        result=re.search(r'TECHNICAL SKILLS(.*?)ACHIEVEMENTS', text).group(1)
        return result
