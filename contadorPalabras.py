import sys
from PyQt5 import QtWidgets, uic

class contadorPalabras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #carga nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)

    def ContarPalabras(self):
        #Recuperar texto✅
        texto = self.edtCaracteres.text()
        print(texto)

        #SepararTexto✅|    
        textoSeparado = texto.split()
        print(textoSeparado)

        #Contar palabras✅
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"palabras: {cantidadPalabras}")
        print("Palabras: ", cantidadPalabras)

        #Contar CAracteres
        totalCaracteres=0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        print("caracteres: ", totalCaracteres)


        print("Se ha presionado el boton")

        if (cantidadPalabras >=50 ) :
            self.tvPalabras.setStyleSheet("color: #ff756b")
        else :
                self.tvPalabras.setStyleSheet("color: #3478D4")
        if (cantidadPalabras >=50 ) :
            self.tvCaracteres.setStyleSheet("color: #ff756b")
        else :
                self.tvCaracteres.setStyleSheet("color: #3478D4")
                               
                    

app= QtWidgets.QApplication(sys.argv)
ventana = contadorPalabras()
ventana.show()
sys.exit(app.exec())