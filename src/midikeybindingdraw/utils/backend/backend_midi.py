import pygame.midi
from .backend_controller import BackendController


NOTE: dict = {
    0:"C", 1:"C#", 2:"D", 3:"D#", 4:"E",
    5:"F", 6:"F#", 7:"G", 8:"G#", 
    9:"A", 10:"A#", 11:"B"
}

class BackendMidi:
    def __init__(self):

        pygame.init()
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        
        if input_id == -1:
            print("No MIDI input devices found.")
            return

        midi_input = pygame.midi.Input(input_id)
        print(f"Reading from MIDI device ID: {input_id}")

        try:
            going = True
            while going:
                if midi_input.poll():
                    midi_events = midi_input.read(10)
                    
                    for event in midi_events:
                        data, timestamp = event
                        status, note, velocity, _ = data
                        
                        if velocity == 0:
                            continue

                        if status == 144:
                            print(self.translate(note=note, velocity=velocity))

                pygame.time.wait(10)

        except KeyboardInterrupt:
            print("\nExiting...")
            
        finally:
            midi_input.close()
            pygame.midi.quit()
            pygame.quit()

    # mentranslate hasil dari int menjadi literal note midi controller
    def translate(self, note:int, velocity:int ) -> str:
        modulus: int = note%12
        octave: int = ( note - modulus ) // 12

        return f"{NOTE.get(modulus)}{octave}"