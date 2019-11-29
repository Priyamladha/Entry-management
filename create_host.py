from app import db
from app import Host

def create(name1,email1,number1):
    host1 = Host(name=name1,email=email1,number=number1)
    db.session.add(host1)
    db.session.commit()


