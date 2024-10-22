from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import random
import string

def generate_short_url(length=6):
    """Helper function to generate a random short URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def home(request):
    short_url = None

    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        
        # Save the long URL and short URL to the database
        url = URL(long_url=long_url, short_url=short_url)
        url.save()

    return render(request, 'shortener/home.html', {'short_url': short_url})

def redirect_url(request, short_url):
    """Redirects to the long URL associated with the short URL."""
    url = get_object_or_404(URL, short_url=short_url)
    url.hits += 1  # Increment the hits counter
    url.save()  # Save the updated count
    return redirect(url.long_url)

def stats(request):
    """Display statistics for all URLs."""
    urls = URL.objects.all()  # Fetch all URL records
    return render(request, 'shortener/stats.html', {'urls': urls})
