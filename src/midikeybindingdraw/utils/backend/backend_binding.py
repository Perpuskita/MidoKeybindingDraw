from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

class BackendBinding:
    def __init__(self):
        
        self.mouse: MouseController = MouseController()
        self.keyboard: KeyboardController = KeyboardController()

        # penyimpan command dengan menggunakan dictionary
        self.commands: dict = {}

    # menambahkan command dengan binding key : command
    def add_command(self, key: str, command:str):
        self.commands[key] = command

    # execute command untuk key
    def execute_command(self, key) -> None:
        command = None
        command = self.commands.get(key)

        if command == None :
            print(f"key { key } belum dibinding dengan command apapun ... ")

        else :
            self.parse(command=command)

        return None


    def parse(self, command: str) -> None:

        self.keyboard_run([Key.ctrl, 'c'])
        commands: list[str] = command.split("+") 

        # mengubah ctrl dan shift key
        for i, command in enumerate(commands):
            key = command

            # perbcabangan ctrl dan shif
            if command == 'ctrl':
                key = Key.ctrl            
            elif command == 'shift':
                key = Key.shift

            # mngubah command[i] menjadi key
            commands[i] = key

        self.keyboard_run(commands=commands)
        return None
    
    def keyboard_run(self, commands: list[Key] ):
        try:
            for key in commands:
                self.keyboard.press(key=key)

        # release button dari belakang
        finally:
            for key in reversed(commands):
                self.keyboard.release(key=key)

    def mouse(self, command: list[str]):
        self.mouse.click(button=Button.left, count=1)