from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from sistemaAutenticar import LoginSistemaAutenticar



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = LoginSistemaAutenticar()
    window.show()
    app.exec()


