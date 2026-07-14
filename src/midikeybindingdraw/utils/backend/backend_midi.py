import pygame.midi
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from midikeybindingdraw.utils.frontend import FrontEndToast
from midikeybindingdraw.exception import MidiException

NOTE: dict = {
    0:"C", 1:"C#", 2:"D", 3:"D#", 4:"E",
    5:"F", 6:"F#", 7:"G", 8:"G#", 
    9:"A", 10:"A#", 11:"B"
}

class BackendMidi:
    def __init__(self, controller):
        pygame.init()
        pygame.midi.init()
        
        # membuat variabel midi input
        self.midi_input = None
        
        # menyimpan controller
        self.controller = controller

        # mendapatkan qaplication di mido keybinding draw
        self.app: QApplication = controller.frontend.app 
        self.exception = MidiException()
        
    # mentranslate hasil dari int menjadi literal note midi controller
    def translate(self, note:int, velocity:int ) -> str:
        modulus: int = note%12
        octave: int = ( note - modulus ) // 12

        return f"{NOTE.get(modulus)}{octave}"
    
    def device_init(self):
        
        print(f"Reading from MIDI device")
        input_id = pygame.midi.get_default_input_id()
        
        if input_id == -1:
            self.exception.device_unconnected()
            return

        print(f"Device found: {input_id}")
        return pygame.midi.Input(input_id)

    def run(self):
        self.midi_input = self.device_init()
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
                        notes = self.translate(note=note, velocity=velocity)
                        self.controller.execute_command(key=notes)
                        
        except Exception as e:
            self.exception.app_error()