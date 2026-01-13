import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
# Funciones de la aplicacion
# -------------------------------------------------------------------------

# Funcion para nuevo
def newFile():
    if len(text.get(1.0, tk.END)) > 1:
        if messagebox.askyesno("Guardar", "Desea guardar el archivo?"):
            saveFile()
            text.delete(1.0, tk.END)
        else:
            text.delete(1.0, tk.END)
 
# -------------------------------------------------------------------------

# Funcion para abrir
def OpenFile():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Abrir archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if filepath == "":
        messagebox.showerror("Error", "Archivo no encontrado")
        return
    with open(filepath, 'r') as file:
        contenido = file.read()
    text.delete(1.0, tk.END)
    text.insert(tk.END, contenido)
    filename = os.path.basename(filepath)
    windows.title(f"Blog de Notas - {filename}")


# -------------------------------------------------------------------------

# Funcion para guardar
def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text File","*.txt"),
                                               ("All Files","*.*")])
    if file is None:  
        return
    filetext = str(text.get(1.0, tk.END))
    file.write(filetext)
    file.close()
# -------------------------------------------------------------------------
# Funcion de eventos
# Funcion cortar
def cut(event=None):
    text.event_generate("<<Cut>>") 
    
# ------------------------------------------------------------------------- 
# funcion copiar
def copy(event=None):
    text.event_generate("<<Copy>>")
# -------------------------------------------------------------------------

# funcion pegar
def paste(event=None):
    text.event_generate("<<Paste>>")
    
# -------------------------------------------------------------------------
# Crear la ventana principal
windows = tk.Tk()
windows.title(f"Blog de Notas")

# Tamaño de la ventana
windows.geometry("600x700")
# Barra de menu 
menubar = tk.Menu(windows)
windows.config(bg="lightblue", menu=menubar)
# El menu
fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=fileMenu)
fileMenu.add_command(label="Abrir", command=OpenFile)
fileMenu.add_command(label="Nuevo", command=newFile)
fileMenu.add_command(label="Guardar", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=windows.quit)
# Barra de editar
editMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editMenu)
editMenu.add_command(label="Cortar", command=cut)
editMenu.add_command(label="Copiar", command=copy)
editMenu.add_command(label="Pegar", command=paste)
# Texto a escribir
text = tk.Text(windows, height=400, width=400)
text.pack(pady=20)
# Abrir ventana
windows.mainloop()
