from django.conf import settings


VERSION = (0, 1, 0)
__version__ = '.'.join(map(str, VERSION))


class Router:
    @staticmethod
    def db_for_read(model, **_hints):
        return getattr(settings, 'DATABASE_FOR_APPS', {}).get(model._meta.app_label, getattr(settings, 'DATABASE_FOR_APPS', {}).get('*', 'default'))

    @staticmethod
    def db_for_write(model, **_hints):
        return getattr(settings, 'DATABASE_FOR_APPS', {}).get(model._meta.app_label, getattr(settings, 'DATABASE_FOR_APPS', {}).get('*', 'default'))

    @staticmethod
    def allow_relation(_obj1, _obj2, **_hints):
        return getattr(settings, 'DATABASE_FOR_APPS_RELATIONS', None)

    @staticmethod
    def allow_migrate(db, app_label, _model=None, **_hints):
        db_app_label = getattr(settings, 'DATABASE_FOR_APPS', {}).get(app_label)

        if db_app_label:
            return db == getattr(settings, 'DATABASE_FOR_APPS', {}).get(app_label)

        return db == getattr(settings, 'DATABASE_FOR_APPS', {}).get('*', 'default')
