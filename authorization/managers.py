from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password, role=3):
        user = self.model(username=username)
        user.set_password(password)
        user.role = role
        user.save(using=self._db)

        return user

    def create_salesman(self, username, password):
        user = self.create_user(username, password, role=2)
        is_staff = True

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password, role=1)
        is_staff = True
        is_superuser = True
        user.save(using=self._db)
        return user


