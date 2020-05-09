from flask import Flask

if __name__ == '__main__':
    from templates import app
    #Load this config object for development mode
    app.config.from_object('configs.DevelopmentConfig')
    app.run()