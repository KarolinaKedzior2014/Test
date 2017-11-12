from django.contrib.auth.models import User


class MissingValuesException(Exception):
    def __init__(self, array):
        self.missing_values = array

    def __str__(self):
        return ', '.join(self.missing_values)


def check_registration_data(data):
    required_params = [
        'login',
        'password',
        'email',
        'first_name',
        'last_name'
    ]
    missing_params = []
    for param in required_params:
        if param not in data:
            missing_params.append(param)

    if len(missing_params) > 0:
        raise MissingValuesException(missing_params)


def create_user(data):
    check_registration_data(data)
    user = User.objects.create_user(data['login'], data['email'], data['password'])
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.save()
    return user
