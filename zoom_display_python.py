import tkinter as tk
from pynput import keyboard
import time

class ZoomDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Sembunyikan window utama
        self.zoom_active = False
        self.notification_window = None
        self.auto_hide_id = None
        
    def show_notification(self, text, bg_color, fg_color):
        """Tampilkan notifikasi di layar"""
        # Batalkan auto-hide sebelumnya jika ada
        if self.auto_hide_id:
            self.root.after_cancel(self.auto_hide_id)
            self.auto_hide_id = None
        
        # Jika window sudah ada, update saja
        if self.notification_window and self.notification_window.winfo_exists():
            # Update label yang ada
            for widget in self.notification_window.winfo_children():
                widget.config(text=text, bg=bg_color, fg=fg_color)
        else:
            # Buat window baru
            self.notification_window = tk.Toplevel(self.root)
            self.notification_window.overrideredirect(True)
            self.notification_window.attributes('-topmost', True)
            
            # Posisi di tengah atas layar
            screen_width = self.notification_window.winfo_screenwidth()
            x = (screen_width - 250) // 2
            y = 50
            self.notification_window.geometry(f'250x60+{x}+{y}')
            
            # Buat label
            label = tk.Label(
                self.notification_window,
                text=text,
                font=("Arial", 16, "bold"),
                bg=bg_color,
                fg=fg_color,
                padx=15,
                pady=15
            )
            label.pack()
        
        # Auto-hide setelah 1 detik
        self.auto_hide_id = self.root.after(1000, self.hide_notification)
    
    def hide_notification(self):
        """Sembunyikan notifikasi"""
        if self.notification_window and self.notification_window.winfo_exists():
            self.notification_window.destroy()
            self.notification_window = None
        self.auto_hide_id = None
    
    def toggle_zoom(self):
        """Toggle status zoom"""
        self.zoom_active = not self.zoom_active
        
        if self.zoom_active:
            print(f"[{time.strftime('%H:%M:%S')}] Status: Zoom ACTIVE ✓")
            self.show_notification("🔍 Zoom Active", "#00ff00", "black")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Status: Zoom INACTIVE ✗")
            self.show_notification("🚫 Zoom Inactive", "#ff3333", "white")
    
    def on_press(self, key):
        """Handler untuk key press"""
        try:
            if hasattr(key, 'char') and key.char == '1':
                # Gunakan after untuk menjalankan di main thread
                self.root.after(0, self.toggle_zoom)
        except AttributeError:
            pass
        except Exception as e:
            print(f"Error: {e}")
    
    def run(self):
        """Jalankan aplikasi"""
        # Start keyboard listener di thread terpisah
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        
        # Jalankan Tkinter mainloop
        self.root.mainloop()

def main():
    print("=" * 50)
    print("Program Zoom Toggle berjalan...")
    print("=" * 50)
    print("Tekan tombol '1' untuk toggle Zoom Active/Inactive")
    print("Tekan Ctrl+C untuk keluar")
    print("=" * 50)
    print()
    
    app = ZoomDisplay()
    
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")

if __name__ == "__main__":
    main()
