from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Doctor(db.Model):
    __tablename__ = "Doctor"

    id_d = db.Column(db.String(20), primary_key=True, nullable=False)
    name_d = db.Column(db.String(40), nullable=False)
    last_d = db.Column(db.String(40), nullable=False)
    mail_d = db.Column(db.String(50), nullable=False)
    password_d = db.Column(db.String(128), nullable=False)
    specialty = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    role_d = db.Column(db.String(2), nullable=False)
    family_group = db.relationship(
        'Family', backref='group', lazy='dynamic', foreign_keys='Family.id_d')
    appointment_assigned_doctor = db.relationship(
        'Appointment', backref='app_assi_doc', lazy='dynamic', foreign_keys='Appointment.id_d')

    def __init__(self, id_d, name_d, last_d, mail_d, password_d, specialty, phone, role_d):
        self.id_d = id_d
        self.name_d = name_d
        self.last_d = last_d
        self.mail_d = mail_d
        self.password_d = password_d
        self.specialty = specialty
        self.phone = phone
        self.role_d = role_d


class Patient(db.Model):
    __tablename__ = "Patient"

    id_p = db.Column(db.String(20), primary_key=True, nullable=False)
    name_p = db.Column(db.String(40), nullable=False)
    last_p = db.Column(db.String(40), nullable=False)
    mail_p = db.Column(db.String(50), nullable=False)
    password_p = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(12))
    age = db.Column(db.Integer, nullable=False)
    id_family = db.Column(db.String(10), db.ForeignKey('Family.id_f'))
    role_p = db.Column(db.String(2), nullable=False)
    id_m = db.Column(db.String(10), db.ForeignKey('Medicalrecord.id_m'))
    appointment_assigned_patient = db.relationship(
        'Appointment', backref='app_assi_pat', lazy='dynamic', foreign_keys='Appointment.id_p')

    def __init__(self, id_p, name_p, last_p, mail_p, password_p, phone, age, id_family, role_p, id_m):
        self.id_p = id_p
        self.name_p = name_p
        self.last_p = last_p
        self.mail_p = mail_p
        self.password_p = password_p
        self.phone = phone
        self.age = age
        self.id_family = id_family
        self.role_p = role_p
        self.id_m = id_m


class Family(db.Model):
    __tablename__ = "Family"

    id_f = db.Column(db.String(10), primary_key=True, nullable=False)
    id_d = db.Column(db.String(20), db.ForeignKey('Doctor.id_d'), nullable=True)
    patient_member = db.relationship('Patient', backref='member', lazy='dynamic', foreign_keys='Patient.id_family')

    def __init__(self, id_f, id_d):
        self.id_f = id_f
        self.id_d = id_d


class Medicalrecord(db.Model):
    __tablename__ = "Medicalrecord"

    id_m = db.Column(db.String(10), primary_key=True, nullable=False)
    pathologies = db.Column(db.String(250))
    patient_record = db.relationship('Patient', backref='owner_record', lazy='dynamic', foreign_keys='Patient.id_m')

    def __init__(self, id_m, pathologies):
        self.id_m = id_m
        self.pathologies = pathologies


class Appointment(db.Model):
    __tablename__ = "Appointment"

    id_a = db.Column(db.String(10), primary_key=True, nullable=False)
    id_p = db.Column(db.String(20), db.ForeignKey('Patient.id_p'))
    id_d = db.Column(db.String(20), db.ForeignKey('Doctor.id_d'))
    date_a = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(250), nullable=False)
    order_a = db.relationship(
        'Order', backref='app_order', lazy='dynamic', foreign_keys='Order.id_a')

    def __init__(self, id_a, id_p, id_d, date_a, reason):
        self.id_a = id_a
        self.id_p = id_p
        self.id_d = id_d
        self.date_a = date_a
        self.reason = reason


class Order(db.Model):
    __tablename__ = "Order"

    id_o = db.Column(db.String(10), primary_key=True, nullable=False)
    id_a = db.Column(db.String(10), db.ForeignKey('Appointment.id_a'))
    diagnosis = db.Column(db.String(250), nullable=False)
    auth = db.relationship(
        'Authorization', backref='auth_order', lazy='dynamic', foreign_keys='Authorization.id_o')
    result = db.relationship(
        'Result', backref='result_order', lazy='dynamic', foreign_keys='Result.id_o')

    def __init__(self, id_o, id_a, diagnosis):
        self.id_o = id_o
        self.id_a = id_a
        self.diagnosis = diagnosis


class Authorization(db.Model):
    __tablename__ = "Authorization"

    id_auth = db.Column(db.String(10), primary_key=True, nullable=False)
    id_o = db.Column(db.String(10), db.ForeignKey('Order.id_o'))
    file_a = db.Column(db.LargeBinary)

    def __init__(self, id_auth, id_o, file_a):
        self.id_auth = id_auth
        self.id_o = id_o
        self.file_a = file_a


class Result(db.Model):
    __tablename__ = "Result"

    id_r = db.Column(db.String(10), primary_key=True, nullable=False)
    id_o = db.Column(db.String(10), db.ForeignKey('Order.id_o'))
    file_r = db.Column(db.LargeBinary)
    
    def __init__(self, id_r, id_o, file_r):
        self.id_r = id_r
        self.id_o = id_o
        self.file_r = file_r
