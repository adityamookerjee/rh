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

# Background
-------------------------
Details:
-------------------------
Being... well... programmers, the applicants weapon of choice is the slap. Each applicant must engage in a one on one match with each other applicant.

A match consists of one or more rounds where two applicants square off in a fight until one applicant gets slapped so hard by another applicant that he or she literally can't walk. This is serious business.

In each round, the applicants alternate slapping each other until both candidates have exhausted the number of attacks they are permitted, or a candidate's health reaches or drops below 0. You may randomly choose who attacks first in each round, or if you're feeling spicy, you can implement an initiative system using the initiative data supplied in the import file.
-------------------------
Requirements:
-------------------------
The application must import this applicant spreadsheet (https://www.dropbox.com/s/cchi1qx6z5u92fi/applicants.csv), which contains the vitals for each applicant. Each applicant must then fight against all the other applicants. The applicant with the highest winning percentage after all the matches are completed gets the job!
-------------------------
Example match:
-------------------------
Candidate 1:
Health: 46
Damage: 3
Attacks: 5

Candidate 2:
Health: 52
Damage: 8
Attacks: 2

Round 1:
Candidate 1 is randomly selected to go first (43 > 40)  <-- initiative roll
Candidate 1 hits candidate 2 for 3 damage (52 -> 49)    <-- Damage applied (health before damage -> health after damage)
Candidate 2 hits candidate 1 for 8 damage (46 -> 38)
Candidate 1 hits candidate 2 for 3 damage (49 -> 46)
Candidate 2 hits candidate 1 for 8 damage (38 -> 30)
Candidate 1 hits candidate 2 for 3 damage (46 -> 43)
Candidate 1 hits candidate 2 for 3 damage (43 -> 40)
Candidate 1 hits candidate 2 for 3 damage (40 -> 37)
Round 2:
Candidate 1 is randomly selected to go first (26 > 11)
Candidate 1 hits candidate 2 for 3 damage (37 -> 34)
Candidate 2 hits candidate 1 for 8 damage (30 -> 22)
Candidate 1 hits candidate 2 for 3 damage (34 -> 31)
Candidate 2 hits candidate 1 for 8 damage (22 -> 14)
Candidate 1 hits candidate 2 for 3 damage (31 -> 28)
Candidate 1 hits candidate 2 for 3 damage (28 -> 25)
Candidate 1 hits candidate 2 for 3 damage (25 -> 22)
Round 3:
Candidate 2 is randomly selected to go first (35 > 29)
Candidate 2 hits candidate 1 for 8 damage (14 -> 6)
Candidate 1 hits candidate 2 for 3 damage (22 -> 19)
Candidate 2 hits candidate 1 for 8 damage (6 -> -2)
Candidate 2 wins!
-------------------------
Additional info:
-------------------------
Try to keep application output clear and readable, but concise. Using the above output format would work fine, though feel free to provide what you feel is best.

In regards to program design, you have complete control. This challenge was designed to get a feel for your problem solving ability and creativity.
-------------------------
Vitals:
-------------------------
Name - Applicant name
Health - Starting health
Damage - Damage that each slap inflicts
Attacks - Number of attacks per round
I've also included some additional columns in the spreadsheet that you can incorporate if you have extra time:

Dodge - Percentage chance to dodge
Critical - Percentage chance to inflict critical damage (x2)
Initiative - Added to random roll for deciding who goes first each round
