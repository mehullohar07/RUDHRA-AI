import tkinter as tk
import threading

from core.command_handler import process_command
from core.assistant import ASSISTANT_NAME, VERSION

class RudhraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{ASSISTANT_NAME} | v{VERSION}")
        self.root.geometry("900x600")
        self.root.minsize(650, 450)
        self.root.configure(bg="#171717")

        self.is_waiting = False
        self.create_widgets()

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def create_widgets(self):
        header = tk.Frame(self.root, bg="#222222", height=65)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text=ASSISTANT_NAME,
            font=("Segoe UI", 16, "bold"),
            fg="#ffffff",
            bg="#222222",
        ).pack(side="left", padx=22, pady=15)

        tk.Label(
            header,
            text=f"v{VERSION}",
            font=("Segoe UI", 10),
            fg="#aaaaaa",
            bg="#222222",
        ).pack(side="right", padx=22)

        self.chat_area = tk.Text(
            self.root,
            bg="#171717",
            fg="#eeeeee",
            font=("Segoe UI", 11),
            wrap="word",
            relief="flat",
            padx=22,
            pady=20,
            state="disabled",
        )
        self.chat_area.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10,
        )

        self.add_message(
            ASSISTANT_NAME,
            "System initialized. Desktop interface is ready.",
        )

        input_frame = tk.Frame(self.root, bg="#222222")
        input_frame.pack(
            fill="x",
            padx=18,
            pady=(5, 18),
        )

        self.message_input = tk.Entry(
            input_frame,
            bg="#303030",
            fg="#ffffff",
            insertbackground="#ffffff",
            font=("Segoe UI", 12),
            relief="flat",
        )
        self.message_input.pack(
            side="left",
            fill="x",
            expand=True,
            padx=12,
            pady=12,
        )
        self.message_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg="#eeeeee",
            fg="#171717",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
        )
        self.send_button.pack(
            side="right",
            padx=(0, 12),
            pady=10,
        )

        self.status_label = tk.Label(
            self.root,
            text="Ready",
            bg="#171717",
            fg="#aaaaaa",
            font=("Segoe UI", 9),
            anchor="w",
        )
        self.status_label.pack(fill="x", padx=22, pady=(0, 8))

    
    def add_message(self, sender, message):
        self.chat_area.configure(state="normal")

        if sender == "You":
            name_tag = "user_name"
        else:
            name_tag = "ai_name"

        self.chat_area.insert("end", f"{sender}\n", name_tag)
        self.chat_area.insert("end", f"{message}\n\n", "message_body")

        self.chat_area.configure(state="disabled")
        self.chat_area.see("end")

    def send_message(self, event=None):
        if self.is_waiting:
            return "break"

        message = self.message_input.get().strip()

        if not message:
            return "break"

        self.message_input.delete(0, "end")

        self.is_waiting = True
        self.send_button.configure(state="disabled")
        self.status_label.configure(text=f"{ASSISTANT_NAME} is thinking...")

        self.add_message("You", message)
        self.add_message(ASSISTANT_NAME, "Thinking...")

        worker = threading.Thread(
            target=self.get_response_in_background,
            args=(message,),
            daemon=True,
        )
        worker.start()

        return "break"

    def get_response_in_background(self, message):
        try:
            result = process_command(message)
            response = result["text"]
            should_exit = result["should_exit"]

        except Exception as error:
            response = "Sorry, something went wrong while processing your request."
            should_exit = False

        try:
            self.root.after(
                0,
                lambda: self.show_response(response, should_exit),
            )
        except tk.TclError:
            pass


    def show_response(self, response, should_exit=False):
        if not self.root.winfo_exists():
            return

        self.chat_area.configure(state="normal")

        content = self.chat_area.get("1.0", "end-1c")
        marker = f"{ASSISTANT_NAME}\nThinking...\n\n"
        position = content.rfind(marker)

        if position != -1:
            content = (
                content[:position]
                + f"{ASSISTANT_NAME}\n{response}\n\n"
            )

            self.chat_area.delete("1.0", "end")
            self.chat_area.insert("end", content)

        self.chat_area.configure(state="disabled")
        self.chat_area.see("end")

        self.is_waiting = False
        self.send_button.configure(state="normal")
        self.status_label.configure(text="Ready")
        self.message_input.focus_set()

        if should_exit:
            self.close_app()

    def close_app(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    RudhraGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()