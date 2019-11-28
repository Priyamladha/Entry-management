import requests
from datetime import datetime
from app import db,User,Host
import smtplib
from email.message import EmailMessage

def send(name1,email1,number1):
    now = datetime.now()
    current_time = now.strftime("%H:%M %p")
    checkout1=current_time +" IST"
    try:
        user = User.query.filter_by(number=number1).first()
        user.checkout=checkout1
        db.session.commit()
        checkin1=user.checkin
        hostname1=user.hostname
        User.query.filter_by(number=number1).delete()
        db.session.commit()


        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()
        sender_id ="xyzcompany20@gmail.com"
        msg = EmailMessage()
        msg['Subject'] = 'Visitor Details'
        msg['From'] = sender_id
        msg['To'] = user.email
        # msg.set_content(message)
        html_message=open('templates/html_email_user.html').read().format(name=name1,number=number1,checkin=checkin1,checkout=checkout1,hostname=hostname1,address="2nd and 9th Floor, Tower 3, Candor Techspace, Rajat Vihar, Block B, Industrial Area, Sector 62, Noida, Uttar Pradesh 201309")
        msg.add_alternative(html_message, subtype='html')
        s.login(sender_id,"qKHcnWwBEkL8g96")
        s.send_message(msg)
        s.quit()
        return -1
    except:
        return 1  
