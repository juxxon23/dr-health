from db.postgresql.postgresql_manager import PostgresqlManager
from db.cloudant.cloudant_manager import CloudantManager
from db.postgresql.model import Patient, Doctor, Family
from db.postgresql.model import Medicalrecord, Appointment
from db.postgresql.model import Order, Authorization, Result

postgres_manager = PostgresqlManager()
cloud_manager = CloudantManager()


class DBP:
    def sync(self, my_db, cm):
        try:
            # Sincronizacion de la tabla patient
            patient_temp = postgres_manager.get_all(Patient)
            if patient_temp != []:
                for patient in patient_temp:
                    patient_nosql = {
                        'id_p': patient.id_p,
                        'name_p': patient.name_p,
                        'mail_p': patient.mail_p,
                        'password_p': patient.password_p,
                        'phone': patient.phone,
                        'age': patient.age,
                        'id_family': patient.id_family,
                        'role_p': '2'
                    }
                    msg = cloud_manager.add_doc(my_db, patient_nosql)
                    patient_del = postgres_manager.delete(patient)

            # Sincronizacion de la tabla doctor
            doctor_temp = postgres_manager.get_all(Doctor)
            if doctor_temp != []:
                for doctor in doctor_temp:
                    doctor_nosql = {
                        'id_d': doctor.id_d,
                        'name_d': doctor.name_d,
                        'mail_d': doctor.mail_d,
                        'password_d': doctor.password_d,
                        'specialty': doctor.specialty,
                        'phone': doctor.phone,
                        'role_d': '1'
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

            # Sincronizacion de la tabla appointment
            appointment_temp = postgres_manager.get_all(Appointment)
            if appointment_temp != []:
                for appointment in appointment_temp:
                    appointment_nosql = {
                        'id_a': appointment.id_a,
                        'id_p': appointment.id_p,
                        'id_d': appointment.id_d,
                        'date_a': appointment.date_a,
                        'reason': appointment.reason
                    }
                    msg = cloud_manager.add_doc(my_db, appointment_nosql)
                    appointment_del = postgres_manager.delete(appointment)

            # Sincronizacion de la tabla order
            order_temp = postgres_manager.get_all(Order)
            if order_temp != []:
                for order in order_temp:
                    order_nosql = {
                        'id_o': order.id_o,
                        'id_a': order.id_a,
                        'diagnosis': order.diagnosis
                    }
                    msg = cloud_manager.add_doc(my_db, order_nosql)
                    order_del = postgres_manager.delete(order)

            # Sincronizacion de la tabla authorization
            authorization_temp = postgres_manager.get_all(Authorization)
            if authorization_temp != []:
                for authorization in authorization_temp:
                    authorization_nosql = {
                        'id_auth': authorization.id_r,
                        'id_o': authorization.id_o,
                        'file_a': authorization.file_a
                    }
                    msg = cloud_manager.add_doc(my_db, authorization_nosql)
                    authorization_del = postgres_manager.delete(authorization)

            # Sincronizacion de la tabla result
            result_temp = postgres_manager.get_all(Result)
            if result_temp != []:
                for result in result_temp:
                    result_nosql = {
                        'id_r': result.id_r,
                        'id_o': result.id_o,
                        'file_r': result.file_r
                    }
                    msg = cloud_manager.add_doc(my_db, result_nosql)
                    result_del = postgres_manager.delete(result)
            return 'ok'
        except:
            return 'error'
