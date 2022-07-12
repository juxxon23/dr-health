from flask.views import MethodView
from flask import request, jsonify
from db.cloudant.cloudant_manager import CloudantManager
from validators.appointment_val import AppointmentVal

cm = CloudantManager()
appointment_schema = AppointmentVal()


class Appointment(MethodView):
    def get(self):
        try:
            id_u = request.args.get('idu')
            print(id_u)
            cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            user_docs = cm.get_query_by(my_db, id_u, 'id_p')
            print(user_docs)
            list_appointments = []
            for result in user_docs:
                try:
                    appointment_id = result['doc']['id_a']
                    id_u = result['doc']['id_p']
                    new_appointment = {
                        'id_a': appointment_id,
                        'id_d': result['doc']['id_d'],
                        'id_p': id_u,
                        'date_a': result['doc']['date_a'],
                        'reason': result['doc']['reason']
                    }
                    print(new_appointment)
                    list_appointments.append(new_appointment)
                except:
                    pass
            return jsonify({'appointments': list_appointments}), 200
        except:
            return jsonify({'st': "error"}), 403

    def post(self):
        try:
            appointment = request.get_json()
            errors = appointment_schema.validate(appointment)
            if errors:
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, appointment)
            if doc_msg == "ok":
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == "error":
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403
        except:
            return jsonify({'st': "bad"}), 403
