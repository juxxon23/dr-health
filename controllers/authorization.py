from flask import request, jsonify
from flask.views import MethodView
from db.cloudant.cloudant_manager import CloudantManager
from validators.authorization_val import AuthorizationVal

cm = CloudantManager()
authorization_schema = AuthorizationVal()

class Authorization(MethodView):
    def get(self):
        try:
            id_u = request.args.get('idu')
            # Conexion a Cloudant
            cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            # Falta agregar sincronizacion de las db
            # Ajustarlo para el paciente
            user_result = cm.get_query_by(
                my_db, id_u, 'id_p')
            list_auth = []
            for result in user_result:
                try:
                    appointment_id = result['doc']['id_a']
                    orders = cm.get_query_by(
                        my_db, appointment_id, 'id_a')
                    for order in orders:
                        try:
                            order_id = order['doc']['id_o']
                            authorizations = cm.get_query_by(
                                my_db, order_id, 'id_o')
                            for auth in authorizations:
                                try:
                                    authorization_doc = auth['doc']['id_auth']
                                    new_auth = {
                                        'id_auth': authorization_doc,
                                        'id_o': order_id,
                                        'file_a': auth['doc']['file_a']}
                                    list_auth.append(new_auth)
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            return jsonify({'st': 'ok', "authorizations": list_auth}), 200
        except:
            return jsonify({'st': 'error'}), 403

    def post(self):
        try:
            authorization = request.get_json()
            errors = authorization_schema.validate(authorization)
            if errors:
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, authorization)
            if doc_msg == 'ok':
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == 'error':
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403
        except:
            return jsonify({'st': 'bad'}), 403  
