import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Player Display")
        self.geometry("800x560")
        self.grid_columnconfigure((0, 1), weight=1)
        #Text labels - OLED
        self.oled_label_l = customtkinter.CTkLabel(self, text="OLED text Left")
        self.oled_label_l.grid(row=0, column = 0, padx= 20, pady=20, sticky = "n")

        self.oled_label_r = customtkinter.CTkLabel(self, text="OLED text right")
        self.oled_label_r.grid(row=0, column = 1, padx= 20, pady=20, sticky = "n")
        
        #Enter Oled text left, any text
        self.oled_entry_l = customtkinter.CTkEntry(self, placeholder_text="Value 1")
        self.oled_entry_l.grid(row=1, column = 0, padx= 20, pady=20, sticky = "n")
        
        #Enter Oled text right, any text
        self.oled_entry_r = customtkinter.CTkEntry(self, placeholder_text="Value 2")
        self.oled_entry_r.grid(row=1, column = 1, padx= 20, pady=20, sticky = "n")

        #Text labels - Digits
        self.digit_label_l = customtkinter.CTkLabel(self, text="Counter 1")
        self.digit_label_l.grid(row=2, column = 0, padx= 20, pady=20, sticky = "n")

        self.digit_label_r = customtkinter.CTkLabel(self, text="Counter 2")
        self.digit_label_r.grid(row=2, column = 1, padx= 20, pady=20, sticky = "n")

        #Enter number left 4 digits, only numbers
        self.digits_l = customtkinter.CTkEntry(self, placeholder_text="1021")
        self.digits_l.grid(row=3, column = 0, padx= 20, pady=20, sticky = "n")
        #Enter number right 4 digits, only numbers
        self.digits_r = customtkinter.CTkEntry(self, placeholder_text="0003")
        self.digits_r.grid(row=3, column = 1, padx= 20, pady=20, sticky = "n")

        self.send_button = customtkinter.CTkButton(self, text="Send values",command=self.button_callback)
        self.send_button.grid(row=4,column=0,columnspan=2)
        
    def button_callback(self):
        print(self.oled_entry_l.get())
        print(self.oled_entry_r.get())
        print(self.digits_l.get())
        print(self.digits_r.get())



app = App()
app.mainloop()