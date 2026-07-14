# make binding
# use c7 for undo
# use c#7 for transpose
from midikeybindingdraw import MidiKeyBindingDraw

if __name__  == "__main__" :
    app = MidiKeyBindingDraw()
    app.detect_keyboard()

    # # memasukan beberapa key binding
    app.add("C7", "#Undo")
    # app.add("C#7", "#Transpose")

    # # app.run untuk memulai menjalankan aplikasi
    app.run()
