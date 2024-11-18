HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "BACLJYM5S2ZFx8gr3GeIxuhXsausRAQF7T8A92P1xORgZB5T4CLXBTqKXbWhAlk2TYwwplWkQhDiLTJISz_1QXUyBCGIew5N9dnuBIg2SccVTa0J29JkyHDKJRNxgQMZPOJvqttZk2cYGFA-V5DgsWBzILCKU3MWON7-BeCNiSzd5LzP_SjnNvQKdJtuKP2bHAj9XpSjz3ZLzR5t0Mf4iJJT-0k0IcRks5fvsv7nc1rM6mhHae81TN_s0P4yDBCOmLEamRLxheqxaKj0SCNmLf0_3uAqo1ImwJvYm1zZB-QHwKYrMzGqi7QmvwJnkpGP9uHZBZppd5boqadQfvP0hjRCAAAAAb2qOzMA"
    ARQ_API_KEY = "EZH-DQCRLD-AYNFYQ-OSWJPP-ARQ
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "tr"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
