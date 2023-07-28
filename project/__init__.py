# project/__init__.py



#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
##################################################
### Flask App Configuration and Initialization ###
##################################################

# Create a Flask web application instance
app = Flask(__name__)

# Load configuration settings from "_config.py" file
app.config.from_pyfile("_config.py")

# Create a Bcrypt instance and initialize it with the app
bcrypt = Bcrypt(app)

# Create a SQLAlchemy database instance and initialize it with the app
db = SQLAlchemy(app)
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
##############################
### Blueprint Registration ###
##############################
# Import "helloword_bp" blueprint from the "helloworld" module
from project.helloworld.views import helloworld_bp

# Register the "helloword_bp" blueprint with the app
app.register_blueprint(helloworld_bp)
#------------------------------------------------------------------------------------------------
