from django.shortcuts import render, HttpResponse
from .models import Article

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
