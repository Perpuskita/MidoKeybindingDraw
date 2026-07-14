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
        return None
    
    def keyboard(self, commands: list[str] ):
        
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.press('t')
            self.keyboard.release('t')

    def mouse(self, command: list[str]):
        self.mouse.click(button=Button.left, count=1)