# 🔍 Zoom Toggle Notification

Program sederhana untuk menampilkan notifikasi status Zoom di layar desktop dengan menekan tombol keyboard.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ✨ Fitur

- 🎯 Toggle status Zoom dengan menekan tombol **1**
- 💚 Notifikasi "Zoom Active" dengan background hijau
- ❤️ Notifikasi "Zoom Inactive" dengan background merah
- ⚡ Respons cepat dan realtime
- 🎨 Tampilan notifikasi yang clean dan modern
- ⏱️ Auto-hide setelah 1 detik
- 🔄 Dapat menekan berulang kali tanpa crash

## 📸 Preview

Ketika tombol **1** ditekan:
- **Pertama kali**: Muncul "🔍 Zoom Active" (hijau)
- **Kedua kali**: Muncul "🚫 Zoom Inactive" (merah)
- **Selanjutnya**: Toggle antara Active/Inactive

## 🚀 Instalasi

### Prerequisites

Pastikan Python 3.7+ sudah terinstall di sistem Anda.

### Install Dependencies

```bash
pip install pynput
```

atau gunakan requirements.txt:

```bash
pip install -r requirements.txt
```

## 📝 Cara Penggunaan

1. Clone repository ini:
```bash
git clone https://github.com/username/zoom-toggle-notification.git
cd zoom-toggle-notification
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan program:
```bash
python zoom_toggle.py
```

4. Tekan tombol **1** di keyboard untuk toggle status Zoom

5. Untuk menghentikan program, tekan **Ctrl+C** di terminal

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+**
- **Tkinter** - untuk GUI dan notifikasi
- **pynput** - untuk mendeteksi input keyboard

## 📂 Struktur File

```
zoom-toggle-notification/
│
├── zoom_toggle.py       # File utama program
├── requirements.txt     # Dependencies
├── README.md           # Dokumentasi
└── LICENSE             # Lisensi MIT
```

## ⚙️ Konfigurasi

Anda dapat menyesuaikan beberapa parameter dalam file `zoom_toggle.py`:

```python
# Durasi notifikasi (dalam milidetik)
self.root.after(1000, self.hide_notification)  # 1000 = 1 detik

# Ukuran notifikasi
self.notification_window.geometry(f'250x60+{x}+{y}')

# Ukuran font
font=("Arial", 16, "bold")

# Warna background
bg_color="#00ff00"  # Hijau untuk Active
bg_color="#ff3333"  # Merah untuk Inactive
```

## 🐛 Troubleshooting

### Program tidak merespon keyboard
- **Linux**: Jalankan dengan `sudo` karena memerlukan permission untuk keyboard listener
  ```bash
  sudo python3 zoom_toggle.py
  ```

### ModuleNotFoundError: No module named 'pynput'
- Install pynput terlebih dahulu:
  ```bash
  pip install pynput
  ```

### Notifikasi tidak muncul
- Pastikan tidak ada program lain yang menggunakan Tkinter
- Coba restart program

## 📋 Requirements.txt

```
pynput>=1.7.6
```

## 🤝 Kontribusi

Kontribusi selalu welcome! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Terima kasih kepada komunitas Python
- Inspired by kebutuhan untuk monitoring status Zoom meeting
- Built with ❤️ using Python

---

⭐ Jika project ini membantu, jangan lupa berikan star!
