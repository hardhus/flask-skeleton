# run_test.py



#------------------------------------------------------------------------------------------------
####################################
### Import the necessary modules ###
####################################

import os
import webbrowser
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------
######################
### Running Tests  ###
######################

if __name__ == "__main__":
    # Command to run tests with coverage and generate HTML report
    command = "nosetests --with-coverage --cover-erase --cover-html --cover-package=project"
    
    # Execute the command to run tests with coverage and generate HTML report
    os.system(command)

    command = "pip freeze"
    os.system(command)
    
    # Path to the generated coverage HTML report
    cover_report_path = "file:///C:/Users/cumon/Desktop/Web%20Projects/flask-skeleton/cover/index.html"
    
    # Open the coverage report in the default web browser
    webbrowser.open(cover_report_path)
#------------------------------------------------------------------------------------------------
