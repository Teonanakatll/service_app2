from celery_app import app as celery_app

# для того чтобы celery запустился с джанго приложением
__all__ = ('celery_app',)