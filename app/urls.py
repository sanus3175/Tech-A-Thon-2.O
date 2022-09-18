from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    # path('', views.home),
    path('', views.BlogView.as_view(), name="home"),
    path('blog-detail/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

