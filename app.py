import tkinter as tk
from filechooser import choose_file

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
        print(file_name)
        print(file_path)
        update_frame()

def remove_background():
    pass


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