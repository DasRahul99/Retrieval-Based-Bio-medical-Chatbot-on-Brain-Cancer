from tkinter import *
from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 12 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Biomedical ChatBot on Brain Cancer")
        self.window.geometry("500x400")

        # Head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Hello I am your medical assistance.\nHow can I help you today?",
                           font=FONT_BOLD, pady=5)
        head_label.pack(fill=X)

        # Tiny divider
        line = Label(self.window, bg=BG_GRAY)
        line.pack(fill=X, pady=5)

        # Text widget
        self.text_widget = Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5, wrap="word")
        self.text_widget.pack(fill=BOTH, expand=True)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_widget.yview)

        # Bottom frame
        bottom_frame = Frame(self.window, bg=BG_GRAY)
        bottom_frame.pack(fill=X, side=BOTTOM)

        # Message entry box
        self.msg_entry = Entry(bottom_frame, bg="#2C3E50",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.pack(fill=X, padx=5, pady=5)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_frame, text="Send", font=FONT_BOLD, width=20, bg=BG_COLOR, fg=TEXT_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.pack(side=RIGHT, padx=5, pady=5)

        # Quit button
        quit_button = Button(bottom_frame, text="Quit", font=FONT_BOLD, width=20, bg=BG_COLOR, fg=TEXT_COLOR,
                             command=self.window.quit)
        quit_button.pack(side=RIGHT, padx=5, pady=5)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        if msg.lower() == "quit":
            self.window.quit()

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)

        # User message
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # Bot response
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
