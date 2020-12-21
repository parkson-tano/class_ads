from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginUser
from products.models import Product_upload
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email
# Create your views here.

# @login_required
def index(request):
    pro = Product_upload.objects.all()
    return render(request, 'index.html', {'pro':pro})

def Ulogin(request):
    loginUser = LoginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')  
        else:
            messages.error(request, 'invalid creditials')
            return render(request, 'login.html', {'loginUser':loginUser})
          
    else:
        return render(request, 'login.html', {'loginUser':loginUser})

def register(request):
    regform = RegisterForm()
    
    if  request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if (len(pass1) > 8 and pass1 == pass2):
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already exist')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'email already taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
                user.save()
            return redirect('login')
        else:
            messages.error(request, f'passwords do not match')   
            return render(request, 'register.html', {'reg': regform})
    else:  
        return render(request, 'register.html', {'reg': regform})

def profile(request):
    return render(request, 'profile.html')

def Userlogout(request):
    logout(request)
    return redirect('/')
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change')
            return redirect('profile')
        else:
            return render(request, 'password_change.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'password_change.html', {'form':form})

def password_reset_request(request):
    password_reset_form = PasswordResetForm()
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "forgotpassword/reset_subject.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message has been sent to your email')
                    return redirect ("/")
            messages.error(request, 'Email address in invalid')
            return render(request=request, template_name="forgotpassword/password_reset.html", context={"password_reset_form":password_reset_form})
    return render(request=request, template_name="forgotpassword/password_reset.html", context={"password_reset_form":password_reset_form})