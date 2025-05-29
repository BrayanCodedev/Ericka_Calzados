class Product ():
    def __init__(self, id, 
                nombre, 
                descripcion,
                imagen) -> None:
        self.id = id
        self.nombre = nombre
        self.descricion = descripcion
        self.imagen = imagen
    @staticmethod
    def get_all(conn):
        sql ="SELECT * FROM products;"
        cursor = conn.cursor()
        datos = cursor.execute(sql)
        Productos =[]
        for row in datos.fetchall():
            Productos.append(
                Product(row[0],row[1],row[2],row[3],)
            )
        return Productos