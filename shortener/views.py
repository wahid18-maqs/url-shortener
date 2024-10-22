from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from urllib.parse import urlparse

def extract_domain(long_url):
    """Extracts the domain from the long URL."""
    parsed_url = urlparse(long_url)
    return parsed_url.netloc.replace('www.', '')  # Remove 'www.' if present

def home(request):
    short_url = None

    if request.method == 'POST':
        long_url = request.POST['long_url']
        domain = extract_domain(long_url)
        short_url = domain  # Use the domain as the short URL

        # Check if the short URL already exists
        if URL.objects.filter(short_url=short_url).exists():
            short_url += '-' + str(URL.objects.filter(short_url__startswith=domain).count() + 1)  # Add a unique suffix

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
