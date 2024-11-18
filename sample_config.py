HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["8089776460:AAHzk9V4OKGOPaEGxyCZsH1MvdisZC7KPBc"]
    ARQ_API_KEY = environ["APTEZH-DQCRLD-AYNFYQ-OSWJPP-ARQ"]
    LANGUAGE = environ["tr"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
    ARQ_API_KEY = "Get this from @ARQRobot"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
