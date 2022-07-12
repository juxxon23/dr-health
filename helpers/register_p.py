"""from controllers.signin import Signin
from db.cloudant.cloudant_manager import CloudantManager
from helpers.crypt import Crypt
from flask import  jsonify
cm = CloudantManager()
crypt = Crypt()

class RegisterPatient:
    def register_patient(self, patient_signin, my_db):
        docs = cm.get_query_by(my_db, patient_signin['email'], 'email')
        if docs != []:
            doc = docs[0]
            if patient_signin['email'] == doc['doc']['email']:
                return "exists"
        return "void"

        patient_signin['password_p'] = crypt.hash_string(patient_signin['password_p'])
        doc_msg = cm.add_doc(my_db, patient_signin)
        disconnect = cm.disconnect_db('health_db') 
        if doc_msg == "ok":
            return jsonify({'st': 'ok'}), 200
        elif doc_msg == "error":
            return jsonify({'st': 'error'}), 403
"""