import pygame.midi
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from .backend_controller import BackendController


NOTE: dict = {
    0:"C", 1:"C#", 2:"D", 3:"D#", 4:"E",
    5:"F", 6:"F#", 7:"G", 8:"G#", 
    9:"A", 10:"A#", 11:"B"
}

class BackendMidi:
    def __init__(self, app: QApplication):
        pygame.init()
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()

        self.app = app
        
        if input_id == -1:
            print("No MIDI input devices found.")
            return

        self.midi_input = pygame.midi.Input(input_id)
        print(f"Reading from MIDI device ID: {input_id}")

    # mentranslate hasil dari int menjadi literal note midi controller
    def translate(self, note:int, velocity:int ) -> str:
        modulus: int = note%12
        octave: int = ( note - modulus ) // 12

        return f"{NOTE.get(modulus)}{octave}"
    
    def run(self):
        self.timer = QTimer(self.app)
        self.timer.timeout.connect(self.update_detection)
        self.timer.start(16)

    def close(self):
        self.timer.stop()
        self.timer.timeout.disconnect()
        self.midi_input.close()
        pygame.midi.quit()
        pygame.quit()
        pass

    def update_detection(self):
        try:
            if self.midi_input.poll():
                midi_events = self.midi_input.read(3)
                
                for event in midi_events:
                    data, timestamp = event
                    status, note, velocity, _ = data
                    
                    if velocity == 0:
                        continue

                    if status == 144: # Note On
                        # Pastikan objek self masih utuh sebelum print/translate
                        print(self.translate(note=note, velocity=velocity))
                        
        except Exception as e:
            # Tangkap error jika MIDI tiba-tiba tertutup saat membaca
            print(f"Error reading MIDI: {e}")