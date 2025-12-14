import customtkinter

#pencere oluşturuldu
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("Text-to-Cad")
app.geometry("700x500")

#sayfa başlığı
pageTitle = customtkinter.CTkLabel(master=app, text="Text to CAD", font=("arial", 30))
pageTitle.pack(pady=30)


def on_enter(event):
    # Kutuya tıklandığında placeholder silinsin
    if promt_textBox.get("0.0", "end-1c") == placeholder_text:
        promt_textBox.delete("0.0", "end")
        promt_textBox.configure(text_color="white")

def on_leave(event):
    # Kutudan çıkıldığında eğer boşsa placeholder geri gelsin
    if promt_textBox.get("0.0", "end-1c") == "":
        promt_textBox.insert("0.0", placeholder_text)
        promt_textBox.configure(text_color="gray") 

placeholder_text = "Oluşturmak istediğiniz çizimi açıklayın..."
promt_textBox = customtkinter.CTkTextbox(master=app, width=500)
promt_textBox.pack(pady=15)

promt_textBox.insert(("0.0"), text=placeholder_text)

promt_textBox.bind("<FocusIn>", on_enter)
promt_textBox.bind("<FocusOut>", on_leave)

createButton = customtkinter.CTkButton(master=app, text="Oluştur", width=500, height=40, font=("Arial", 15))
createButton.pack(pady=5)

infoLabel = customtkinter.CTkLabel(master=app, text="Bekeniyor...", font=("Arial", 15))
infoLabel.pack(pady=25)

detail_textBox = customtkinter.CTkLabel(master=app)

app.mainloop()