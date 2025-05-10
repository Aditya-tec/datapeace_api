import json
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Import users from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the users.json file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

                for item in data:
                    if not User.objects.filter(id=item['id']).exists():
                        User.objects.create(
                            id=item['id'],
                            first_name=item['first_name'],
                            last_name=item['last_name'],
                            company_name=item['company_name'],
                            city=item['city'],
                            state=item['state'],
                            zip=item['zip'],
                            email=item['email'],
                            web=item['web'],
                            age=item['age']
                        )
                self.stdout.write(self.style.SUCCESS('Users imported successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
