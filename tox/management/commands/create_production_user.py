from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create or update production user (user / user123) as per AGENTS.md specification'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Delete existing user if exists
        if User.objects.filter(username='user').exists():
            User.objects.filter(username='user').delete()
            self.stdout.write(self.style.WARNING('Deleted existing user'))
        
        # Create new production user
        prod_user = User.objects.create_superuser('user', 'user@tox.iq', 'user123')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created production user'))
        self.stdout.write(f'Username: {prod_user.username}')
        self.stdout.write(f'Email: {prod_user.email}')
        self.stdout.write(f'Is superuser: {prod_user.is_superuser}')
        self.stdout.write(f'Is staff: {prod_user.is_staff}')
        self.stdout.write(f'Is active: {prod_user.is_active}')
        self.stdout.write(self.style.SUCCESS('Login credentials: user / user123'))
