import User.conection as conection

#creamos las conexiones
connect = conection.conect()
database = connect[0]
cursor = connect[1]

class Note:
    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def save(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        note = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, note)
        database.commit()
        return [cursor.rowcount,self]

    def show(self):
        sql = f"SELECT * FROM notas WHERE usuario_id ={self.usuario_id}"

        cursor.execute(sql)
        database.commit()

        result = cursor.fetchall()
        return result

    def delete(self):
        sql=f"DELETE FROM notas WHERE usuario_id ={self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount,self]

    def update(self):
        sql=f"UPDATE notas SET descripcion = '{self.descripcion}' WHERE titulo = '{self.titulo}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount,self]

