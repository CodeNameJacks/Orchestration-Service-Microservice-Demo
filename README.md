# Orchestration Microservice Demo Project

This is a Python program built with the Flask framework to demonstrate and test microservices architecture and the design of a scalable microservice system.

Note that you can clone the project files by running `git clone https://github.com/CodeNameJacks/Orchestrate.git` in the command line.

To set up and run locally:
1. In the terminal command line use the command `mkdir <name of folder>` to create the following three folders in your project directory: `user`, `subscription`, `preference` and `orchestrationService`.
Perform steps 2 - 6 in each folder.
2. Install Python 3.x
3. Create a virtual Python environment in the folder by entering `python3 -m venv venv`
4. To activate the virtual environment run `. venv/bin/activate` Now that virtual Python environment is running, install the following:
5. Run the `requirements.txt` file to install the dependencies. Should the dependencies fail to laod you can enter them manually be entering `pip install flask python-dotenv requests` in the command line.
6. Also install the mySQL connector by running `pip install mysql-connector-python` in the command line.
7. You need to create a file called .flaskenv in each folder. Place this in the root directory. In that file, place the following on their own line: `FLASK_APP=<name of the api.py for each folder>`,  `FLASK_DEBUG=1`, and `FLASK_RUN_PORT=<port number for the service>`.
8. In the root directory create a file called `.env`. Place your non-Flask environment variables in this file.
9. In the terminal command line `cd` to each folder one by one and run the command `flask run`. Your servers should now be running on their respective ports.

You can test each server to ensure it is running by opening a web browser and entering `localhost:<port number>/api/test` in the url. You should get the following response `<Name of service> service is working and backend is running` for the respective service.

System documentation is contianed in the `Documentation.pdf` file.
