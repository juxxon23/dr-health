import bcrypt

class Crypt():
    # Generar Hash de tipo String
    def hash_string(self, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hash_password

    #comparar hash
    def check_hash(self, password, hash):
        result = bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
        return result