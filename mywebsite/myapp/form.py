from django import forms
# from .models import Image

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['name', 'image', 'designation']

# forms.py
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image', 'designation']

# from myapp import models 
# from django.forms import fields  
# from .models import Image  
# from django import forms  
  
  
# class UserImage(forms.ModelForm):  
#     class meta:  
#         # To specify the model to be used to create form  
#         models = Image  
#         # It includes all the fields of model  
#         fields = '__all__'  