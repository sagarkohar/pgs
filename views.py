from django.conf import settings
from django.shortcuts import redirect,render
from django.contrib import messages
from Teachers.models import Teacher
from Events.models import Event 
from AboutUs.models import *
from FrontImage.models import Images
from Classes.models import Classes
from Gallery.models import Drawing,Reading,Playing,Events




def first(request):


    about_us = AboutUs.objects.first()
    front_images = Images.objects.first()
    teachers=Teacher.objects.all()[:4]
    events = Event.objects.all()[:3]
    classes=Classes.objects.all()[:3]
    parents=Parents.objects.all()


    context = {
        "about": about_us,
        "front": front_images,
        "teacher": teachers,
        "event": events,
        "classs":classes,
        "parent":parents,
    }
    return render(request,"index.html",context)

def about(request):

    about=AboutUs.objects.first()
    teachers=Teacher.objects.all()[:4]
    parents=Parents.objects.all()

    context={
       "ab":about,
       "staff":teachers,
       "parent":parents,
    }
    return render(request,"about.html",context)

def classes(request):

    cl=Classes.objects.all()
    return render(request,"class.html",{"classes":cl} )

def teachers(request):
    teacher=Teacher.objects.all()

    
    return render(request,"team.html",{"staff":teacher})

def gallery(request):

    play=Playing.objects.all()
    draw=Drawing.objects.all()
    read=Reading.objects.all()
    event=Events.objects.all()

    context={
        "pl":play,
        "dl":draw,
        "rl":read,
        "e":event,
    }

    
    return render(request,"gallery.html",context)

def event(request):
    events = Event.objects.all()
    return render(request,"event.html",{"events":events})

def contact(request):
    return render(request,"contact.html")

def staff(request,id):

    faculty=Teacher.objects.get(id=id)
    return render(request,"staff.html",{"staff":faculty})

def feedback(request):

    if request.method=="POST":

        p_name=request.POST.get('full_name')  
        p_phone_number=request.POST.get('phone_number')
        p_address=request.POST.get('address')     
        p_profile_picture=request.FILES.get('profile_picture')
        p_message=request.POST.get('message')


        if p_profile_picture:
            # Create the Parents object with the image
            insert_data = Parents(
                name=p_name,
                opnion=p_message,
                address=p_address,
                image=p_profile_picture,
                contact_number=p_phone_number
            )
        else:
            # Create the Parents object without the image
            insert_data = Parents(
                name=p_name,
                opnion=p_message,
                address=p_address,
                contact_number=p_phone_number
            )


        insert_data.save()
        

    return render(request,"contact.html")


def register(request,id):

    classs=Classes.objects.get(id=id)

    return render(request,"register.html",{"cls":classs})


def bookSeat(request):

    if request.method=="POST":
        name=request.POST.get("name")
        grade=request.POST.get("grade")
        address=request.POST.get("address")
        contact_number=request.POST.get("contact_number")

        insert=Book(
            student_name=name,
            student_grade=grade,
            student_address=address,
            contact_number=contact_number
        )

        insert.save()

        messages.success(request, 'Seat has been booked Please visit us!')

        return redirect('index.html')
    

    return redirect('/')






        





