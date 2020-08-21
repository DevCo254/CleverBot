from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Messagingresponse
from cleverwrap import cleverwrap



app = Flask(__name__)

cleverbot_API = CleverWrap("Insert Your API key")

@app.route("/sms",methods=['GET','POST'])
def sms_reply():
    message_body=request.form['body']
    cleverbot_response = cleverbot_API.say(message_body)

    resp = Messagingresponse()
    resp.message(cleverbot_response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)