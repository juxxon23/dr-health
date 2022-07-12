from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result


class CloudantManager():
    # Autenticacion
    client = Cloudant.iam("d6179485-8359-47c6-9067-337120997531-bluemix",
                          "2_9ItqbvPPIMPM7meDDr4nbB1ND-vvZ4dXMT8z8oGH1_")

    # Conexion al servicio
    def connect_service(self):
        try:
            CloudantManager.client.connect()
            return "ok"
        except:
            return "error"

    # Crear base de datos Cloudant
    def create_db(self, db_name):
        try:
            my_db = CloudantManager.client.create_database(
                db_name, throw_on_exit=True)
            return my_db
        except CloudantException as ex:
            return ex

    # Conectar una base de datos existente
    def connect_db(self, db_name):
        try:
            my_db = CloudantManager.client[db_name]
            return my_db
        except:
            return "error"

    # desconectar servicio
    def disconnect(self, db_name):
        try:
            CloudantManager.client.disconnect()
            return "ok"
        except:
            return "error"

    # Eliminar una base de datos Cloudant
    def  delete_db(self, db_name):
        try:
            CloudantManager.client.delete_database(db_name)
            return "ok"
        except:
            return "error"

    # Crear documentos
    def add_doc (self, db, *args):
        try:
            for doc in args:
                document = db.create_document(doc)
                return "ok"
        except:
            return "error"

    # Actualizar documentos
    def update_doc(self, db, key_i, value_i, data):
        try:
            docs = CloudantManager.get_all_docs(db)
            for doc in docs:
                if doc['doc'].get(key_i) == value_i:
                    document = db[doc['id']]
                    for key, value in data.items():
                        document[key] = value
                    document.save()
            return "ok"
        except:
            return "error"

    # Eliminar documentos
    def delete_doc(self, db, id_doc, key_i):
        try:
            doc_temp = db[id_doc]
            doc_temp.delete()
            return "ok"
        except:
            return "error"

    # Consulta general
    @staticmethod
    def get_all_docs(db):
        try:
            docs = Result(db.all_docs, include_docs = True)
            return docs
        except:
            return "error"

    # Consulta individual
    def get_query_by(self, db, value_i, key_i):
        try:
            list_docs = []
            docs = CloudantManager.get_all_docs(db)
            for doc in docs:
                if doc["doc"].get(key_i) == value_i:
                    print(doc["doc"].get(key_i) == value_i, value_i, key_i, sep='-')
                    list_docs.append(doc)
            return list_docs
        except:
            return "error"

