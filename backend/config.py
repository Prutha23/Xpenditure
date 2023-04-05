from main import app
from flask_jwt_extended import JWTManager


# jwt config
app.config["APPLICATION_TITLE"] = "Xpenditure"
app.config["DEBUG"] = "Xpenditure_Debug"
app.config["SECRET_KEY"] = "xpenditure_secret_key"
app.config["JWT_TOKEN_LOCATION"] = "headers"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 60*60*24
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 60*60*24*7
app.config["JWT_ALGORITHM"] = "HS256"

jwt = JWTManager(app)


# CORS config
@app.after_request
def after_request(response):
    """
    Post request processing - add CORS, cache control headers
    """
    # Enable CORS requests for local development
    # The following will allow the local angular-cli development environment to
    # make requests to this server (otherwise, you will get 403s due to same-origin poly)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Set-Cookie,'
                                                         'Cookie,Cache-Control,Pragma,Expires')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')

    # disable caching all requests
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    return response
