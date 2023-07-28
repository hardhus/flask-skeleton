# db_create.py



# This script creates all the database tables defined in the models.
#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################

from project import db, app
from models import User
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
### Database Creation ###
# Create the database tables based on the defined models
with app.app_context():
    db.create_all()
#------------------------------------------------------------------------------------------------
