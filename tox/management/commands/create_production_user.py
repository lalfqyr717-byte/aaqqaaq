from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create or update production user (maqi / 12345) - Idempotent'

    def handle(self, *args, **options):
        User = get_user_model()

        # Check if user exists, if not create it
        if not User.objects.filter(username='maqi').exists():
            prod_user = User.objects.create_superuser('maqi', 'maqi@tox.iq', '12345')
            self.stdout.write(self.style.SUCCESS(f'Successfully created production user'))
        else:
            prod_user = User.objects.get(username='maqi')
            prod_user.set_password('12345')
            prod_user.is_superuser = True
            prod_user.is_staff = True
            prod_user.is_active = True
            prod_user.email = 'maqi@tox.iq'
            prod_user.save()
            self.stdout.write(self.style.WARNING(f'Updated existing production user'))

        self.stdout.write(f'Username: {prod_user.username}')
        self.stdout.write(f'Email: {prod_user.email}')
        self.stdout.write(f'Is superuser: {prod_user.is_superuser}')
        self.stdout.write(f'Is staff: {prod_user.is_staff}')
        self.stdout.write(f'Is active: {prod_user.is_active}')
        self.stdout.write(self.style.SUCCESS('Login credentials: maqi / 12345'))
