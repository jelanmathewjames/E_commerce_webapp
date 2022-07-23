from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email,phone_number, password=None,is_active=True, is_superuser=False,
                    is_staff=False,**extra_fields):
        if phone_number != None and email != None:
           checker_number = int(phone_number) 
           checker_email = self.normalize_email(email)
        elif phone_number != None:
           checker_number = int(phone_number) 
           checker_email = None
        elif email != None: 
           checker_number = None
           checker_email = self.normalize_email(email)
        else:
            raise ValueError("User Name field cannot be empty")
        user = self.model(
                email = checker_email,
                phone_number = checker_number,
                is_active = is_active,
                is_superuser = is_superuser,
                is_staff = is_staff,
                **extra_fields
                ) 
        user.set_password(password)
        user.save(using=self._db)     
        return user   
    def create_superuser(self,email,phone_number,password=None,is_active=True, is_superuser=True,
                    is_staff=True,**extra_fields):
        user = self.create_user(
            email,
            phone_number,
            password,
            is_active = is_active,
            is_superuser = is_superuser,
            is_staff = is_staff,
            **extra_fields
        )
        user.save(using=self._db)
        return user