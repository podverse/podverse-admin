from podverse_db.models import Author, Category, Episode, FeedUrl, MediaRef, Podcast, User

class PodverseDBRouter(object):

    def db_for_read(self, model, **hints):
        if model == Author or model == Category or model == Episode or model == FeedUrl or model == MediaRef or model == Podcast or model == User:
            return 'podverse_db'
        return None

    def db_for_write(self, model, **hints):
        if model == Author or model == Category or model == Episode or model == FeedUrl or model == MediaRef or model == Podcast or model == User:
            return 'podverse_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Migrations to podverse_db should never be handled by Django
        if db == 'podverse_db':
            return False
        return None
