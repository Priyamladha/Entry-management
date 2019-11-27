from app import db
from app import Host

def create(name1,email1,number1):
    try:
        host1=Host.query.first()
        host_number=host1.number
        Host.query.filter_by(number=host_number).delete()
        db.session.commit()
    except:
        pass
    host1 = Host(name=name1,email=email1,number=number1)
    db.session.add(host1)
    db.session.commit()


