from .utils.backend import BackendMidi, BackendBinding, BackendController
from .utils.frontend import FrontEndToast
from PyQt6.QtWidgets import QApplication
import sys

class MidiKeyBindingDraw():
    def __init__(self):
        self.frontend = FrontEndToast()
        self.midi = BackendMidi(app=self.frontend.app)
        self.binding = BackendBinding()
        pass
    
    def detect_keyboard(self) -> None:
        return None

    # fungsi untuk menjalankan dan memulai loop
    def run(self) -> None:
        self.midi.run()
        app_qt = QApplication(sys.argv)

        try:
            sys.exit(app_qt.exec())

        except KeyboardInterrupt:
            print("Exit...")
            self.midi.close()
            sys.exit(0)

        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")
            import traceback
            traceback.print_exc()
            self.midi.close()
            sys.exit(1)

        return None
    
    def collect_event(self) -> None:
        return None

    def add(self, key: str, command: str) -> None:
        return None
    
    def configure(self) -> None:
        return None
    
    def print_message(self) -> str:
        return "testt"