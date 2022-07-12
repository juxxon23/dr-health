from flask import request, jsonify
from flask.views import MethodView
from db.cloudant.cloudant_manager import CloudantManager
from validators.result_val import ResultVal

cm = CloudantManager()
result_schema = ResultVal()

class Result(MethodView):
    def get(self):
        try:
            # Conexion a Cloudant
            id_u = request.args.get('idu')
            cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            # Falta agregar sincronizacion de las db
            user_result = cm.get_query_by(my_db, id_u, 'id_p')
            list_results = []
            for result in user_result:
                try:
                    appointment_id = result['doc']['id_a']
                    orders = cm.get_query_by(my_db, appointment_id, 'id_a')
                    for order in orders:
                        try:
                            order_id = order['doc']['id_o']
                            results = cm.get_query_by(my_db, order_id, 'id_o')
                            for result_u in results:
                                try:
                                    result_id = result_u['doc']['id_r']
                                    new_result = {
                                        'id_r': result_id,
                                        'id_o': result_u['doc']['id_o'],
                                        'file_r': result_u['doc']['file_r']
                                    }
                                    list_results.append(new_result)
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            return jsonify({'st': 'ok', "results": list_results}), 200
        except:
            return jsonify({'st': 'error'}), 403

    def post(self):
        try:
            result_user = request.get_json()
            errors = result_schema.validate(result_user)
            if errors:
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, result_user)
            if doc_msg == 'ok':
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == 'error':
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403
        except:
            return jsonify({'st': 'bad'}), 403
