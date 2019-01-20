from server.controller.contributor import bp

def configure_blueprints(app):
    app.register_blueprint(bp)
