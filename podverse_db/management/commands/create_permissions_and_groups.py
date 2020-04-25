from django.apps import apps
from django.contrib.admin.models import LogEntry
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

class Command(BaseCommand):
    # Create Permissions
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    # Create Groups
    admin, adminCreated = Group.objects.get_or_create(name='Admin')
    curator, curatorCreated = Group.objects.get_or_create(name='Curator')

    # ACCOUNTCLAIMTOKEN
    accountClaimTokenCT = ContentType.objects.get(app_label='podverse_db', model='accountclaimtoken')
    accountClaimTokenPerms = Permission.objects.filter(content_type=accountClaimTokenCT)
    accountClaimTokenPermView = accountClaimTokenPerms[3]
    admin.permissions.add(accountClaimTokenPermView)

    # APPSTOREPURCHASE
    appStorePurchaseCT = ContentType.objects.get(app_label='podverse_db', model='appstorepurchase')
    appStorePurchasePerms = Permission.objects.filter(content_type=appStorePurchaseCT)
    appStorePurchasePermView = appStorePurchasePerms[3]
    admin.permissions.add(appStorePurchasePermView)

    # AUTHOR
    authorCT = ContentType.objects.get(model='author')
    authorPerms = Permission.objects.filter(content_type=authorCT)
    authorPermView = authorPerms[3]
    admin.permissions.add(authorPermView)

    # BITPAYINVOICE
    bitpayInvoiceCT = ContentType.objects.get(app_label='podverse_db', model='bitpayinvoice')
    bitpayInvoicePerms = Permission.objects.filter(content_type=bitpayInvoiceCT)
    bitpayInvoicePermView = bitpayInvoicePerms[3]
    admin.permissions.add(bitpayInvoicePermView)

    # CATEGORY
    categoryCT = ContentType.objects.get(app_label='podverse_db', model='category')
    categoryPerms = Permission.objects.filter(content_type=categoryCT)
    categoryPermView = categoryPerms[3]
    admin.permissions.add(categoryPermView)

    # EPISODE
    episodeCT = ContentType.objects.get(model='episode')
    episodePerms = Permission.objects.filter(content_type=episodeCT)
    episodePermChange = episodePerms[1]
    episodePermDelete = episodePerms[2]
    episodePermView = episodePerms[3]
    admin.permissions.add(episodePermChange)
    admin.permissions.add(episodePermDelete)
    admin.permissions.add(episodePermView)
    curator.permissions.add(episodePermChange)
    curator.permissions.add(episodePermDelete)
    curator.permissions.add(episodePermView)

    # FEEDURL
    feedUrlCT = ContentType.objects.get(model='feedurl')
    feedUrlPerms = Permission.objects.filter(content_type=feedUrlCT)
    feedUrlPermAdd = feedUrlPerms[0]
    feedUrlPermChange = feedUrlPerms[1]
    feedUrlPermDelete = feedUrlPerms[2]
    feedUrlPermView = feedUrlPerms[3]
    admin.permissions.add(feedUrlPermAdd)
    admin.permissions.add(feedUrlPermChange)
    admin.permissions.add(feedUrlPermDelete)
    admin.permissions.add(feedUrlPermView)
    curator.permissions.add(feedUrlPermAdd)
    curator.permissions.add(feedUrlPermChange)
    curator.permissions.add(feedUrlPermDelete)
    curator.permissions.add(feedUrlPermView)

    # GOOGLEPLAYPURCHASE
    googlePlayPurchaseCT = ContentType.objects.get(app_label='podverse_db', model='googleplaypurchase')
    googlePlayPurchasePerms = Permission.objects.filter(content_type=googlePlayPurchaseCT)
    googlePlayPurchasePermView = googlePlayPurchasePerms[3]
    admin.permissions.add(googlePlayPurchasePermView)

    # MEDIAREF
    mediaRefCT = ContentType.objects.get(model='mediaref')
    mediaRefPerms = Permission.objects.filter(content_type=mediaRefCT)
    mediaRefPermChange = mediaRefPerms[1]
    mediaRefPermDelete = mediaRefPerms[2]
    mediaRefPermView = mediaRefPerms[3]
    admin.permissions.add(mediaRefPermChange)
    admin.permissions.add(mediaRefPermDelete)
    admin.permissions.add(mediaRefPermView)

    # PAYPALORDER
    paypalOrderCT = ContentType.objects.get(model='paypalorder')
    paypalOrderPerms = Permission.objects.filter(content_type=paypalOrderCT)
    paypalOrderPermView = paypalOrderPerms[3]
    admin.permissions.add(paypalOrderPermView)

    # PLAYLIST
    playlistCT = ContentType.objects.get(model='playlist')
    playlistPerms = Permission.objects.filter(content_type=playlistCT)
    playlistPermChange = playlistPerms[1]
    playlistPermDelete = playlistPerms[2]
    playlistPermView = playlistPerms[3]
    admin.permissions.add(playlistPermChange)
    admin.permissions.add(playlistPermDelete)
    admin.permissions.add(playlistPermView)

    # PODCAST
    podcastCT = ContentType.objects.get(model='podcast')
    podcastPerms = Permission.objects.filter(content_type=podcastCT)
    podcastPermChange = podcastPerms[1]
    podcastPermDelete = podcastPerms[2]
    podcastPermView = podcastPerms[3]
    admin.permissions.add(podcastPermChange)
    admin.permissions.add(podcastPermDelete)
    admin.permissions.add(podcastPermView)
    curator.permissions.add(podcastPermChange)
    curator.permissions.add(podcastPermDelete)
    curator.permissions.add(podcastPermView)

    # USER
    userCT = ContentType.objects.get(app_label="podverse_db", model='user')
    userPerms = Permission.objects.filter(content_type=userCT)
    userPermAdd = userPerms[0]
    userPermChange = userPerms[1]
    userPermDelete = userPerms[2]
    userPermView = userPerms[3]
    admin.permissions.add(userPermAdd)
    admin.permissions.add(userPermChange)
    admin.permissions.add(userPermDelete)
    admin.permissions.add(userPermView)

    # DJANGO GROUP
    djangoGroupCT = ContentType.objects.get(app_label="auth", model='group')
    djangoGroupPerms = Permission.objects.filter(content_type=djangoGroupCT)
    for perm in djangoGroupPerms:
        admin.permissions.add(perm)

    # DJANGO USER
    djangoUserCT = ContentType.objects.get(app_label="auth", model='user')
    djangoUserPerms = Permission.objects.filter(content_type=djangoUserCT)
    for perm in djangoUserPerms:
        admin.permissions.add(perm)

    # DJANGO LOGS
    djangoLogCT = ContentType.objects.get_for_model(LogEntry)
    djangoLogPerms = Permission.objects.filter(content_type=djangoLogCT)
    djangoLogPermView = djangoLogPerms[3]
    admin.permissions.add(djangoLogPermView)

    def handle(self, *args, **options):
        self.stdout.write("Permissions and groups created.")
