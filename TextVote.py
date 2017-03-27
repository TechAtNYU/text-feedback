#
# TextVote.py
# Cole Smith
# Receives votes from a number and exports a results JSON file
#

import json
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
votes = dict()

@app.route("/", methods=['GET', 'POST'])
def handle_text():
    '''
    Runs whenever a message triggers this web hook. Will update a
    dictionary with the current count of responses that match that
    message string. Will update a JSON text file with the results
    indefinitely.
    :return: An HTTP response echo that is REQUIRED by Twilio
    '''
    resp = twilio.twiml.Response()
    number = request.form['From']
    message_body = request.form['Body']

    # Add Vote to the votes dictionary
    vote = str(message_body).lower()
    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1

    # Write to JSON File
    with open('results.txt', 'wb') as f:
        json.dump(votes, f)

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
