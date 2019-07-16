# Aditya Mookerjee - Dualing Web App
## aditya.mookerjee@gmail.com
### Mon 15 July
https://adi-rh.herokuapp.com/

**Process** : 
1. User uploads a .CSV file (see example `applicants.csv`)
2. App randomly selects two `applicants` to ***battle***
3. App renders some output, including two tabs : a 1v1 battle, a bonus ***melee*** battle with all combinations

The application is built in Python using the Dash Library.

When developing the application it is recommended to use a virtualenv, wherein the app's dependencies must be reinstalled.
```python
$ virtualenv venv
$ source venv/bin/activate
```

## To Install Requirements
```python
$ pip install -r requirements.txt
```



## To Run the Application
```python
$ python app.py
```
**Note** This command will launch a local Flask server, which is recommended **only** for development purposes. Please see the section on running the application in a production environment
Running the command above in the terminal will result in the following output :
> python app.py
> * Serving Flask app "streaming-app" (lazy loading)
>  * Environment: production
>    WARNING: Do not use the development server in a production environment.
>    Use a production WSGI server instead.
>  * Debug mode: on
>  * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
>  * Restarting with stat
>  * Debugger is active!
>  * Debugger PIN: 157-549-508

Note that the Debugger is active on Default, so modifying the code structure will automatically restart the flask server


## Running the Application in Production
The Hive Streaming App is designed to run with , a UNIX WSGI HTTP Server
```python
$ pip install gunicorn
```

Upon installing this dependency, a WSGI HTTP Server can be started by :
```python
$ gunicorn app:app --bind 0.0.0.0:8080
```
