import datetime
from datetime import datetime, time, timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from requests import request, session
from django.contrib import messages
from plyer import notification
from .models import RequistionForm, UserDetails, FeedbackForm

# Create your views here.

def home(request):
    return render(request,"CSRP/home.html")

def about(request):
    return render(request, "CSRP/about.html")

def contactus(request):
    return render(request, "CSRP/contactus.html")

def portal(request):
    return render(request, "CSRP/portal.html")

def Register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        phone_number = request.POST.get('phone_number')
        telephone_number = request.POST.get('telephone_number')
        cnic = request.POST.get('cnic')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password)
        print(confirmpassword)
        print(phone_number)
        print(telephone_number)
        print(cnic)
        print(city)
        print(gender)

        if password!=confirmpassword:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            user=User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            UserDetails.objects.create(
                phone_number=phone_number,
                telephone_number=telephone_number,
                gender=gender,
                cnic=cnic,
                city=city,
                user=user.id
            )
            return redirect('login')

    return render (request,"CSRP/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login to log the user in
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "CSRP/login.html")


def logout(request):
    return redirect('login')

@never_cache
@login_required
@require_http_methods(["GET", "POST", "UPDATE"])
def dashboard(request):
    if request.method == "POST":
        # Your existing POST handling logic remains unchanged
        pass

    requistionid = request.GET.get("requistionsubject_id")
        
    if requistionid:
            requistionforms = RequistionForm.objects.filter(
                user_id=request.user.id, id=requistionid
        )

    else:  # Handle GET requests
        # Fetching the requisition forms for non-superuser
        requistionforms = RequistionForm.objects.filter(user_id=request.user.id)

        # If the user is a superuser, adjust the requisition forms accordingly
        if request.user.is_superuser:
            if request.user.is_superuser == 2:
                requistionforms = RequistionForm.objects.filter(department__contains='Electrical')
            elif request.user.is_superuser == 3:
                requistionforms = RequistionForm.objects.filter(department__contains='Civil')
            else:
                requistionforms = RequistionForm.objects.all()
    
    return render(
        request,
        "CSRP/dashboard.html",
        {
            "requistion_forms": requistionforms,

            # Pass other necessary context data as needed
        },
    )


@login_required
def addrequistion(request):
    return render(request, "CSRP/requistionportal.html")


@login_required
def requistionportal(request):
    return render(request, "CSRP/requistionportal.html")


@login_required
def Requistionform(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        department= request.POST.get('department')
        requistion_type = request.POST.get('requistion_type')
        requistionsubject = request.POST.get('requistionsubject')
        noofarticles = request.POST.get('noofarticles')
        requistiondescription = request.POST.get('requistiondescription')
        assignto = request.POST.get('assignto')
        comment = request.POST.get('comment')
        comments = request.POST.get('comments')
        designation = request.POST.get('designation')
        extensionnumber = request.POST.get('extensionnumber')

        print(user)
        print(department)
        print(requistion_type)
        print(requistionsubject)
        print(noofarticles)
        print(requistiondescription)
        print(assignto)
        print(comment)
        print(comments)
        print(designation)
        print(extensionnumber)

        requistionform = RequistionForm.objects.create(
            user_id=user,
            department=department,
            requistion_type=requistion_type,
            requistionsubject=requistionsubject,
            noofarticles=noofarticles,
            requistiondescription=requistiondescription,
            assignto=assignto,
            comment=comment,
            comments=comments,
            designation=designation,
            extensionnumber=extensionnumber,
        )
        requistionform.save()
        
        return redirect('dashboard')
    
    requistionform = RequistionForm.objects.filter(user_id=request.user.id)

    return render(request, 'CSRP/requistionform.html', {
        'requistionform': requistionform,
    })


@login_required
def electricalrequistionform(request):
    return render(request, "CSRP/electricalrequistionform.html")


@login_required
def requistiondetails(request):
    if request.method == "GET":
        requistionid = request.GET.get("requistionsubject_id")
        
        requistionforms = RequistionForm.objects.filter(user_id=request.user.id, id=requistionid)

        if request.user.is_superuser:
             requistionforms = RequistionForm.objects.filter(id=requistionid)
        
        first_requistionform = requistionforms.first()
        print(first_requistionform)
        user = User.objects.get(id=first_requistionform.user_id)
        userdetails = UserDetails.objects.get(user=user.id)
        print(user)
        print(userdetails)

    return render(request, "CSRP/requistiondetails.html", {
        'requistion_forms': requistionforms,
        'user': user,
        'userdetails' : userdetails,
    })


@login_required
def update(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        requistionid = request.POST.get('requistionid')
        assign_to = request.POST.get('assign_to')
    #    comment = request.POST.get('comment')

        # Update the fields directly without fetching the queryset
        RequistionForm.objects.filter(id=requistionid).update(
            status=status,
            assignto=assign_to,  # Add this line to update the assign_to field
       #    comment=comment,
            updatedon=datetime.now(),
            updatedtime=datetime.now()
        )
        return redirect("dashboard")
    return render(request, "CSRP/updatesection.html")


def applybutton():
    if request.method == "UPDATE":
        applybutton = RequistionForm.objects.filter(user_id=request.user.id) 


@login_required
def delete(request, requistionid):
    if request.method == 'POST':
        requistion = get_object_or_404(RequistionForm, pk=requistionid)
        requistion.delete()
        return HttpResponseRedirect('dashboard')  # Redirect to the dashboard page
    return HttpResponseRedirect('dashboard')  # Redirect to the dashboard page


@login_required
def logsheetdetails(request):
    if request.method == 'GET':
        requistionforms = RequistionForm.objects.filter(user_id=request.user.id)

        if request.user.is_superuser:
            if request.user.is_superuser == 3:
                requistionforms = RequistionForm.objects.filter(department__contains='Civil')
            elif request.user.is_superuser == 2:
                requistionforms = RequistionForm.objects.filter(department__contains='Electrical')
            else:
                requistionforms = RequistionForm.objects.all()
            # Add more conditions for other superuser cases as needed

    return render(request, "CSRP/logsheetdetails.html", {"requistion_forms": requistionforms,})


#@login_required
#def comments(request, requistionid):
#    print(requistionid)
#    if request.method == "GET":
#        owner = RequistionForm.objects.get(id=requistionid)
#        comments = owner.comments_set.all()
#        return render(request, "CSRP/comments.html", {"comments": comments, "id":requistionid})
#    if request.method == 'POST':
#        comments_txt = request.POST.get('comments')
#        requistionid = request.POST.get('requistionid')
#        # Get the RequistionForm instance
#        owner = RequistionForm.objects.get(id=requistionid)
#        commentpostername = f"{request.user.first_name} {request.user.last_name}"
#        print(commentpostername)
#        # Create a new comment associated with the RequistionForm
#        comment = Comments.objects.create(comment=comments_txt, owner=owner, commentsubmiton=datetime.now(),commentposter=commentpostername)
#        comment.save()
#        return redirect('comments', requistionid=requistionid)


@login_required
def feedbackform(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        csrno = request.POST.get('csrno')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')

        print(name)
        print(csrno)
        print(phonenumber)
        print(message)

        feedbackform = FeedbackForm.objects.create(
            name=name,
            csrno=csrno,
            phonenumber=phonenumber,
            message=message,
        )
        feedbackform.save()
        return redirect('dashboard')
    
    return render(request,"CSRP/feedbackform.html")


@login_required
def feedbacksdetails(request):
    feedbackforms = FeedbackForm.objects.all()
    return render(request, "CSRP/feedbacksdetails.html", {'feedbackforms': feedbackforms})

#@login_required
#def message(request):
#    return render(request, "CSRP/message.html")

@login_required
def notification(request):
    if request.method == 'POST':
        # Assuming you have a form for requisitions, and the user is submitting it
        # Save the requisition
        requisition = RequistionForm(user=request.user.id)
        requisition.save()

        # Notify the user
        notification.notify(
            title='Notification',
            message='Your requisition has been posted successfully!',
            app_icon=None,
            timeout=10
        )

    return render(request, "CSRP/dashboard.html")










