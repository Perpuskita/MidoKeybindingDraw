import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation

class FrontEndToast:
    def __init__(self):
        # Ensure QApplication exists
        self.app = QApplication.instance()
        if not self.app:
            self.app = QApplication(sys.argv)
            
        self.toast = QLabel(text="toast")
        self.anim = None  
        
        # We need TWO manageable timers to replace all single shots safely
        self.animation_timer = QTimer(self.app)
        self.animation_timer.setSingleShot(True)
        
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
        self.toast.hide() 
        
        # Positioning
        screen = self.app.primaryScreen().geometry()
        self.toast.move(
            (screen.width() - self.toast.width()) // 2, 
            int(screen.height() * 0.85)
        )
    
    def showtoast(self, text: str = "toast", duration: int = 2000, hide_duration: int = 500):
        # 1. Clear ALL previous timers and animations instantly to prevent collision
        self.animation_timer.stop()
        
        if self.anim and self.anim.state() == QPropertyAnimation.State.Running:
            self.animation_timer.timeout.disconnect()
            self.anim.stop()

        # 2. Update content and UI state
        self.toast.setText(text)
        self.toast.adjustSize()
        
        # 3. Repositioning
        screen = self.app.primaryScreen().geometry()
        self.toast.move(
            (screen.width() - self.toast.width()) // 2, 
            int(screen.height() * 0.85)
        )
        
        self.toast.setWindowOpacity(1.0)
        self.toast.show()
        
        # 4. Create new animation
        self.anim = QPropertyAnimation(self.toast, b"windowOpacity")
        self.anim.setDuration(hide_duration)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        
        # Connect the timer to this specific animation instance
        self.animation_timer.timeout.connect(self.anim.start)

        # 5. Handle timing logic
        if duration > hide_duration:
            self.animation_timer.start(duration - hide_duration)
        else:
            self.anim.start()
            


