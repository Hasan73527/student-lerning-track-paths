from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'hasan735278@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Hasan@123'  
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)  
  
#configure the Message class object and send the mail from a URL  
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'hasan735278@gmail.com', recipients=['hasan73527@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    mail.send(msg)
    return "Mail Sent, Please check the mail id"  
  
if __name__ == '__main__':  
    app.run(debug = True)