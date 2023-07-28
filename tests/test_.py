# test/test_.py



#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################

import os
import unittest
from project import app, db, bcrypt
from project._config import basedir
from models import Model
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
#########################
### burayı sen doldur ###
#########################

TEST_DB = "test.db"
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
#########################
### burayı sen doldur ###
#########################

class UserTests(unittest.TestCase):
    
    ##########################
    ### setup and teardown ###
    ##########################
    
    
    # executed prior to each test
    def setUp(self):
        
        # configure the test database for the app
        app.config["TESTING"] = True
        app.config["CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
            os.path.join(basedir, TEST_DB)
        
        # start the flask app in test mode
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        # create the test database and create the tables
        with self.app_context:
            db.create_all()
            print(db.engine.url)
        
        self.assertEqual(app.debug, False)
    
    def tearDown(self):
        # remove the database connection
        db.session.remove()
        # drop all the tables from the datbase
        db.drop_all()

        # pop the flask app context
        #self.app_context.pop()
    
    
    ######################
    ### helper methods ###
    ######################
    
    def helper(self):
        pass
    
    #############
    ### tests ###
    #############
    
    def test_example(self):
        # Burada bir test senaryosu oluşturuyoruz
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
#########################
### burayı sen doldur ###
#########################

if __name__ == "__main__":
    unittest.main()
#------------------------------------------------------------------------------------------------