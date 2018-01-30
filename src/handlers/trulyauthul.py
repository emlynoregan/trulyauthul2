from flask import render_template#, request, redirect

def get_trulyauthul(app):
    @app.route('/', methods=["GET", "POST"])
    def trulyauthul():
        return render_template("trulyauthul.html")
