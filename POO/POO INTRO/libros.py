class Libro:
    def __init__(self, id="12345", titulo="Cien años de soledad", autor="Gabriel García Márquez", publicacion="2000", disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.disponible = disponible

    def mostrarInformacion(self, id):
        if self.id == id:
            print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.publicacion}, Disponible: {self.disponible}")
        else:
            print("El código no existe")

    def prestarLibro(self, id):
        if self.id == id:
            if self.disponible:
                print("Libro disponible. El libro ha sido prestado.")
                self.disponible = False
            else:
                print("El libro ya está prestado.")
        else:
            print("El código del libro no existe.")

    
    def devolverLibro(self,id):
        self.id = id
        if self.id =="12345":
            if self.disponible:
                print("El libro ya esta prestado")
                self.disponible=False
            else:
                print("El libro devuelto")