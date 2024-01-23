import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

def generate_password(length, use_special_chars):
    if use_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(length_var.get())
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_special_chars)
    result_label.config(text=f"Senha gerada: {password}")
    
    # Copiar a senha para a área de transferência
    pyperclip.copy(password)
    messagebox.showinfo("Senha Copiada", "A senha foi copiada para a área de transferência.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

length_label = ttk.Label(root, text="Escolha o comprimento da senha:")
length_label.pack()

length_var = tk.StringVar()
length_combobox = ttk.Combobox(root, textvariable=length_var, values=[6, 8, 16, 32])
length_combobox.set(6)
length_combobox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(root, text="Incluir caracteres especiais", variable=special_chars_var)
special_chars_checkbox.pack()

generate_button = ttk.Button(root, text="Gerar Senha", command=generate_and_display_password)
generate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()