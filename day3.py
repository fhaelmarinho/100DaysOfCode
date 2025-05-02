# ✨ Desafio 100 Dias de Código - Dia 3/100 💻

import os
import tkinter as tk
from tkinter import messagebox, filedialog
from pdf2docx import Converter

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Selecione um Arquivo PDF")
    if file_path:  
        file_name = os.path.basename(file_path)
        file_input.set(file_path) 
        messagebox.showinfo("Arquivo Selecionado", f"Você selecionou: {file_name}")

def convert_pdf():
    pdf_path = file_input.get()
    if not pdf_path or not os.path.exists(pdf_path):
        messagebox.showerror(title="Erro", message="Selecione um arquivo PDF válido")
        return
    docx_path = os.path.splitext(pdf_path)[0]+".docx"
    
    try:
        pdf_converter = Converter(pdf_path)
        pdf_converter.convert(docx_path, start=0, end=None)
        pdf_converter.close()
        messagebox.showinfo(title="Sucesso", message="Arquivo convertido com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Ocorreu um erro durante a conversão: {e}") 
        
window = tk.Tk()
window.title("PDF to DOCX")
window.resizable(width=False, height=False)

file_input = tk.StringVar()

frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True, fill="both")

entry = tk.Entry(frame, textvariable=file_input, width=60)
entry.pack()

botao_adicao = tk.Button(frame, text="Upload", command=select_pdf_file)
botao_adicao.pack(pady=5)

conversor = tk.Button(frame, text="Converter", command=convert_pdf)
conversor.pack(pady=10)

window.mainloop()
