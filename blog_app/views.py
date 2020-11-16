from django.shortcuts import render, get_object_or_404
from .models import post,category,comment
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm , EditForm,Comment
from django.urls import reverse_lazy,reverse 
from django.http import HttpResponseRedirect


# Create your views here.

''' These Are All Functional Base View'''

def CategoryView(request,cats):
    category_posts = post.objects.filter(category=cats)
    return render(request,'category.html',{'cats':cats, 'category_posts':category_posts})

def LikeView(request,pk):
    posts = get_object_or_404(post,id=request.POST.get('post_id'))
    liked =False 
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        liked = False
    else:
        posts.likes.add(request.user)
        liked = True       
    
    return HttpResponseRedirect (reverse('post', args=[str(pk)]))



'''These are All Class Base View'''

class HomeView (ListView):
    template_name='index.html'
    model=post
    ordering=['-post_date']

    def get_context_data(self,*args,**kwargs):
        cat_menu=category.objects.all()
        context = super (HomeView, self).get_context_data(*args,**kwargs)
        context ['cat_menu']=cat_menu
        return  context 
        



class PostView(DetailView):
    model = post
    template_name='post.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=category.objects.all ()
        context = super (PostView, self).get_context_data(*args,**kwargs)
        stuff= get_object_or_404 (post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked = False 
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context ['cat_menu']=cat_menu
        context['total_likes'] =total_likes
        context['liked']= liked
        return context   


class AddPost(CreateView):
    model = post 
    form_class=PostForm
    template_name= 'add_post.html'


class AddComment(CreateView):
    model = comment 
    form_class=Comment
    template_name= 'add_comment.html'
    #fields='__all__'    
    success_url = reverse_lazy ('home')
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk'] 
        return super().form_valid(form)

class AddCategory(CreateView):
    model = category 
    template_name= 'add_category.html'
    fields='__all__'
    def get_context_data(self,*args,**kwargs):
        cat_menu=category.objects.all
        context = super (AddCategory, self).get_context_data(*args,**kwargs)
        context ['cat_menu']=cat_menu
        return  context     
    

class UpdatePost(UpdateView):
    model=post 
    form_class=EditForm
    template_name='update_post.html'




class DeletePost(DeleteView):
    model=post 
    template_name='delete_post.html'
    success_url= reverse_lazy('home')





