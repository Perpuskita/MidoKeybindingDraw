import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation

class FrontEndToast:
    def __init__(self):
        # Pastikan QApplication sudah ada, jika belum buat baru
        self.app = QApplication.instance()
        if not self.app:
            self.app = QApplication(sys.argv)
            
        self.toast = QLabel(text="toast")
        self.anim = None  # Simpan animasi sebagai atribut kelas
        self.make_toast()
    
    def make_toast(self):
        self.toast.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.SubWindow
        )
        self.toast.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.toast.setStyleSheet(
            "QLabel { background-color: #333; color: white; "
            "font-size: 24px; padding: 20px 40px; border-radius: 5px; }"
        )
        self.toast.adjustSize()
        self.toast.hide() # Sembunyikan awal
        
        # Positioning
        screen = self.app.primaryScreen().geometry()
        self.toast.move(
            (screen.width() - self.toast.width()) // 2, 
            int(screen.height() * 0.85)
        )
    
    def showtoast(self, text: str = "toast", duration: int = 1000):
        # 1. Update konten
        self.toast.setText(text)
        self.toast.adjustSize()
        
        # 2. Repositioning karena ukuran teks berubah
        screen = self.app.primaryScreen().geometry()
        self.toast.move(
            (screen.width() - self.toast.width()) // 2, 
            int(screen.height() * 0.85)
        )
        
        # 3. Reset state
        self.toast.setWindowOpacity(1.0)
        self.toast.show()
        
        # 4. Stop animasi sebelumnya jika ada
        if self.anim and self.anim.state() == QPropertyAnimation.State.Running:
            self.anim.stop()
            
        # 5. Buat animasi baru
        self.anim = QPropertyAnimation(self.toast, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        
        # 6. Jadwalkan animasi dan hide
        # Animasi mulai setelah (duration - waktu_animasi)
        if duration > 500:
            QTimer.singleShot(duration - 500, self.anim.start)
        else:
            self.anim.start()
            
        # Sembunyikan toast setelah durasi selesai
        QTimer.singleShot(duration, self.toast.hide)

if __name__ == "__main__":
    app_qt = QApplication(sys.argv) # Buat instance QApplication utama di sini
    
    toaster = FrontEndToast()
    
    # Panggil pertama kali
    toaster.showtoast(text="Halo Dunia!", duration=2000)
    
    # Panggil kedua kali setelah 3 detik (simulasi event lain)
    QTimer.singleShot(1000, lambda: toaster.showtoast(text="Pesan Kedua", duration=1500))
    QTimer.singleShot(3000, lambda: toaster.showtoast(text="Pesan Ketiga", duration=1500))
    
    # Jalankan event loop di sini, bukan di dalam class
    sys.exit(app_qt.exec())