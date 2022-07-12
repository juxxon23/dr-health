from flask import request, jsonify
from flask.views import MethodView
from db.cloudant.cloudant_manager import CloudantManager
from validators.order_val import OrderVal

cm = CloudantManager()
order_schema = OrderVal()

class Order(MethodView):
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
            list_orders = []
            for result in user_result:
                try:
                    appointment_id = result['doc']['id_a']
                    orders = cm.get_query_by(my_db, appointment_id, 'id_a')
                    for order in orders:
                        try:
                            order_id = order['doc']['id_o']
                            new_order = {
                                'id_o': order_id,
                                'id_a': appointment_id,
                                'diagnosis': order['doc']['diagnosis']
                            }
                            list_orders.append(new_order)
                        except:
                            pass
                except:
                    pass
            return jsonify({'st': 'ok', "orders": list_orders}), 200
        except:
            return jsonify({'st': 'error'}), 403

    def post(self):
        try:
            order = request.get_json()
            errors = order_schema.validate(order)
            if errors:
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, order)
            if doc_msg == 'ok':
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == 'error':
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403
        except:
            return jsonify({'st': 'bad'}), 403
