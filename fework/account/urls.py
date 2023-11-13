from django.urls import path
from .views import RegisterView,LoginUser,LoginAdmin,VerifyOtpView,UserLogoutView,UserView,RemoveUser,EditUser,AddUser,LogoutView,ProfileView
from .views import UserProfileView,UserWorkView,UserWorksView,MyInbox,GetMessages,SendMessage,AdminWorksView,VerifyWorkView,RejectWorkView
urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginUser.as_view()),
    path('admin_login/',LoginAdmin.as_view()),
    path('verify_otp/',VerifyOtpView.as_view()),
   
    
    path('userlogout/',UserLogoutView.as_view()),


    path('dashboard/',UserView.as_view()),
    path('remove/<int:pk>',RemoveUser.as_view()),
    path('edit/<int:pk>',EditUser.as_view()),
    path('adduser/',AddUser.as_view()),
    path('logout/',LogoutView.as_view()),


    path('user_profile/',ProfileView.as_view()),
    path('user_profile_display/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('user_work_post/',UserWorkView.as_view()),

    path('user-work/<int:user_id>/', UserWorksView.as_view()),
    path('verify-admin/', AdminWorksView.as_view()),
    path('verify-work/<int:work_id>/', VerifyWorkView.as_view(), name='verify_work'),
    path('reject-work/<int:work_id>/', RejectWorkView.as_view(), name='reject_work'),

     
    path("my-messages/<user_id>/",MyInbox.as_view()),
    path("get-messages/<sender_id>/<receiver_id>",GetMessages.as_view()),
    path("send-message/",SendMessage.as_view()),
]

 # path('user_login/',LoginUser.as_view()),
#  path('user_logout/',UserLogoutView.as_view()),