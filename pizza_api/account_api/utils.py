import datetime,jwt
from django.conf import settings
from rest_framework import exceptions

def create_token(user_id):
    payload = dict(
        id = user_id,
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat = datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    print('------------------------------------------------------')
    print(token)
    return token

def get_payload(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        return payload
    except:
        raise exceptions.AuthenticationFailed("Invalid Credentials")


