from flask import render_template, request
from firebaseutils import decodeFirebaseToken
import json
import logging

def get_trulyauthul(app):
    @app.route('/', methods=["GET"])
    def trulyauthul():
        return render_template("trulyauthul.html")

    @app.route('/api/welcomemessage', methods=["GET"])
    def welcomemessage():
        # get the access token if there is one
        accessToken = request.headers.get("accesstoken")
        logging.debug("accessToken: %s" % accessToken)

        # now decode the access token if possible
        decodedToken = None
        if accessToken:
            decodedToken = decodeFirebaseToken(accessToken)
        logging.debug(
            "decodedToken: %s" % json.dumps(decodedToken, indent=2)
        )

        # lastly, construct and return the welcome message 
        if decodedToken:
            name = decodedToken.get("name", "<can't get name>")
            lresponse = "Hi %s, welcome to Truly Authul" % name
        else:
            lresponse = "Hello there! Please sign in to access Truly Authul"
            
        return json.dumps(
            {
                "message": lresponse
            }, 
            indent=2
        )
            