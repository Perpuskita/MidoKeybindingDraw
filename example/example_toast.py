from midikeybindingdraw.utils.frontend import FrontEndToast
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys


class MainWindow(QWidget):
    def __init__(self, toaster: FrontEndToast):
        super().__init__()
        self.toaster = toaster
        
        # Setup window
        self.setWindowTitle("Contoh Toast dengan Tombol")
        self.setGeometry(100, 100, 400, 300)
        
        # Layout
        layout = QVBoxLayout()
        
        # Tombol 1
        btn1 = QPushButton("Tampilkan Toast 1")
        btn1.clicked.connect(lambda: self.toaster.showtoast("Pesan Pertama!"))
        layout.addWidget(btn1)
        
        # Tombol 2
        btn2 = QPushButton("Tampilkan Toast 2")
        btn2.clicked.connect(lambda: self.toaster.showtoast("Pesan Kedua!", 2000))
        layout.addWidget(btn2)
        
        # Tombol 3
        btn3 = QPushButton("Tampilkan Toast 3")
        btn3.clicked.connect(lambda: self.toaster.showtoast("Pesan Ketiga!", 3000))
        layout.addWidget(btn3)
        
        # Tombol dengan pesan kustom
        btn4 = QPushButton("Toast Kustom")
        btn4.clicked.connect(self.show_custom_toast)
        layout.addWidget(btn4)
        
        self.setLayout(layout)
    
    def show_custom_toast(self):
        """Contoh menampilkan toast dengan input dari user"""
        self.toaster.showtoast("Ini pesan kustom!")


if __name__ == "__main__":
    app_qt = QApplication(sys.argv) # Buat instance QApplication utama di sini
    
    # Buat toaster
    toaster = FrontEndToast()
    
    # Buat window utama dengan tombol-tombol
    window = MainWindow(toaster)
    window.show()
    
    # Jalankan event loop
    sys.exit(app_qt.exec())