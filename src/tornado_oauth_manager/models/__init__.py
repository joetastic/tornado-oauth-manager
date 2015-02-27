class User(object):
    pass


class Client(object):
    client_id = None
    grant_type = None
    response_type = None
    scopes = None
    redirect_uris = None


class BearerToken(object):
    '''
    client=None
    use=None
    Scopes=None
    access_token=None
    refresh_token=None
    expiration_time=None
    '''


class AuthorizationCode(object):
    client_id = None
    user = None
    scopes = None
    authorization_code = None
    expiration_time = None
