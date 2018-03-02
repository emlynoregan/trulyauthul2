import firebase_admin
from firebase_admin import credentials, auth

def initFirebaseApp():
    retval = None
    try:
        # just see if the app's already initialised
        retval = firebase_admin.get_app()
    except:
        # nope. Let's initialise it
        cred = credentials.Certificate('config/firebasekey.json')
        retval = firebase_admin.initialize_app(cred)
    return retval
        
def decodeFirebaseToken(accesstoken):
    initFirebaseApp()
    return auth.verify_id_token(accesstoken)