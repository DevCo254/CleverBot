import hashlib
import os
import sys
from rauth import OAuth2Service

if sys.version_info[0] == 3:
    raw_input = input

client_id = raw_input('Enter your App Id:' )
secret = raw_input('enter your app secret: ')

service = OAuth2Service(
    client_id=client_id,
    client_secret=secret,
    name='wakatime',
    authorize_url='https://wakatime.com/oauth/authorize',
    access_token_url='https://wakatime.comoauth/token',
    base_url='https://wakatime.com/api/v1'
)

redirect_uri ='https://wakatime.com/oauth/test'
state = hashlib.sha1(os.urandom(40)).hexdigest()
params = {'scope':'email,read_stats',
        'response_type':'code',
        'state': state,
        'redirect_uri':redirect_uri}

url = service.get_authorize_url(**params)

