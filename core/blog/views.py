from django.shortcuts import render
from .models import Category, Tag, Post
from itertools import chain
from django.shortcuts import redirect
from django.http import Http404


def gohome(request):
    return redirect('home')



def home_view(request):
    list_cat = navigation_home_view()
    posts = Post.objects.filter(title = "xyzz")
    for lc in list_cat:
        result = Post.objects.filter(category = lc).order_by('-id')[0:6]   
        posts = list(chain(posts, result))
    context = {
        'list_cat' : list_cat,
        'posts' : posts,
    }
    return render(request, 'home.html',context)



def category_list_view(request, catname):
    catname = catname.replace('-',' ') #slugify
    catname = catname.lower()
    list_cato = navigation_home_view()
    result = False
    for lc in list_cato:
        ctn = lc.name.lower()
        if catname == ctn :
            result = lc.name
            qcat = lc

    if result == False :
        raise Http404

    list_tag = Tag.objects.filter(category = qcat)
    posts = Post.objects.filter(category = qcat).order_by('-id')
    
    context = {
        'catname' : result,
        'posts' : posts,
        'list_cat' : list_cato,
        'list_tag': list_tag ,
    }
    return render(request, 'category-list.html',context)



def tag_list_view(request, catname, tagname):
    catname = catname.replace('-',' ') #slugify
    catname = catname.lower()
    
    tagname = tagname.lower()
    list_cato = navigation_home_view()
    list_tag = Tag.objects.all()

    result = False
    for tg in list_tag:
        tgn = tg.name.lower()
        ctn = tg.category.name.lower()
        if tagname == tgn and catname == ctn :
            result = tg.name
            qtg = tg

    if result == False :
        raise Http404

    posts = Post.objects.filter(tag = qtg).filter(category = qtg.category).order_by('-id')

    list_tag = Tag.objects.filter(category=qtg.category)

    context = {
        'catname' : catname,
        'tagname' : result,
        'posts' : posts,
        'list_cat' : list_cato,
        'list_tag': list_tag ,
    }
    return render(request, 'tag-list.html',context)



def post_details_view(request, myurl):
    list_cato = navigation_home_view()

    myurl = myurl.lower()
    
    try:
        the_post = Post.objects.get(url = myurl)
    except Post.DoesNotExist:
        raise Http404
        
    list_tag = Tag.objects.filter(category = the_post.category)
    context = {
        'the_post' : the_post,
        'list_cat' : list_cato,
        'list_tag': list_tag ,
    }
    return render(request, 'post-details.html',context)



###################################

def navigation_home_view ():
    list_cato = Category.objects.order_by('rank')
    return list_cato

