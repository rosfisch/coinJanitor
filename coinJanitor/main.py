import pandas as pd
import customtkinter as ctk

ctk.set_appearance_mode("dark")

class coinApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("My coin collection")
        self.geometry("900x600")

        label = ctk.CTkLabel(self, text="Coin collection", font=("Arial", 24))
        label.pack(pady=40)

        textbox = customtkinter.CtkTextbox(app)

app = coinApp()
app.mainloop()