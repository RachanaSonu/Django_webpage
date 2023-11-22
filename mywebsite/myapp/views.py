from django.shortcuts import redirect, render
from .models import Cdata, Feedback,Image
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    stdform=Cdata.objects.all()
    return render(request, 'services.html',{'stdform':stdform})

def adddata(request):
    if request.method=='GET':
        return render(request,'Sform.html')
    else:
        Cdata(Instructor=request.POST.get('Instructor'),
              Program_Language=request.POST.get('Program_Language'),
              Duration_Months=request.POST.get('Duration_Months'),
              Start_Date=request.POST.get('Start_Date'),
              End_Date=request.POST.get('End_Date'),
              Fee=request.POST.get('Fee')).save()
        
        stdform=Cdata.objects.all()
        return render(request,'services.html',{'stdform':stdform})

def update_data(request,id):
    data=Cdata.objects.get(id=id)
    return render(request,'updatedata.html',{'data':data})

def save_update_data(request,id):
    data=Cdata.objects.get(id=id)
    data.Instructor=request.POST.get('Instructor')
    data.Program_Language=request.POST.get('Program_Language')
    data.Duration_Months=request.POST.get('Duration_Months')
    data.Start_Date=request.POST.get('Start_Date')
    data.End_Date=request.POST.get('End_Date')
    data.Fee=request.POST.get('Fee')
    data.save()
    return redirect(services)

def delete_data(request,id):
    data=Cdata.objects.get(id=id)
    data.delete()
    return redirect(services)

# def gallery(request):
#     if request.method == 'POST':
#         image_form = Image(request.POST, request.FILES)
#         if image_form.is_valid():
#             image_form.save()
#             return redirect('gallery')  # Redirect to the same page after successful upload
#     else:
#         image_form = Image()

#     images = Image.objects.all()  # Replace YourImageModel with your actual model
#     return render(request, 'gallery.html', {'image_form': image_form, 'images': images})

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def feedback(request):
    data = Feedback.objects.all()
    return render(request, 'feedback.html', {'data': data})

def feed_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        rating = request.POST.get('rating', '')
        comment = request.POST.get('comment', '')

        # Save feedback to the database
        Feedback.objects.create(name=name, rating=rating, comment=comment)

        # Fetch feedback data again after saving
        data = Feedback.objects.all()
        return render(request, 'feedback.html', {'data': data})

    return render(request, 'feedback.html')

# from .form import UserImage  
# from .models import Image  
  
# def image_request(request):  
#     if request.method == 'POST':  
#         form = UserImage(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
  
#             # Getting the current instance object to display in the template  
#             img_object = form.instance  
              
#             return render(request, 'gallery.html', {'form': form, 'img_obj': img_object})  
#     else:  
#         form = UserImage()  
  
#     return render(request, 'gallery.html', {'form': form})  

from .form import ImageForm
from .models import Image

def image_request(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = form.save()
            return render(request, 'gallery.html', {'img_obj': img_obj, 'form': form})
        else:
            print(form.errors)  # Check the console or logs for validation errors
    else:
        form = ImageForm()
        img1=Image.objects.all()
        # print(img1)

    return render(request, 'gallery.html', {'form': form,'img1':img1})


    