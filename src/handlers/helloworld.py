from flask import render_template#, request, redirect

def get_helloworld(app):
    @app.route('/', methods=["GET"])
    def helloworld():
        return render_template("helloworld.html")

    @app.route('/api/welcomemessage', methods=["GET"])
    def welcomemessage():
        
        return render_template("helloworld.html")

