# MIDI Keybinding Draw

MidiKeybindingDraw adalah aplikasi berbasis Python yang mengubah *input* dari MIDI Controller menjadi *keyboard shortcuts* global. Aplikasi ini dirancang khusus untuk mempercepat alur kerja (*workflow*) seniman digital saat menggunakan aplikasi menggambar.

> **Status Proyek:** Unstable (Fragile)

---

## Fitur Utama

* **Pemetaan Tombol Fleksibel:** Memetakan not MIDI (contoh: `C4`) ke kombinasi tombol keyboard (contoh: `ctrl+c`).
* **Deteksi Perangkat Otomatis:** Mendeteksi MIDI controller dan keyboard secara langsung.
* **Dukungan Pintasan Global:** Menjalankan *shortcut* bahkan saat aplikasi menggambar sedang berjalan di latar depan (*foreground*).
* **Penanganan Eror Kokoh:** Mencegah aplikasi *crash* jika perangkat MIDI terputus secara tiba-tiba.

---

## Cara Instalasi

### 1. Prasyarat
Pastikan Anda telah menginstal Python versi 3.10 atau yang lebih baru.

### 2. Instal Dependensi
Unduh dependensi yang diperlukan menggunakan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```

### 3. Instal Aplikasi
Instal paket `midikeybindingdraw` secara lokal dengan perintah:
```bash
pip install .
```

---

## Cara Penggunaan

Berikut adalah contoh dasar cara mengonfigurasi dan menjalankan aplikasi:

```python
from mido_keybinding_draw import MidiKeyBindingDraw
import sys

def main():
    try:
        # Inisialisasi aplikasi
        app = MidiKeyBindingDraw()
        
        # Deteksi hardware yang terhubung
        app.detect_keyboard()
        app.detect_midi_devices()

        # Konfigurasi Key Binding (Not MIDI -> Shortcut Keyboard)
        app.add("C4", "ctrl+c")
        app.add("D4", "ctrl+v")
        app.add("E4", "ctrl+z")

        # Mulai mendengarkan input
        print("[INFO] Aplikasi berjalan. Tekan Ctrl+C untuk keluar.")
        app.run()

    except KeyboardInterrupt:
        print("\n[INFO] Aplikasi dihentikan oleh pengguna.")
        sys.exit(0)
        
    except Exception as e:
        print(f"[EROR] Terjadi kesalahan fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

> **Tips:** Anda dapat melihat konfigurasi yang lebih kompleks pada folder `examples/`.

---

## Kompatibilitas

### Sistem Operasi
* **Windows 11** (Sangat Kompatibel, Diuji pada versi 25H2)

### Aplikasi Menggambar yang Didukung
* MediBang Paint
* Krita
---

## Library

* **PyQt6** - Manajemen antarmuka dan *event loop*.
* **pynput** - Mengontrol dan mensimulasikan *input* keyboard global.
* **pygame** - Membaca *input* data dari perangkat MIDI (via `pygame.midi`).

---

## Penanganan Eror & Catatan Rilis

Versi terbaru ini masih ber-status *fragile* belum ada *exception handling* untuk menangani error.

---

## Lisensi & Apresiasi

Proyek ini dilisensikan di bawah **GNU GPL3**. Terima kasih kepada komunitas pengembang **PyQt6**, **pynput**, dan **`pygame`** yang menyediakan pustaka luar biasa ini.

---
<p align="center">Dibuat dengan Python untuk Para Seniman Digital</p>
