from django.shortcuts import render, redirect, get_object_or_404
from .models import CounselRecomment, CounselComment, CounselPost, JarPost
from .forms import CounselCommentForm, CounselPostForm, CounselRecommentForm, JarPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def main2(request):
    return render (request, 'main2.html')

def home(request):
    post = CounselPost.objects.filter().order_by('-post_like')
    return render(request, 'home.html', {'post':post})
    # return render(request, '#html파일이름', {'post':post})

def write_post(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = CounselPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            # return redirect('고민상담으로 이동')
    else:
        form = CounselPostForm()
        return render(request, 'index.html', {'form':form})
        #return render(request, '포스트작성칸html', {'form':form})

def counsel_post_list(request):
    posts = CounselPost.objects.all().order_by('-date')
    return render(request, 'main2.html', {'posts':posts})
    #return render(request, '리스트보여주는 html', {'posts':posts})

def post_detail(request, id):
    post = CounselPost.objects.get(id=id)
    #comment = CounselComment.objects.get(id=id)

    comment_form = CounselCommentForm()
    recomment_form = CounselRecommentForm()

    comment_list = CounselComment.objects.filter(post=post)
    #recomment_list = CounselRecomment.objects.filter(comment=comment)
    context={
        'post':post,
        'comment_form' : comment_form,
        'comment_list':comment_list,
        'recomment_form':recomment_form,
        # 'recomment_list':recomment_list
    }
    return render(request, 'detail.html', context)
    #return render(request, '디테일페이지', {'post':post})

def post_update(request, id):
    post = CounselPost.objects.get(id=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = CounselPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
            #return redirect('리스트')
    else: 
        form = CounselPostForm(instance=post)
        return render(request, 'index.html', {'form':form,'id':id})
        #return render(request, '작성하는 html', {'form':form,'id':id})
    
def post_delete(request, id):
    post = CounselPost.objects.get(pk=id)
    post.delete()
    return redirect('list')
    # return redirect('리스트')

def create_comment(request, id):
    filled_form = CounselCommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = CounselPost.objects.get(pk=id)
        finished_form.save()
    return redirect('post_detail', id)

def create_recomment(request, id):
    comment = get_object_or_404(CounselComment, pk=id)

    filled_form = CounselRecommentForm(request.POST)

    if filled_form.is_valid():
        filled_form.save()
    # filled_form = CounselRecommentForm(request.POST)

    # if filled_form.is_valid():
    #     recomment = filled_form.save(commit=False)
    #     #recomment.author = request.user
    #     recomment.comment = comment
    #     recomment.recomment = recomment
    #     recomment.save()
    #     #filled_form.save()
    return redirect('post_detail', id)

def write_jar(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = JarPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            # return redirect('고민상담으로 이동')
    else:
        form = JarPostForm()
        return render(request, 'index.html', {'form':form})
        #return render(request, '포스트작성칸html', {'form':form})

def jar_list(request):
    posts = JarPost.objects.all().order_by('-date')
    return render(request, 'main3.html', {'posts':posts})


def like_post(request, post_id):
    post = get_object_or_404(CounselPost, id=post_id)

    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    # post.like_users.toggle(request.user)
    return redirect('post_detail', post_id=post_id)

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(CounselComment, id=comment_id)
    comment.like_users.toggle(request.user)
    return redirect('comment_detail', comment_id=comment_id)

@login_required
def like_recomment(request, recomment_id):
    recomment = get_object_or_404(CounselRecomment, id=recomment_id)
    recomment.like_users.toggle(request.user)
    return redirect('recomment_detail', recomment_id=recomment_id)

@login_required
def like_jarpost(request, jarpost_id):
    jarpost = get_object_or_404(JarPost, id=jarpost_id)
    jarpost.like_users.toggle(request.user)
    return redirect('jarpost_detail', jappost_id=jarpost_id)