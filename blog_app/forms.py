from django import forms
from .models import post,category,comment 

choices= category.objects.all().values_list('name','name')

choice_list=[]


for items in choices:
    choice_list.append(items)


class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','author','category','post_body','post_thumb','snippet')

        widgets={

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is Your Post Title'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'post_body':forms.Textarea(attrs={'class':'form-control','placeholder':'This is Your Post Body'}),
            'post_thumb':forms.FileInput(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
            

        }



class EditForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','category','post_body','post_thumb','snippet')

        widgets={

            'title':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'post_body':forms.Textarea(attrs={'class':'form-control'}),
            'post_thumb':forms.FileInput(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
            

        }        







class Comment(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','body')

        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}), 
            'body':forms.Textarea(attrs={'class':'form-control'}),
            
            

        }               