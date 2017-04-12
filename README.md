# Text Vote
## Python Script to build voting results from text messages

### Dependencies
#### It's recommended to use a virtual environment

#### Install with `pip`
`twilio`

`flask`

#### Set the environment variables

`INTRANET_URL`

`INTRANET_TOKEN`

### Running
Run the script normally with `python TextVote.py`

In a separate terminal, download and install `ngrok` to
expose the python server to the web.

`brew cask install ngrok`

Then run `ngrok`

`ngrok http 5000`

Enter the forwarding URL from `ngrok` as a web hook URL for
you Twilio number as defined [here](https://www.twilio.com/blog/2016/09/how-to-receive-and-respond-to-a-text-message-with-python-flask-and-twilio.html)

