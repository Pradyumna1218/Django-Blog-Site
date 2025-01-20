from django.shortcuts import render

posts = [
    {
        'author': 'Pradyumna',
        'title': 'Blog Post 1',
        'content': 'First Post Created',
        'date_posted': 'Jan 20, 2025'
    },
    {
        'author': 'Kriti',
        'title': 'Blog Post 2',
        'content': 'My GU',
        'date_posted': 'Jan 25, 2025'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

