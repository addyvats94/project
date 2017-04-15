from django.conf import settings

from rest_framework import status
import oauth2_provider.models as oauth_models

from django.contrib.auth import authenticate, login, logout

from HostelActivities import models

import requests
import json


def login_user(request):
    auth = (settings.OAUTH_CLIENT_ID, settings.OAUTH_CLIENT_SECRET)
    username = request.data['username']
    password = request.data['password']
    try:
        user_object = models.User.objects.get(email=username.lower())
    except models.User.DoesNotExist:
        print('user does not exist')
        return
    # import pdb
    # pdb.set_trace()   
    # response = requests.post(settings.BACKEND_HOST+ '/o/token/',
                             # data={'username': user_object.email, 'password': password, 'grant_type': 'password'},
                             # auth=auth)
    # if response.status_code == status.HTTP_200_OK:
    # result = json.loads(response.text)
    user = authenticate(username=username, password=password)
    if user.is_active:
        login(request, user)
        
    return {"status": True, "message": {"access_token":'',
                                        'first_name': user_object.firstname, 'last_name': user_object.lastname,
                                        'email': user_object.email,
                                        'mobile': user_object.mobile_no}}


def logout_user(request):
    """
        Logs out the user
        Params: access_token to be rendered invalid
    """

    data = {}
    
    data['client_id'] = settings.OAUTH_CLIENT_ID
    data['client_secret'] = settings.OAUTH_CLIENT_SECRET
    data['token'] = request.META["HTTP_AUTHORIZATION"].split("Bearer ")[1]
    resp = requests.post(settings.BACKEND_HOST + '/o/revoke_token/', data=data)
    return resp.status_code == status.HTTP_200_OK
