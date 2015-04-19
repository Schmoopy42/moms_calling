from flask import Flask, request, redirect, render_template, url_for
import twilio.twiml
import os
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

mp3_dir = '/home/jerry/Documents/my_tutorial_folder/mp3_files'
 
'''
@app.route('/files')
def index():
    mp3_files = [f for f in os.listdir(mp3_dir) if f.endswith('mp3')]
    mp3_files_number = len(mp3_files)
    return render_template("index.html",
         title = 'files',
         mp3_files_number = mp3_files_number,
         mp3_files = mp3_files) 
'''

@app.route("/make_call")
def make_call():
    account_sid = 'AC4822ec321e60caaf56588d0de0cc108e'
    auth_token = 'a140c252d652aac5c19618ecbb4cd2be'
    client = TwilioRestClient(account_sid, auth_token)
 
    # Make the call
    call = client.calls.create(to="+18623240282",  # Any phone number
        from_="+18622032900", # Must be a valid Twilio number
        url="http://104.131.248.123/files/weasel.mp3")
    print call.sid
    return 'success'

'''
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"
 
    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an MP3
    resp.play("posixpath(/home/jerry/Documents/my_tutorial_folder/mp3_files/weasel.mp3)")
 
    return str(resp)
 '''

if __name__ == "__main__":
    app.run(debug=True)
