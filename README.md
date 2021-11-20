## TOR SERVER
### For startup the app:
1. Install [python 3.9.1+](https://www.python.org/downloads/)
2. Install pipenv (shell command):
    * `pip install pipenv`
3. Install requirements (shell command):
    * `pipenv install`
4. Generate crypto key and token:
   * `pipenv run python src/utils/util.py generate_crypto_key` - generate `CRYPTO_KEY`
   * `pipenv run python src/utils/util.py generate_crypto_token` - generate auth token
     *(Your inserted `secret password` should be pasted in env)*
5. Set env variables:
   * Open file `.env`
   * Set env parameters like the same in `env_example`
     *(some parameters were generated at past step)*
6. Run the app (shell command):
   * Important! You should be at `src` directory
   * `pipenv run uvicorn main:app --port <CHOSE_YOUR_PORT>`  
7. Stop the app press:
    * `Ctrl + C`

### For using app:
Load site-page `http://127.0.0.1:<CHOSE_YOUR_PORT>/dosc`

### For using web-app:
Load site-page `http://127.0.0.1:<CHOSE_YOUR_PORT>/`

### For using app under tor-network:
Use this [instruction](https://github.com/satwikkansal/tor-hidden-service-python)
