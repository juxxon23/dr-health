from db.postgresql.postgresql_manager import PostgresqlManager
from db.cloudant.cloudant_manager import CloudantManager
from db.postgresql.model import Patient, Doctor, Family
from db.postgresql.model import Medicalrecord, Appointment
from db.postgresql.model import Order, Authorization, Result

postgres_manager = PostgresqlManager()
cloud_manager = CloudantManager()


class DBP:
    def sync(self, my_db):
        try:
            # Sincronizacion de la tabla patient
            patient_temp = postgres_manager.get_all(Patient)
            if patient_temp != []:
                for patient in patient_temp:
                    patient_nosql = {
                        'id_u': patient.id_p,
                        'name': patient.name_p,
                        'last': patient.last_p, 
                        'mail': patient.mail_p,
                        'password': patient.password_p,
                        'phone': patient.phone,
                        'age': patient.age,
                        'id_family': patient.id_family,
                        'role': patient.role_p,
                        'id_m': patient.id_m
                    }
                    msg = cloud_manager.add_doc(my_db, patient_nosql)
                    patient_del = postgres_manager.delete(patient)

            # Sincronizacion de la tabla doctor
            doctor_temp = postgres_manager.get_all(Doctor)
            if doctor_temp != []:
                for doctor in doctor_temp:
                    doctor_nosql = {
                        'id_u': doctor.id_d,
                        'name': doctor.name_d,
                        'last': doctor.last_d,
                        'mail': doctor.mail_d,
                        'password': doctor.password_d,
                        'specialty': doctor.specialty,
                        'phone': doctor.phone,
                        'role': doctor.role_d
                    }
                    msg = cloud_manager.add_doc(my_db, doctor_nosql)
                    doctor_del = postgres_manager.delete(doctor)

            # Sincronizacion de la tabla family
            family_temp = postgres_manager.get_all(Family)
            if family_temp != []:
                for family in family_temp:
                    family_nosql = {
                        'id_f': family.id_f,
                        'id_d': family.id_d,
                    }
                    msg = cloud_manager.add_doc(my_db, family_nosql)
                    family_del = postgres_manager.delete(family)

            # Sincronizacion de la tabla medicalrecord
            record_temp = postgres_manager.get_all(Medicalrecord)
            if record_temp != []:
                for record in record_temp:
                    record_nosql = {
                        'id_m': record.id_m,
                        'pathologies': record.pathologies,
                    }
                    msg = cloud_manager.add_doc(my_db, record_nosql)
                    record_del = postgres_manager.delete(record)
            return 'ok'
        except:
            return 'error'
