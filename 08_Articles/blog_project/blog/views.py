from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import Article
from .forms import ArticleCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # context = {'title': "Home Page",
    #            'articles':[
    #                {
    #                    'image':"https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
    #                     'category':"Technology",
    #                     'title': 'The Future of AI in Web Development',
    #                     'content': 'Artificial intelligence is rapidly changing how we build and maintain modern web applications, from automated testing to code generation.',
    #                     'author': 'Alex Rivers',
    #                     'created_at': '2026-02-20' # Django's |date filter will parse strings or datetime objects
    #                 },
    #                 {
    #                     'image': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb',
    #                     'category': 'Lifestyle',
    #                     'title': '10 Tips for a Productive Morning',
    #                     'content': 'Starting your day right is the key to maintaining focus and energy throughout your hectic work week. Here is how you can optimize your routine.',
    #                     'author': 'Jordan Smith',
    #                     'created_at': '2026-02-18'
    #                 },
    #                 {
    #                     'image': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085',
    #                     'category': 'Coding',
    #                     'title': 'Mastering Tailwind CSS Layouts',
    #                     'content': 'Tailwind CSS has revolutionized styling by providing utility-first classes that make building complex responsive designs a total breeze.',
    #                     'author': 'Taylor Chen',
    #                     'created_at': '2026-02-15'
    #                 }

    #            ]
    #            }
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'blog/home.html',context)
    # return HttpResponse("<h1>Welcome to Home Page</h1>")

def about(request):
    context = {'title': "About Page"}
    return render(request,'blog/about.html',context)
    # return HttpResponse("<h1>This About Us Page</h1>")

def article_list(request):
    articles = Article.objects.filter(
        author = request.user
        ).order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('blog-home')
    else:            
        form = ArticleCreationForm()

    context = {'form':form}
    return render(request,'blog/article_form.html',context)

@login_required
def update_article(request,id):
    article = Article.objects.get(id = id)
    if request.method == "POST":
        form = ArticleCreationForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('blog-home')
    else:            
        form = ArticleCreationForm(instance=article)
    context = {'form':form}
    return render(request,'blog/article_form.html',context)

@login_required
def delete_article(request,id):
    article = get_object_or_404(Article,id = id)
    # check if the user is the owner
    if article.author != request.user:
        return redirect('article_list')
    
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    
    context = {'article':article}
    return render(request,'blog/article_delete.html',context)
    

@login_required
def article_detail(request,id):
    article = get_object_or_404(Article,id = id)
    context = {'article':article}
    return render(request,'blog/article_detail.html',context)

# forms.py 
# views.py
# urls.py