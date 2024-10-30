from django.shortcuts import render,redirect
from Accounts.models import Customer_register
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password 
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if Customer_register.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return redirect('/Accounts/')
            
            elif Customer_register.objects.filter(mobile=mobile).exists():
                messages.info(request,"mobile exist")
                return redirect('/Accounts/')
            
            else:
                password = make_password(password)
                new_customer = Customer_register.objects.create(name=name, mobile=mobile, email=email , gender= gender, city=city,state=state, pincode=pincode,address=address, password= password, confirm_password=confirm_password)
                new_customer.save()
                return redirect('/Accounts/login/')                 

        else:
            messages.info(request,"Password did not match")
            return redirect('/Accounts/')
        
    return render(request,"register.html")


def login(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        password = request.POST['password']

        try:

            login_user = Customer_register.objects.get(mobile = mobile)
            if login_user.mobile == int(mobile) and check_password(password, login_user.password):
                request.session['id'] = login_user.id
                return redirect('/Accounts/profile/')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect('/Accounts/login/')
        except ObjectDoesNotExist:
            messages.info(request,"Mobile Does Not Exist")
            return redirect('/Accounts/login/')
    return render(request, 'login.html')


def profile(request):
    return render(request,"profile.html")


def logout(request) :
    request.session.flush()
    return redirect('/Accounts/login/')