from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = 'Create seller and customer agent users automatically'

    def handle(self, *args, **kwargs):
        # Create or get groups
        seller_group, created = Group.objects.get_or_create(name='Seller')
        agent_group, created = Group.objects.get_or_create(
            name='Customer Agent')
        admin_group, created = Group.objects.get_or_create(
            name='Admin')  # Add admin group

        # Create Seller Users
        if not User.objects.filter(username='seller1').exists():
            seller1 = User.objects.create_user(
                username='seller1',
                email='seller1@example.com',
                password='password123',
                first_name='Seller',
                last_name='One'
            )
            seller1.groups.add(seller_group)
            self.stdout.write(self.style.SUCCESS(
                'Successfully created seller1'))

        if not User.objects.filter(username='seller2').exists():
            seller2 = User.objects.create_user(
                username='seller2',
                email='seller2@example.com',
                password='password123',
                first_name='Seller',
                last_name='Two'
            )
            seller2.groups.add(seller_group)
            self.stdout.write(self.style.SUCCESS(
                'Successfully created seller2'))

        # Create Customer Agent Users
        if not User.objects.filter(username='agent1').exists():
            agent1 = User.objects.create_user(
                username='agent1',
                email='agent1@example.com',
                password='password123',
                first_name='Agent',
                last_name='One'
            )
            agent1.groups.add(agent_group)
            self.stdout.write(self.style.SUCCESS(
                'Successfully created agent1'))

        if not User.objects.filter(username='agent2').exists():
            agent2 = User.objects.create_user(
                username='agent2',
                email='agent2@example.com',
                password='password123',
                first_name='Agent',
                last_name='Two'
            )
            agent2.groups.add(agent_group)
            self.stdout.write(self.style.SUCCESS(
                'Successfully created agent2'))

       # Create Admin Users
        if not User.objects.filter(username='admin1').exists():
            admin1 = User.objects.create_user(
                username='admin1',
                email='admin1@example.com',
                password='password123',
                first_name='Admin',
                last_name='One'
            )
            admin1.is_staff = True  # Set as staff
            admin1.is_superuser = True  # Set as superuser for admin privileges
            admin1.groups.add(admin_group)
            admin1.save()  # Save changes after updating superuser status
            self.stdout.write(self.style.SUCCESS(
                'Successfully created admin1'))

        if not User.objects.filter(username='admin2').exists():
            admin2 = User.objects.create_user(
                username='admin2',
                email='admin2@example.com',
                password='password123',
                first_name='Admin',
                last_name='Two'
            )
            admin2.is_staff = True  # Set as staff
            admin2.is_superuser = True  # Set as superuser for admin privileges
            admin2.groups.add(admin_group)
            admin2.save()  # Save changes after updating superuser status
            self.stdout.write(self.style.SUCCESS(
                'Successfully created admin2'))

        self.stdout.write(self.style.SUCCESS(
            'All users and groups created successfully.'))
