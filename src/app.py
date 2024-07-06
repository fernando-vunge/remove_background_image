import tkinter as tk
from tkinter import messagebox
from filechooser import choose_file
from rembg import remove
from PIL import Image
import os


file_name = "escolher imagem"
file_path = ''
file_chosen = False

def get_file_path():
    global file_name
    global file_path
    global file_chosen
    result = choose_file()
    if result[0]:
        file_name = str(result[1]).replace(" mode='r' encoding='cp1252'>","")
        file_name = file_name.replace("<_io.TextIOWrapper ","")
        file_name = file_name.replace("name='C:","")
        file_name = file_name.replace("'","")
        file_path = "C:" + file_name
        path_array = file_name.split("/") 
        file_name = path_array[len(path_array) - 1]
        file_chosen = True
        update_frame()

def remove_background():
    global file_name
    global file_chosen
    if file_name != "escolher imagem" :
        image_with_background = Image.open(file_path)
        image_without_background = remove(image_with_background)
        output_path = str(file_path).replace(file_name, "out.png")
        image_without_background.save(output_path)
        if os.path.exists(output_path) :
            messagebox.showinfo("processo finalizado", f"A imagem com fundo removido foi salva em:\n\n{output_path}")
        file_name = "escolher imagem"
        file_chosen = False
        update_frame()
        


def update_frame():
    for commponent in main_frame.winfo_children():
        commponent.destroy()

    label = tk.Label(main_frame,
        text="Removedor de fundo de imagens",
        bg="#0D3E66",
        fg="#ffffff",
        font=('Helvetica',14, 'bold')
    )

    chooisefile_frame = tk.Frame(
        main_frame, 
        bg="#ffffff", 
        bd=2, 
        width=190, 
        height=36
    )

    file_chooserbutton= tk.Button(
        main_frame,
        command=get_file_path,
        text=file_name, 
        bg='#0D3E66',
        fg='#ffffff',
        relief=tk.FLAT,
        padx=20,
        pady=5,
        bd=1,
        height=1,
        width=20
    )


    button = tk.Button(
        main_frame, 
        command=remove_background,
        text="Remover Fundo",
        bg='#000000',
        fg='#ffffff',
        font=('Consolas',10, 'bold'),
        relief=tk.RAISED,
        padx=20,
        pady=5,
        bd=0,
        height=1,
        width=10
    )

    label.place(x=40, y=25)
    chooisefile_frame.place(x=108, y=78)
    file_chooserbutton.place(x=110,y=80)
    if file_chosen:
        button.place(x=145, y=200)

main_frame = tk.Tk()
main_frame.title('rembg')
main_frame.geometry('400x300')
main_frame.resizable(False, False)
main_frame.configure(bg='#0D3E66')
update_frame()
main_frame.mainloop()