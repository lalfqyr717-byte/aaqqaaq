from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """Render the main index.html page"""
    return render(request, 'index.html')

def health_check(request):
    """Health check endpoint for Railway"""
    return JsonResponse({'ok': True, 'status': 'healthy'})