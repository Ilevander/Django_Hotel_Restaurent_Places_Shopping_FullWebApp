from django.urls import path
from .views import profile , profile_edit , signup , myReservation , myListing
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('reservation/',myReservation,name='reservation'),
    path('mylisting/',myListing,name='mylisting'),
    path('profile/edit', profile_edit , name='profile_edit'),
    #Using class based views : thats why we add as.view()
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),

    #Customizing urls design to customize the functionnality of the PasswordResetView class
    #Each of this urls should be attached between them by using the URL name attibut , because there is a cycle and relation between theme
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),#To allow to user to write the appropriate email
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),#means that the mail has been sent with the token
    #Keyword arguments from the URL:
    #-uidb64: The user’s id encoded in base 64.
    #-token: Token to check that the password is valid.
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),#To confirme the link from the user from the mail sent
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html.'),name='password_reset_complete'),

]

'''
Its not autorized to use google accounts for django as a sender to reset lpassword , 
because we have to enable the lesssecureapps option to alow the use of other apps
to use our gmail account , thing that let your django account more venurable , so google dont removed this option, to reset the password we have too loock for another 
option
'''