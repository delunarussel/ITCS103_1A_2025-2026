import tkinter as tk

window = tk.Tk()

window.title("STUDENT PROFILE")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="pink",cursor="hand2")



label = tk.Label(window, text = "STUDENT PROFILE", font = ("Poppins",35), fg = "blue", bg = "pink", anchor = "center")
label.pack(padx=20,pady=20)

label = tk.Label(window, text = "RUSSEL REVILLOSA DE LUNA", font = ("Poppins",25), fg = "black", bg = "pink")
label.pack(padx=20,pady=20, anchor = "w")

label = tk.Label(window, text = "19 YEARS OLD", font = ("Poppins",25), fg = "black", bg = "pink")
label.pack(padx=20,pady=20,anchor = "w")

label = tk.Label(window, text = "BSIT - 1A", font = ("Poppins",25), fg = "black", bg = "pink")
label.pack(padx=20,pady=20, anchor = "w")


label = tk.Label(window, text = "SEPTEMBER 25 2006", font = ("Poppins",25), fg = "black", bg = "pink")
label.pack(padx=20,pady=20, anchor = "w")

label = tk.Label(window, text = "BUHAY BUHAY LANG", font = ("Poppins",25), fg = "black", bg = "pink")
label.pack(padx=20,pady=20, anchor = "w")

window.mainloop()