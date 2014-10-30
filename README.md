DUMBPHONIA

A Flask-and-Twilio-backed question-and-answer-ish app that lets you do Bing
queries via SMS.

WHY?

I have a dumbphone, and sometimes I want to know things that would be trivially
Google-able with a smartphone (e.g., "What's the definition of this word I just
read?", "What's that video game with the exploding penguins?", etc)

ChaCha (https://en.wikipedia.org/wiki/ChaCha_(search_engine)) was pretty decent
for this, but they shut down :(

SETUP

- Sign up for access to the Bing search API
(https://datamarket.azure.com/dataset/bing/search). As of this writing, 5,000
requests per month is free. As part of the sign up process, you should get a
Microsoft Azure Marketplace account key. Set BING_DEVELOPER_KEY in settings.py
to this value.

- Deploy the code in this repo to Heroku. A nifty guide:
https://devcenter.heroku.com/articles/getting-started-with-python-o

- Once your app is running on Heroku, sign up for a Twilio account and get a
number if you don't already have one.

- Go to "Manage Numbers" on your Twilio dashboard and paste your Heroku app URL
into the spot for a messaging request URL.

- Try texting a search query to your Twilio number. Have fun!

EXTRA STUFF THAT WOULD BE FUN TO ADD SOMETIME MAYBE

- the Mechanical Turk API is hideously overcomplicated for this, but it would
replicate ChaCha much more nicely
- maybe optionally use the DuckDuckGo Instant Answers API?