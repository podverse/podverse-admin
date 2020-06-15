# Generated by Django 2.1.5 on 2020-06-15 22:37

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import podverse_db.models.feedUrl
import podverse_db.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountClaimToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('claimed', models.BooleanField(default=False)),
                ('yearsToAdd', models.PositiveIntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AccountClaimToken',
                'verbose_name_plural': 'AccountClaimTokens',
                'db_table': 'accountClaimToken',
            },
        ),
        migrations.CreateModel(
            name='AppStorePurchase',
            fields=[
                ('transactionId', models.CharField(max_length=2084, primary_key=True, serialize=False)),
                ('cancellation_date', models.CharField(blank=True, max_length=2084)),
                ('cancellation_date_ms', models.CharField(blank=True, max_length=2084)),
                ('cancellation_date_pst', models.CharField(blank=True, max_length=2084)),
                ('cancellation_reason', models.CharField(blank=True, max_length=2084)),
                ('expires_date', models.CharField(blank=True, max_length=2084)),
                ('expires_date_ms', models.CharField(blank=True, max_length=2084)),
                ('expires_date_pst', models.CharField(blank=True, max_length=2084)),
                ('is_in_intro_offer_period', models.BooleanField(blank=True)),
                ('is_trial_period', models.BooleanField(blank=True)),
                ('original_purchase_date', models.CharField(blank=True, max_length=2084)),
                ('original_purchase_date_ms', models.CharField(blank=True, max_length=2084)),
                ('original_purchase_date_pst', models.CharField(blank=True, max_length=2084)),
                ('original_transaction_id', models.CharField(blank=True, max_length=2084)),
                ('product_id', models.CharField(blank=True, max_length=2084)),
                ('promotional_offer_id', models.CharField(blank=True, max_length=2084)),
                ('purchase_date', models.CharField(blank=True, max_length=2084)),
                ('purchase_date_ms', models.CharField(blank=True, max_length=2084)),
                ('purchase_date_pst', models.CharField(blank=True, max_length=2084)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('transaction_id', models.CharField(blank=True, max_length=2084)),
                ('web_order_line_item_id', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AppStorePurchase',
                'verbose_name_plural': 'AppStorePurchases',
                'db_table': 'appStorePurchase',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2084, unique=True)),
                ('slug', models.CharField(max_length=2084, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='BitPayInvoice',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('orderId', models.CharField(max_length=2084, unique=True)),
                ('amountPaid', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=2084)),
                ('exceptionStatus', models.CharField(default='false', max_length=2084)),
                ('price', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=2084)),
                ('transactionCurrency', models.CharField(blank=True, max_length=2084)),
                ('transactionSpeed', models.CharField(blank=True, max_length=2084)),
                ('url', models.URLField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'BitPayInvoice',
                'verbose_name_plural': 'BitPayInvoices',
                'db_table': 'bitpayInvoices',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('fullPath', models.CharField(max_length=2084, unique=True)),
                ('slug', models.CharField(max_length=2084)),
                ('title', models.CharField(max_length=2084, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, db_column='categoryId', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_category', to='podverse_db.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('episodeType', models.CharField(blank=True, max_length=2084)),
                ('guid', models.CharField(blank=True, max_length=2084)),
                ('imageUrl', models.URLField(blank=True)),
                ('isExplicit', models.BooleanField(default=False)),
                ('isPublic', models.BooleanField(default=False)),
                ('linkUrl', models.URLField(blank=True)),
                ('mediaFilesize', models.PositiveIntegerField(default=0)),
                ('mediaType', models.CharField(blank=True, max_length=2084)),
                ('mediaUrl', models.URLField(unique=True)),
                ('pastHourTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')),
                ('pastDayTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')),
                ('pastWeekTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')),
                ('pastMonthTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')),
                ('pastYearTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')),
                ('pastAllTimeTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')),
                ('pubDate', models.DateTimeField(blank=True)),
                ('title', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'episodes',
            },
        ),
        migrations.CreateModel(
            name='FeedUrl',
            fields=[
                ('id', models.CharField(default=podverse_db.models.feedUrl.FeedUrl.shortid, max_length=14, primary_key=True, serialize=False)),
                ('isAuthority', models.BooleanField(default=True)),
                ('url', models.URLField(unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FeedUrl',
                'verbose_name_plural': 'FeedUrls',
                'db_table': 'feedUrls',
            },
        ),
        migrations.CreateModel(
            name='GooglePlayPurchase',
            fields=[
                ('transactionId', models.CharField(max_length=2084, primary_key=True, serialize=False)),
                ('acknowledgementState', models.IntegerField(blank=True)),
                ('consumptionState', models.IntegerField(blank=True)),
                ('developerPayload', models.CharField(blank=True, max_length=2084)),
                ('kind', models.CharField(blank=True, max_length=2084)),
                ('productId', models.CharField(max_length=2084)),
                ('purchaseTimeMillis', models.CharField(blank=True, max_length=2084)),
                ('purchaseState', models.IntegerField(blank=True)),
                ('purchaseToken', models.CharField(max_length=2084, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'GooglePlayPurchase',
                'verbose_name_plural': 'GooglePlayPurchases',
                'db_table': 'googlePlayPurchase',
            },
        ),
        migrations.CreateModel(
            name='MediaRef',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('endTime', models.PositiveIntegerField(blank=True, default=0)),
                ('isPublic', models.BooleanField(default=False)),
                ('pastHourTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')),
                ('pastDayTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')),
                ('pastWeekTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')),
                ('pastMonthTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')),
                ('pastYearTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')),
                ('pastAllTimeTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')),
                ('startTime', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('episode', models.ForeignKey(db_column='episodeId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.Episode')),
            ],
            options={
                'verbose_name': 'MediaRef',
                'verbose_name_plural': 'MediaRefs',
                'db_table': 'mediaRefs',
            },
        ),
        migrations.CreateModel(
            name='PayPalOrder',
            fields=[
                ('paymentID', models.CharField(max_length=2084, primary_key=True, serialize=False)),
                ('state', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'PayPalOrder',
                'verbose_name_plural': 'PayPalOrders',
                'db_table': 'paypalOrders',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=2084)),
                ('isPublic', models.BooleanField(default=False)),
                ('itemCount', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'playlists',
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('alwaysFullyParse', models.BooleanField(default=False)),
                ('authorityId', models.CharField(blank=True, max_length=2084)),
                ('description', models.TextField(blank=True)),
                ('feedLastUpdated', models.DateTimeField(blank=True)),
                ('guid', models.CharField(blank=True, max_length=2084)),
                ('hideDynamicAdsWarning', models.BooleanField(default=False)),
                ('imageUrl', models.URLField(blank=True, max_length=2084)),
                ('isExplicit', models.BooleanField(default=False)),
                ('isPublic', models.BooleanField(default=False)),
                ('language', models.CharField(blank=True, max_length=2084)),
                ('lastEpisodePubDate', models.DateTimeField(blank=True)),
                ('lastEpisodeTitle', models.CharField(blank=True, max_length=2084)),
                ('linkUrl', models.URLField(blank=True, max_length=2084)),
                ('pastHourTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')),
                ('pastDayTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')),
                ('pastWeekTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')),
                ('pastMonthTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')),
                ('pastYearTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')),
                ('pastAllTimeTotalUniquePageviews', models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')),
                ('shrunkImageUrl', models.URLField(blank=True, max_length=2084)),
                ('sortableTitle', models.CharField(blank=True, max_length=2084)),
                ('title', models.CharField(blank=True, max_length=2084)),
                ('type', models.CharField(blank=True, max_length=2084)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'podcasts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=podverse_db.models.user.User.shortid, max_length=14, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('emailVerified', models.BooleanField()),
                ('freeTrialExpiration', models.DateTimeField(blank=True)),
                ('isPublic', models.BooleanField(default=False)),
                ('membershipExpiration', models.DateTimeField(blank=True)),
                ('name', models.CharField(blank=True, max_length=2084)),
                ('password', models.CharField(max_length=2084)),
                ('roles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2084), blank=True, default=list, size=20)),
                ('historyItems', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list)),
                ('queueItems', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='owner',
            field=models.ForeignKey(db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
        migrations.AddField(
            model_name='paypalorder',
            name='owner',
            field=models.ForeignKey(db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
        migrations.AddField(
            model_name='mediaref',
            name='owner',
            field=models.ForeignKey(blank=True, db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
        migrations.AddField(
            model_name='googleplaypurchase',
            name='owner',
            field=models.ForeignKey(db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
        migrations.AddField(
            model_name='feedurl',
            name='podcast',
            field=models.ForeignKey(blank=True, db_column='podcastId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.Podcast'),
        ),
        migrations.AddField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(db_column='podcastId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.Podcast'),
        ),
        migrations.AddField(
            model_name='bitpayinvoice',
            name='owner',
            field=models.ForeignKey(db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
        migrations.AddField(
            model_name='appstorepurchase',
            name='owner',
            field=models.ForeignKey(db_column='ownerId', on_delete=django.db.models.deletion.CASCADE, to='podverse_db.User'),
        ),
    ]
