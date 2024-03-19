from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.user_login,name='user_login'),
    path('sregister',views.stud_register,name='stud_register'),
    path('lout' , views.logouts ,name="logouts"),
    path('sview',views.StudHome, name='StudHome'), # student home
    path('tview',views.TeachHome, name='TeachHome'),  # teacher home
    path('admin',views.Admin,name='admin'),  # admin page
    path('adtecher',views.AddTeacher, name='AddTeacher'),  # admin page
    path('vteach',views.ViewTeacher,name='ViewTeacher'),   # view teacher data
    path('delete/<int:id>',views.DeleteTeach,name='DeleteTeach') ,# delete the record of Teacher
    path('edit/<int:id>',views.EditForm,name='EditForm'),     # edit form for
    path('update/<int:id>',views.UpdateForm,name='UpdateForm'),# update form for teachers
    path('vstud',views.ViewStudent,name='ViewStudent'),        # view student data
    path('delete/<int:id>',views.DeleteStud,name='DeleteStud'),# delete the record of Student
    path('s_view_teach',views.StudViewTeach,name='StudViewTeach'), # view all teaches assigned to a particular student
    path('stud_edit/<int:id>',views.StudProfEdit,name='StudProfEdit'), # Edit Profile Page of the student
    path('updates/<int:id>',views.StudUpdateProfile,name='StudUpdateProfile'), # Update profile student
    path('updteach/<int:id>',views.TeachUptProf,name='TeachUptProf'), # Updating Teacher Profile
]
