from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create or update maqi user with password 12345'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Delete existing maqi user if exists
        if User.objects.filter(username='maqi').exists():
            User.objects.filter(username='maqi').delete()
            self.stdout.write(self.style.WARNING('Deleted existing maqi user'))
        
        # Create new maqi user
        maqi_user = User.objects.create_superuser('maqi', 'maqi@tox.iq', '12345')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created maqi user'))
        self.stdout.write(f'Username: {maqi_user.username}')
        self.stdout.write(f'Email: {maqi_user.email}')
        self.stdout.write(f'Is superuser: {maqi_user.is_superuser}')
        self.stdout.write(f'Is staff: {maqi_user.is_staff}')
        self.stdout.write(f'Is active: {maqi_user.is_active}')
        self.stdout.write(self.style.SUCCESS('Login credentials: maqi / 12345'))