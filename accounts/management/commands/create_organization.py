import logging

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from accounts.models import Organization

logger = logging.getLogger(name="CREATE_ORG_COMMAND")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        name = input("Enter name of organization: ")
        abbr = input("Enter organization's abbreviation: ")
        industry = input("Enter organizations industry: ")
        registered_country = input(
            "Where is it registered? Enter country code (ISO 3166-1 alpha-2): "
        )

        try:
            Organization.objects.create(
                name=name,
                abbr=abbr,
                industry=industry,
                registered_country=registered_country,
            )
            logger.info("Organization created successfully.")
        except IntegrityError:
            logger.error("Sorry! That company already exists.")
        except Exception as err:
            logger.exception(err)
