from django.core.management import BaseCommand

from users_app.models import User


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.SUCCESS("Users creation start!"))
        for item in range(30):
            data = {
                "email": f"email{item}@i.ua",
                "first_name": f"first_name{item}",
                "last_name": f"last_name{item}",
                "role": "client"
            }
            password = f"Password{item}!"
            user = User.objects.create(**data)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"{item} user created!"))
        self.stdout.write(self.style.SUCCESS("Done!"))
