FROM python:3.12.3
WORKDIR /project

COPY requirements.txt requirements.txt 
RUN pip3 install virtualenv

RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8001

CMD python3 manage.py runserver

# FROM python:3.12.3

# Set the working directory
# WORKDIR /project

# Copy the current directory contents into the container at /app
# COPY . /app

# Install any necessary dependencies specified in requirements.txt
# RUN pip3 install -r requirements.txt

# Set environment variables (optional)

# Command to run the application
# CMD python3 manage.py runserver
