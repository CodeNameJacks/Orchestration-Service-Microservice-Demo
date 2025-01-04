#userService Dockerfile
FROM python:3.11

#Set the working directory
WORKDIR /app

#create the dependencies file
COPY requirements.txt /app/

#Copying all the application source code and files to the working directory `app`
COPY . .

#Install Python dependencies
RUN pip install -- no-cache-dir -r requirements.txt

#Expose the port that the app rns on
EXPOSE 5006

#Run the application
CMD ["python", "orchestrationService.py"]