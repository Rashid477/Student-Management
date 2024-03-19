from django.shortcuts import render,redirect
from app.models import User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def stud_register(request):
    if request.method == 'POST':
        na=request.POST['Name']
        dob=request.POST['DOB']
        em=request.POST['Email']
        phn=request.POST['Phone']
        usr=request.POST['username']
        pss=request.POST['password']
        
        ad=User.objects.create_user(email=em,username=usr,password=pss,usertype='Student')
        Student.objects.create(Name=na,DOB=dob,Phone=phn,Email=em,Stud=ad).save()
        return redirect(user_login)
    else:
        return render(request,'studregistration.html')

def Admin(request):
    return render(request,'admin.html')


def user_login(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        pwd=request.POST.get('password')
        user=authenticate(request,username=uname, password=pwd)
        print(user)
        if user is not None and user.is_superuser==1:
            login (request,user)
            return redirect(Admin)
        elif user is not None  and user.usertype=="Student":
            student=Student.objects.get(Stud=user.id)
            # request.session['sname']=user.id

            login(request,user)
            request.session['for_id']=student.Stud.id
            return redirect(StudHome)
            # else:
            #     return HttpResponse("sorry your account is blocked")
            
        elif user is not None and user.usertype=='Teacher':
            teacher=Teacher.objects.get(Teach=user.id)
            login(request,user)
            request.session['for_id']=teacher.Teach.id
            return redirect(TeachHome)
            # else:
            #     return HttpResponse("sorry your account is blocked")
        else:
            return HttpResponse('Sorry, invalid details')
    else:
        return render(request,'login.html')



def StudHome(request):
    id = request.session['for_id']
    std=Student.objects.get(Stud=id)
    print(std.id)
    return render(request,'student_home.html',{'profile':std})

def TeachHome(request):
    id= request.session['for_id']
    tch=Teacher.objects.get(Teach=id)
    return render(request,"teach_home.html",{"teach":tch})

def logouts(request):
    logout(request)
    return redirect(user_login)


#_____________admin___________
def AddTeacher(request):
    if  request.method == 'POST':
        nm=request.POST['Name']
        ag=request.POST['Age']
        dep=request.POST['Department']
        exp=request.POST['Experience']
        phn=request.POST['Phoneno']
        em=request.POST['Email']
        usrnm = request.POST['username']
        pwd=request.POST['password']
        cf=request.POST['confirmpassword']
        if pwd==cf:
            x = User.objects.create_user(email=em, username=usrnm, password=pwd,usertype='Teacher')
            Teacher.objects.create(Name=nm,Age=ag,Department=dep,Experience=exp,Phoneno=phn,Email=em,Teach=x).save()
            return redirect(ViewTeacher)
        else:
            HttpResponse("Fail")
    else:
        return render(request,'add_teacher.html')
    


def ViewTeacher(request):
    teachers=Teacher.objects.all()
    return render(request,"view_teacher.html"  , {'teacher' : teachers})

def DeleteTeach(request,id):
    dl=Teacher.objects.filter(id=id)
    dl.delete()
    return  redirect(ViewTeacher)

def EditForm(request,id):
    upd=Teacher.objects.get(id=id)
    return render(request,"Edit_teacher.html",{'teacher':upd})

def UpdateForm(request,id):
    if  request.method=="POST":
        nm=request.POST["Name"]
        ag=request.POST["Age"]
        dep=request.POST["Department"]
        exp=request.POST["Experience"]
        phn=request.POST["Phoneno"]
        em=request.POST["Email"]
        dat=Teacher.objects.get(id=id)
        # m=Teacher.objects.filter(id=id).update(Name=nm,Age=ag, Department=dep,Experience=exp,Phoneno=phn,Email=em)
        dat.Name=nm
        dat.Age=ag
        dat.Department=dep
        dat.Experience=exp
        dat.Phoneno=phn
        dat.Email=em
        dat.save()
        return redirect(ViewTeacher)
    


def ViewStudent(request):
    student = Student.objects.all()
    return render(request,'view_student.html',{"student":student})

def DeleteStud(request,id):
    dt=Student.objects.filter(id=id).delete()
    return redirect(ViewStudent)

def StudViewTeach(request):
    teacher=Teacher.objects.all()
    return  render(request,'stud_view_teacher.html', { 'tch': teacher })



def StudProfEdit(request):
    return render (request , "stud_profile_edit.html", )


def StudUpdateProfile(request,id):
    if  request.method =='POST':
        nam=request.session['for_id']
        print(nam)
        nm=request.POST["Name"]
        db=request.POST["DOB"]
        phn=request.POST["Phoneno"]
        em=request.POST["Email"]
        user =request.POST['username']
        pwd = request.POST['password']
        ed=Student.objects.get(Stud=nam)
        edt=User.objects.get(id=id)
        ed.Name=nm
        ed.DOB=db
        ed.Phone=phn
        ed.Email=em
        edt.first_name=nm
        edt.username = user
        edt.set_password(pwd)
        ed.save()
        edt.save()
        return redirect(StudHome)
    else:
        std=request.session['for_id']
        print('hi', std)
        prf=Student.objects.get(Stud=std)
        return render (request,'stud_profile_edit.html'  , {'profile':prf})
    


def TeachUptProf(request,id):
    if  request.method=="POST":
        nam=request.GET['for_id']
        print(nm)
        nm=request.POST["Name"]
        ag=request.POST["Age"]
        dep=request.POST["Department"]
        exp=request.POST["Experience"]
        phn=request.POST["Phoneno"]
        em=request.POST["Email"]
        user =request.POST['username']
        pwd = request.POST['password']
        dtd=Teacher.objects.get(Teach=nam)
        dt=User.objects.get(id=id)
        dtd.Name=nm
        dtd.Age=ag
        dtd.Department=dep
        dtd.Experience=exp
        dtd.Phoneno=phn
        dtd.Email=em
        dt.first_name=nm
        dt.username=user
        dt.set_password(pwd)
        dtd.save()
        dt.save()
        return redirect(TeachHome)
    else :
        tch=request.session['for_id']
        prof=Teacher.objects.get(Teach=tch)
        return render (request,"teach_prof_upd.html",{'teach':prof})
    