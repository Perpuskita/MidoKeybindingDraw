from .utils.backend import BackendMidi, BackendBinding

class MidiKeyBindingDraw():
    def __init__(self):
        midi = BackendMidi()
        binding = BackendBinding()
        pass
    
    def detect_keyboard(self) -> None:
        return None

    def run(self) -> None:
        return None
    
    def collect_event(self) -> None:
        return None

    def add(self, key: str, command: str) -> None:
        return None
    
    def configure(self) -> None:
        return None
    
    def print_message(self) -> str:
        return "testt"