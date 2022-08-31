## Python Version
FROM python:3.7
## Copy all the files into app folder
COPY . /app
## Setting working directory
WORKDIR /app
## installing requirements
RUN pip install -r requirements.txt
## Open the port (Run time variable)
EXPOSE $PORT
## Run gunicorn app= (Flask app name)
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app