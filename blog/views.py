from django.shortcuts import redirect, render,HttpResponse
from django.http import request
from blog.models import Career_Oppotunitie, Common_strategie,Exam,Career_Oppotunitie_Comment,Oppotunitie_Comment_Reply,strategyQuesition, blogAds
from django.contrib import messages
from home.models import Newslatter_Subscriber
from django.contrib.auth.decorators import login_required
# Create your views here.
def strategies(request):
    
    allstrategies = Common_strategie.objects.all()
    ads = blogAds.objects.all()
    print(allstrategies)
    context = {'allstrategies': allstrategies,'ads':ads}
    return render(request,'Eduguider/strategies.html', context)
def strategiesPost(request, slug):
    
    strategie = Common_strategie.objects.filter(slug=slug).first()
    ads = blogAds.objects.all()
    comments = strategyQuesition.objects.filter(post=strategie)
    context = {'strategie' : strategie,'ads':ads, 'comments':comments}
    return render(request,'Eduguider/strategydetails.html', context)
def opportunities(request):
   
    allopportunities = Career_Oppotunitie.objects.all()
    ads = blogAds.objects.all()
    print(allopportunities)
    context = {'allopportunities' : allopportunities}
    return render(request,'Eduguider/oppor.html', context)
@login_required
def opportunitiesPost(request, slug):
    Post = Career_Oppotunitie.objects.filter(slug=slug).first()
    comments = Career_Oppotunitie_Comment.objects.filter(post=Post)
    context = {'Post' : Post,'comments':comments}
    return render(request,'Eduguider/oppordetails.html', context)
@login_required
def opportunitiesComment(request, slug):
    if request.method =="POST":
       comment = request.POST.get('comment')
       user = request.user
       post = Career_Oppotunitie.objects.get(slug=slug)
       comment=Career_Oppotunitie_Comment(comment=comment,user=user,post=post)
       comment.save()
       messages.success(request, "Your comment has been savedsuccessfully")
    return redirect(f'/explore/opportunities/{post.slug}')
def strategiesPostComment(request, slug):
    if request.method =="POST":
       comment = request.POST.get('comment')
       user = request.user
       post = Common_strategie.objects.get(slug=slug)
       comment=strategyQuesition(comment=comment,user=user,post=post)
       comment.save()
       messages.success(request, "Your comment has been savedsuccessfully")
    return redirect(f'/explore/strategies/{post.slug}')