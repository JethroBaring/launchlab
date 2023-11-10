from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, user_type, password=None, **other_fields):
        """Creates and returns a new User."""
        user = self._create_user(email, password, **other_fields)

        user.user_type = user_type

        user.save(using=self._db)

        return user

    def _create_user(self, email, password, **other_fields):
        user = self.model(email=email, **other_fields)
        user.set_password(password)

        return user
