# Orchestrate

This is a Python program built with the Flask framework to demonstrate and test microservices architecture and the design of a scalable microservice system.

Note that you can clone the project files by running `git clone hhttps://github.com/CodeNameJacks/Orchestrate.git` in the command line.

To set up and run locally:
1. Create the following three folders in your project directory and name them user, subscription and preference.
Perform steps 2 - 6 in each folder.
2. Install Python 3.x
3. Create a virtual Python environment in the backend folder by entering `python3 -m venv venv`
4. To activate the virtual environment run `. venv/bin/activate` Now that virtual Python environment is running, install the following:
5. Run the `requirements.txt` file to install the dependencies. Should the dependencies fail to laod you can enter them manually be entering `pip install flask python-dotenv requests` in the command line.
6. Also install the mySQL connector by running `pip install mysql-connector-python` in the command line.
7. You need to create a file called .flaskenv. Place this in the root directory. In that file, place the following on their own line: `FLASK_APP=api.py` and `FLASK_DEBUG=1`.
