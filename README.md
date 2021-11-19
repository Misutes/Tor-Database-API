## TOR SERVER
### For startup the app:
1. Install [python 3.9.1+](https://www.python.org/downloads/)
2. Install pipenv (shell command):
    * `pip install pipenv`
3. Install requirements (shell command):
    * `pipenv install`
4. Set env variables:
    * Open file `.env`
    * Set DATABASE_PATH (at the end should be '\\')
    * Set DATABASE_NAME
5. Run the app (shell command):
* Important! You should be at `src` directory
    * `pipenv run uvicorn main:app --port <CHOSE_YOUR_PORT>`
6. Stop the app press:
   * `Ctrl + C`

### For using app:
Load site-page `http://127.0.0.1:<CHOSE_YOUR_PORT>/dosc`

### For using app under tor-network:
Use this [instruction](https://github.com/satwikkansal/tor-hidden-service-python)
