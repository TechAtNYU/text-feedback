#
# TextVote.py
# Cole Smith
# Receives votes from a number and exports a results JSON file
#

import datetime
import time
from subprocess import Popen

import os
import requests

event_name = None


def name_for_event_now(url, auth_token):
    '''
    Accesses Intranet API to get a JSON object of
    upcoming events
    :param url: Intranet URL
    :param auth_token: Intranet Auth Token
    :return: Name of Event found or None
    '''
    name = None
    url += '/events/upcoming?include=addedBy'
    auth = "Bearer " + auth_token
    req = requests.get(url, headers={"Authorization": auth})
    try:
        data = req.json()
        for key in data["data"]:
            att = key["attributes"]
            start = ""
            end = ""
            title = ""
            if "title" in att:
                title = att["title"]
            if "startDateTime" in att:
                start = att["startDateTime"]
            if "endDateTime" in att:
                end = att["endDateTime"]

            # Check if time intersects now
            start_date = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
            end_date = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")

            if start_date < datetime.datetime.utcnow() < end_date:
                # Event is now
                name = title

    except ValueError:
        print "[ ERR ] Error in grabbing events from Intranet"

    return name


def event_watch_loop():
    proc = None
    while True:
        event_name = name_for_event_now(str(os.environ["INTRANET_URL"]), str(os.environ["INTRANET_TOKEN"]))
        event_name = "test"
        if event_name is not None and proc is None:
            print "starting server"
            proc = Popen(['python', 'Server.py', str(event_name)])
        else:
            if proc is not None and proc.pid is not None:
                print "stopping server"
                proc.terminate()
        time.sleep(60)

if __name__ == '__main__':
    event_watch_loop()
