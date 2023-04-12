from flask import Flask

# creating flask app
app = Flask(__name__)

# load jwt and cors config
from config import *  # noqa

# load and/or register apis
from utils.error_handler import *  # noqa
from apis.login import *  # noqa
from apis.expense import *  # noqa
from apis.category import *  # noqa
from apis.user import *  # noqa
from apis.reminder import *  # noqa


if __name__ == "__main__":
    app.run(debug=True)
