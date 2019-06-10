from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

class Command(BaseCommand):
    admin, adminCreated = Group.objects.get_or_create(name='Admin')
    curator, curatorCreated = Group.objects.get_or_create(name='Curator')

    authorCT = ContentType.objects.get(model='author')
    authorPerms = Permission.objects.filter(content_type=authorCT)

    for perm in authorPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    bitpayInvoiceCT = ContentType.objects.get(app_label='podverse_db', model='bitpayinvoice')
    bitpayInvoicePerms = Permission.objects.filter(content_type=bitpayInvoiceCT)

    for perm in bitpayInvoicePerms:
        admin.permissions.add(perm)

    categoryCT = ContentType.objects.get(app_label='podverse_db', model='category')
    categoryPerms = Permission.objects.filter(content_type=categoryCT)

    for perm in categoryPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    episodeCT = ContentType.objects.get(model='episode')
    episodePerms = Permission.objects.filter(content_type=episodeCT)

    for perm in episodePerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    feedUrlCT = ContentType.objects.get(model='feedurl')
    feedUrlPerms = Permission.objects.filter(content_type=feedUrlCT)

    for perm in feedUrlPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    paypalOrderCT = ContentType.objects.get(model='paypalorder')
    paypalOrderPerms = Permission.objects.filter(content_type=paypalOrderCT)

    for perm in paypalOrderPerms:
        admin.permissions.add(perm)

    playlistCT = ContentType.objects.get(model='playlist')
    playlistPerms = Permission.objects.filter(content_type=playlistCT)

    for perm in playlistPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    podcastCT = ContentType.objects.get(model='podcast')
    podcastPerms = Permission.objects.filter(content_type=podcastCT)
    
    for perm in podcastPerms:
        admin.permissions.add(perm)
        curator.permissions.add(perm)

    userCT = ContentType.objects.get(app_label="podverse_db", model='user')
    userPerms = Permission.objects.filter(content_type=userCT)

    for perm in userPerms:
        admin.permissions.add(perm)

    djangoGroupCT = ContentType.objects.get(app_label="auth", model='group')
    djangoGroupPerms = Permission.objects.filter(content_type=djangoGroupCT)

    for perm in djangoGroupPerms:
        admin.permissions.add(perm)

    djangoUserCT = ContentType.objects.get(app_label="auth", model='user')
    djangoUserPerms = Permission.objects.filter(content_type=djangoUserCT)

    for perm in djangoUserPerms:
        admin.permissions.add(perm)

    def handle(self, *args, **options):
        self.stdout.write("Groups created.")
