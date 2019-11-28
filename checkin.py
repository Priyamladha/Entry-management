import requests
from datetime import datetime
from app import db,User,Host
import smtplib
from email.message import EmailMessage




def send(name1,email1,number1):
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M %p")
        checkin1=current_time +" IST"

        # enter user in database
        user1 = User(name=name1,email=email1,number=number1,checkin=checkin1)
        db.session.add(user1)
        db.session.commit()
        message = "Visitor Details\n"+"Name -"+name1+"\nEmail - "+email1+"\nNumber - "+number1
        host = Host.query.first()
        host_number = host.number
        host_email = host.email
        user1.hostname=host.name
        db.session.commit()
        #sending sms using Fast2sms
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {"authorization":"KMviuAdxhlzpT2tPYXse16QV9n7JWUr5Rm4oBgCkf0LSHajGZ8r3ZIXj96dqFlvLUAneVcMWJgCYtSwh","sender_id":"FSTSMS","message":message,"language":"english","route":"p","numbers":host_number}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        #sending mail via gmail
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()
        sender_id ="xyzcompany20@gmail.com"
        msg = EmailMessage()
        msg['Subject'] = 'Visitor Details'
        msg['From'] = sender_id
        msg['To'] = host_email
        # msg.set_content(message)
        html_message=open('templates/html_email_host.html').read().format(name=name1,email=email1,number=number1)
        msg.add_alternative(html_message, subtype='html')
        s.login(sender_id,"qKHcnWwBEkL8g96")
        s.send_message(msg)
        s.quit()
        return -1
    except:
        try:
            host = Host.query.first()
            host_number = host.number
            return 1
        except:
            return 2

