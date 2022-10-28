import User.conection as conection
import datetime
import hashlib

#creamos las conexiones
connect = conection.conect()
# database = connect[0]
# cursor = connect[1]

#creamos la clase usuario
class User:
    def __init__(self,name, lastName, email, password):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password

    def register(self):
        #llamamos a la esa madre para que nos de la fecha
        date = datetime.datetime.now()

        #cifrar la contraseña
        encryp = hashlib.sha256()
        encryp.update(self.password.encode("utf8"))

        #creamos la sentencia sql
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        User = (self.name, self.lastName, self.email, encryp.hexdigest(), date)

        # cursor.execute(sql, User)
        # database.commit()
        # result = [cursor.rowcount,self]

        #return result

    def identify(self):
        #cifrar la contraseña para que sea la misma
        encryp = hashlib.sha256()
        encryp.update(self.password.encode("utf8"))

        #creamos la sentencia para ver que sean iguales
        sql ="SELECT * FROM usuarios WHERE email = %s AND password = %s"
        User=(self.email, encryp.hexdigest())
        # cursor.execute(sql, User)

        # #fetchone es para que nos retorne solo una fila(?) de la tabla
        # result = cursor.fetchone()

        #return result
