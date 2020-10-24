"""
    Modified from: https://gist.github.com/c00kiemon5ter/7806c1eac8c6a3e82f061ec32a55c702
"""
import logging

from django.contrib.auth.management.commands import createsuperuser
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import CommandError
from django.db.utils import IntegrityError

from accounts.models import Organization

logger = logging.getLogger(name="CREATE_SUPERUSER_COMMAND")


class Command(createsuperuser.Command):
    help = "Create a superuser with a password non-interactively"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument(
            "--password",
            dest="password",
            default=None,
            help="Specifies the password for the superuser.",
        )
        parser.add_argument(
            "--organization",
            dest="organization",
            default=None,
            help="Specifies the abbreviation for parent company.",
        )

    def handle(self, *args, **options):
        options.setdefault("interactive", False)
        database = options.get("database")
        password = options.get("password")
        username = options.get("username")
        email = options.get("email")
        organizaion_abbr = options.get("organization")

        if not password or not username or not email or not organizaion_abbr:
            raise CommandError(
                "--email --username, --organization and --password are required options"
            )
        try:
            organization = Organization.objects.get(abbr=organizaion_abbr)
        except ObjectDoesNotExist:
            logger.error(
                "Sorry, that organization does not exist. Ensure you create the organization first by running: 'python manage.py create_organization'"
            )
        else:
            user_data = {
                "username": username,
                "password": password,
                "email": email,
                "organization_id": organization.id,
            }
            try:
                self.UserModel._default_manager.db_manager(database).create_superuser(
                    **user_data
                )

                if options.get("verbosity", 0) >= 1:
                    self.stdout.write("Superuser created successfully.")
            except IntegrityError:
                logger.error("User already exists with those details")
            except Exception as err:
                logger.exception(err)
