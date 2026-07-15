# make binding
# use c4 for undo
# use c#4 for transpose
from midikeybindingdraw import MidiKeyBindingDraw

if __name__  == "__main__" :
    app = MidiKeyBindingDraw()
    app.detect_keyboard()

    # # memasukan beberapa key binding
    app.add("C4", "ctrl+c")
    app.add("D4", "ctrl+v")

    # # app.run untuk memulai menjalankan aplikasi
    app.run()
    
    
