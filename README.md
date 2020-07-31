# Super Tracks [![CodeFactor](https://www.codefactor.io/repository/github/kardoso/supertracks/badge)](https://www.codefactor.io/repository/github/kardoso/supertracks) [![](https://img.shields.io/badge/Python-3.8.2-blue.svg)](https://www.python.org/downloads/release/python-382/) [![](https://img.shields.io/badge/Django-3.0.8-green)](https://www.djangoproject.com/) [![](https://img.shields.io/github/license/kardoso/SuperTracks.svg)](https://github.com/kardoso/SuperTracks/blob/master/LICENSE)

Super Tracks is a small and simple web application that lists music tracks from a database, showing the following columns:
- Track Name
- Artist Name
- Album Title

## Running the application
To run this application it's recommended that you use a virtual environment, so you'll have a controlled environment just for this application.
If you don`t want to use a virtual environment skip steps 2 and 3.

1. Install [Python](https://www.python.org/downloads/) if you don't have it yet. <br> For this project I used the version 3.8.2 as you can see in the badges, but you can pick a newer one.

2. As soon as you have python installed run in the terminal the following command(which will create a virtual environment named "venv" in the current directory, you can change the directory if you want): <br> `python3 -m virtualvenv venv` <br> If an error is shown, you'll need to install virtualenv using pip and try it again right after it. Use this command to install virtualenv: `pip install virtualenv` <br> Now, you`re ready to continue.

3. After it you will have a new virtual environment and can execute the command `source venv/bin/activate`(linux/mac) or `venv\Scripts\activate`(windows) to start using it.

4. Now with the active virtual environment go to this project folder and execute `pip install requirements.txt` from your terminal. This will make sure you get all the requirements for this project installed in your virtual environment.

5. Now you just need to run the application. Use the command `python manage.py runserver` and the app will be available at `http://127.0.0.1:8000` or simply at `localhost:8000`. You can access it from the browser now.