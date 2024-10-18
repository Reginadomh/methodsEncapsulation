import tkinter as tk

class Window:
    __ancho = 500
    __alto = 200
    __titulo = "Test"
    __resize = False
    __label_titulo = "Primer ventana"

    def setDimensions(self, width, height):
        self.__ancho = width
        self.__alto = height

    def getDimensions(self):
        return [self.__ancho, self.__alto]

    def setResize(self, resize):
        self.__resize = resize

    def getResize(self):
        return self.__resize

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

    def setLabelTitulo(self, label_titulo):
        """Método para establecer el texto del título dentro de la ventana."""
        self.__label_titulo = label_titulo

    def getLabelTitulo(self):
        """Método para obtener el texto del título dentro de la ventana."""
        return self.__label_titulo

    def crear_ventana(self):

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title(self.__titulo)

        # Establecer el tamaño de la ventana (ancho x alto)
        ventana.geometry(f"{self.__ancho}x{self.__alto}")

        # Evitar que la ventana sea redimensionable si así se ha configurado
        ventana.resizable(self.__resize, self.__resize)

        # Crear una etiqueta dentro de la ventana
        etiqueta = tk.Label(ventana, text=self.__label_titulo, font=("Arial", 14))
        etiqueta.pack(pady=20)  # Agrega padding vertical para centrar la etiqueta

        # Iniciar el bucle principal de la ventana
        ventana.mainloop()
