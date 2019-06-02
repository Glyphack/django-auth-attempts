from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, email, password=None):
        user = self.model(
            phone_number=phone_number,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password):
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)
