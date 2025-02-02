from django.urls import path
from jobwebsite.ViewsFolder.home import home, about_us, contact_us, job_detail, job_listing, notification, profile, profile, terms_and_conditions
from jobwebsite.ViewsFolder.employer import job_posting, employer_dashboard
from jobwebsite.ViewsFolder.employee import job_application, employee_dashboard
from jobwebsite.ViewsFolder.auth import login, logout, register, password_reset
from django.contrib.auth import views as auth_views
from jobwebsite.ViewsFolder.home import Search
from jobwebsite.ViewsFolder.home import home


urlpatterns=[
    path('', home.home_view, name='home'),
    path('about/', about_us.about, name='about'),
    path('contact/', contact_us.contact, name='contact'),
    path('notification/', notification.notification_view, name='notification'),
    path('profile/', profile.profile_view, name='profile'),
    path('register/', register.register_view, name='register'),
    path('logout/', logout.logout_view, name='logout'),
    path('login/', login.login_view, name='login'),
    path('job_list/', job_listing.job_list_View, name='job_list'),
    path('<int:job_id>/', job_detail.job_detail_view, name='job_detail'),
    path('employer/dashboard/',employer_dashboard.employer_dashboard_view, name='employer_dashboard'),
    path('employee/dashboard/',employee_dashboard.employee_dashboard_view, name='employee_dashboard'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('search/', Search.search_result_view, name='search_result'),
    path('job_application/',job_application.apply_job_view, name='job_application'),
    path('job_posting/',job_posting.create_job_view, name='job_posting'),
]