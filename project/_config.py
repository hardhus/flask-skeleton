# project/_config.py



#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################
import os
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
#################################
### Application Configuration ###
#################################

# grab the folder where this scripts lives
basedir = os.path.abspath(os.path.dirname(__file__))

# Database file for the application
DATABASE = "database.db"

# Enable Cross-Site Request Forgery protection
CSRF_ENABLED = True

# Secret key used for secure sessions and cryptographic functions
SECRET_KEY = "secret"

# Enable debugging mode for the application
DEBUG = True

# define the full path for the datebase
DATABASE_PATH = os.path.join(basedir, DATABASE)

# define the database uri
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH
#------------------------------------------------------------------------------------------------