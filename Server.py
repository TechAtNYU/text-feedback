#
# Server.py
# Cole Smith
# Receives votes from a number and exports a results JSON file
#

import json
import sys

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

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
    number = request.form['From']
    message_body = request.form['Body']
    resp = MessagingResponse()
    vote = str(message_body)

    print "Starting Server with output file name: " + event_name

    # Add Vote to the votes dictionary
    if vote.isdigit() and 1 <= int(vote) <= 5:
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1

    # Write to JSON File
    file_name = str(event_name) + ".txt"
    with open(file_name, 'w') as f:
        json.dump(votes, f)

    return str(resp)


event_name = str(sys.argv[0])
app.run(debug=True)
