from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from podverse_db.models import Podcast

class Command(BaseCommand):
    admin, adminCreated = Group.objects.get_or_create(name='Admin')
    curator, curatorCreated = Group.objects.get_or_create(name='Curator')

    episodeCT = ContentType.objects.get(model='episode')
    episodePerms = Permission.objects.filter(content_type=episodeCT)

    for perm in episodePerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    podcastCT = ContentType.objects.get(model='podcast')
    podcastPerms = Permission.objects.filter(content_type=podcastCT)
    
    for perm in podcastPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    groupCT = ContentType.objects.get(model='group')
    groupPerms = Permission.objects.filter(content_type=groupCT)

    for perm in groupPerms:
        admin.permissions.add(perm)

    userCT = ContentType.objects.get(model='user')
    userPerms = Permission.objects.filter(content_type=userCT)

    for perm in userPerms:
        admin.permissions.add(perm)

    def handle(self, *args, **options):
        self.stdout.write("Groups created.")
