from flask import Flask, request, redirect
import twilio.twiml
import requests
import settings
import pprint
from bing import bing_search
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    msg = request.values.get('Body', None)
    resp = twilio.twiml.Response()
    if not msg:
        resp.message("You didn't seem to send a message. Try again?")
        return str(resp)
    else:
        query_result = bing_search(msg)[0]['Description']
        resp.message(query_result)
        return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)