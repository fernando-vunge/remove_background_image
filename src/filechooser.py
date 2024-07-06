from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfile(
        title="escolher imagem",
        filetypes=(("imagens png", "*.png"),("imagens jpg", "*.png"))
    )
    if file_path:
        return [True, file_path]
    else:
        return [False]
    