from dataclasses import field
from django import forms
from django.forms import ModelForm
#from django import forms
from .models import project

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title','description','featured_image','demo_link','source_link','tag']

        widgets={
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args,**kwargs):
        super(projectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})