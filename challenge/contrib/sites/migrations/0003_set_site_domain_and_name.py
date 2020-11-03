"""
Credit for this addition to a project set up is to Daniel Feldroy (pydanny).
We place and reference this migration so that our domain and site name is set as part of our build or deploy process.

"""
from django.conf import settings
from django.db import migrations

# change these to fit your needs
DOMAIN = 'example.com'
NAME = 'example.com'


def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': DOMAIN,
            'name': NAME,
        },
    )


def update_site_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=settings.SITE_ID, defaults={'domain': DOMAIN, 'name': NAME}
    )


class Migration(migrations.Migration):
    dependencies = [('sites', '0002_alter_domain_unique')]

    operations = [migrations.RunPython(update_site_forward, update_site_backward)]
