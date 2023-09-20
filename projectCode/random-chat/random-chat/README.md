# random-chat
Chat with random people

This app uses `Flask-SocketIO` to serve realtime messages from one to second.

Maximum limit for data transfer using socket is set to 13500000.

## Run the application

set the `SECRET_KEY` and `DATABASE_URI` as environment variable for application use

### Install requirements
```shell
$ python -m pip install -r requirements.txt
```

### Run the app
```shell
$ flask run
```
**or**
```shell
python wsgi.py
```
