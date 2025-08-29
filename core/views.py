from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request,'index.html',{'posts':posts})

@login_required
def create_post(request):

    if request.method =='POST':
        form= PostForm(request.POST, request.FILES)

        if form.is_valid():
            post=form.save(commit=False)
            post.user =request.user
            post.save()
            messages.success(request, "Post created successfully!")

            return redirect('home')
        else:
            messages.error(request, "There was an error creating the post. Please check the form.")
  
    else:
        form = PostForm()

    return render(request,'create_post.html', {'form':form})

@login_required
def update_post(request,post_id):
    updated_post = get_object_or_404(Post,pk=post_id,user=request.user)
    if request.method=='POST':
        
        form = PostForm(request.POST,request.FILES,instance=updated_post)
        if form.is_valid():
            updated_post= form.save(commit=False)
            updated_post.user=request.user
            updated_post.save()
            messages.success(request, "Post updated successfully!")

            return redirect('home')
        else:
            messages.error(request, "There was an error updating the post. Please check the form.")
    else:
        form = PostForm(instance=updated_post)
    return render(request,'create_post.html', {'form':form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id,user=request.user)
    if request.method=='POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")

        return redirect('home')
    return render(request,'confirm_delete.html',{"post":post})