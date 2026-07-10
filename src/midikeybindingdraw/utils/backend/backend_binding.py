from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

class BackendBinding:
    def __init__(self):
        
        mouse = MouseController()
        keyboard = KeyboardController()

        print("Siap-siap... Makro berjalan dalam 3 detik.")
        time.sleep(3)

        # 1. Lakukan Klik Mouse di posisi saat ini
        mouse.click(Button.left, 1)
        time.sleep(0.1)

        # 2. Simulasikan Tekan & Tahan Ctrl, lalu tekan T
        with keyboard.pressed(Key.ctrl):
            keyboard.press('t')
            keyboard.release('t')

        print("Perintah klik + Ctrl+T berhasil dikirim!")
    
    def parse(self) -> None:

        return None