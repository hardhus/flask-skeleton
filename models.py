# models.py



#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################

from project import db
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
##########################
### Models Definitions ###
##########################

class Model(db.Model):
    """Model class for the 'table' database table.

    Args:
        db (SQLAlchemy): The SQLAlchemy database instance.

    Returns:
        Model: A Model object representing a row in the 'table' table.

    Attributes:
        __tablename__ (str): The name of the database table associated with this model.
        column1 (db.Column): Primary key column of type Integer.
        column2 (db.Column): String column with a maximum length of 255 characters.
        column3 (db.Column): String column with a maximum length of 255 characters, defaulting to an empty string.

    Methods:
        __init__(self, column2_value, column3_value=""): Constructor to initialize the Model object.
        __repr__(self): Returns a string representation of the Model object.
    """
    __tablename__ = "table"

    # Define columns for the table
    column1 = db.Column(db.Integer, primary_key=True)
    column2 = db.Column(db.String(255), nullable=False)
    column3 = db.Column(db.String(255), nullable=False, default="")
    
    def __init__(self, column2_value, column3_value=""):
        self.column2 = column2_value
        self.column3 = column3_value

    def __repr__(self):
        return f"<Model(column1={self.column1}, column2='{self.column2}', column3='{self.column3}')>"

    # Define any additional methods or properties for the model here
    # ...

# If you have more models, you can define them below
# class AnotherModel(db.Model):
#     ...
#------------------------------------------------------------------------------------------------