from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DonationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donation'

    def ready(self):
        import donation.signals