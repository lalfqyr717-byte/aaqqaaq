from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the main index.html page"""
    return render(request, 'index.html')

def health_check(request):
    """Health check endpoint for Railway"""
    return JsonResponse({'ok': True, 'status': 'healthy'})

@csrf_exempt
def auth_login(request):
    """API endpoint for frontend authentication"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            account_type = data.get('accountType', 'admin')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Map Django user to the format expected by frontend
                user_data = {
                    'username': user.username,
                    'email': user.email,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                    'role': 'admin' if user.is_superuser else account_type,
                    'permissions': [
                        'dashboard.open',
                        'sales.open',
                        'warehouse.open',
                        'purchase.open',
                        'accounts.manage_debts',
                        'accounts.view_profits',
                        'admin.manage_employees',
                        'admin.settings'
                    ] if user.is_superuser else [f'{account_type}.open']
                }
                return JsonResponse({
                    'ok': True,
                    'user': user_data,
                    'accessToken': ''  # No JWT token in session-based auth
                })
            else:
                return JsonResponse({
                    'ok': False,
                    'reason': 'INVALID_CREDENTIALS'
                }, status=401)
        except Exception as e:
            return JsonResponse({
                'ok': False,
                'reason': str(e)
            }, status=400)
    
    return JsonResponse({'ok': False, 'reason': 'Method not allowed'}, status=405)

def api_session(request):
    """API endpoint for session management"""
    if request.user.is_authenticated:
        user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'is_staff': request.user.is_staff,
            'is_superuser': request.user.is_superuser,
            'role': 'admin' if request.user.is_superuser else 'admin',
            'permissions': [
                'dashboard.open',
                'sales.open',
                'warehouse.open',
                'purchase.open',
                'accounts.manage_debts',
                'accounts.view_profits',
                'admin.manage_employees',
                'admin.settings'
            ] if request.user.is_superuser else ['admin.open']
        }
        return JsonResponse({
            'authenticated': True,
            'user': user_data,
            'accessToken': ''
        })
    return JsonResponse({'authenticated': False})

@csrf_exempt
def api_sync(request):
    """API endpoint for data synchronization"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Placeholder for sync logic
            return JsonResponse({
                'success': True,
                'data': data
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)