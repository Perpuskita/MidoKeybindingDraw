# make binding
# use c4 for undo
# use c#4 for transpose
from midikeybindingdraw import MidiKeyBindingDraw

if __name__  == "__main__" :
    app = MidiKeyBindingDraw()
    app.detect_keyboard()

    # # memasukan beberapa key binding
    app.add("C4", "#Undo")
    app.add("C#4", "#Transpose")


    # # app.run untuk memulai menjalankan aplikasi
    app.run()
