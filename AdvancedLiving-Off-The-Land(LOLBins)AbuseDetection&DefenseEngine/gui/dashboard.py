import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import queue
event_queue = queue.Queue()
def push_event(message, level="info"):
    event_queue.put((message, level))
def start_dashboard():
    root = tk.Tk()
    root.title("LOLBINS-X | Advanced Endpoint Defense")
    root.geometry("1050x600")
    root.configure(bg="#05080d") 
    title = tk.Label(
        root,
        text="🛡️ LOLBINS-X | DEFENSE ENGINE",
        font=("Consolas", 26, "bold"),
        fg="#00ffd5",
        bg="#05080d"
    )
    title.pack(pady=(15, 5))

    subtitle = tk.Label(
        root,
        text="Real-time living-off-the-land attack detection & defense",
        font=("Consolas", 14),
        fg="#94a3b8",
        bg="#05080d"
    )
    subtitle.pack(pady=(0, 15))

    log_area = ScrolledText(
        root,
        width=120,
        height=24,
        font=("Consolas", 14, "bold"), 
        bg="#020617",
        fg="#e5e7eb",
        insertbackground="#00ffd5",
        borderwidth=0
    )
    log_area.pack(padx=20, pady=15)
    log_area.tag_config("low", foreground="#22c55e")        
    log_area.tag_config("medium", foreground="#facc15")     
    log_area.tag_config("high", foreground="#ef4444")       
    log_area.tag_config("blocked", foreground="#ff0033")    
    log_area.tag_config("info", foreground="#38bdf8")       
    log_area.tag_config("system", foreground="#a78bfa")     

    def update_logs():
        while not event_queue.empty():
            msg, level = event_queue.get()
            log_area.insert(tk.END, msg + "\n", level)
            log_area.see(tk.END)
        root.after(250, update_logs)

    update_logs()
    root.mainloop()
