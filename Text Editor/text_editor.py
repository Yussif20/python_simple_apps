import tkinter as tk

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

window = tk.Tk()

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files", ".txt"),("All Files", ".")])
    if not file_path:return 
    print(file_path)
    txt_edit.delete(1.0, tk.END)
    with open(file_path, "r", encoding='utf-8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
def save_file():
      txt_edit.update() 
      file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".")])
      if not file_path: return
      with open(file_path, "w", encoding='utf-8') as output_file:
        output_file.write(txt_edit.get(1.0, tk.END))

window.title("Text editor")
window.minsize(width=800, height=600)
window.rowconfigure(0,minsize=600)
window.columnconfigure(1,minsize=600)

txt_edit = tk.Text(master=window)
frame_buttons = tk.Frame(master=window,relief=tk.RAISED )
btn_open = tk.Button(master=frame_buttons,text="Open file",command=open_file)
btn_save = tk.Button(master=frame_buttons,text="Save as",command=save_file)

btn_open.grid(column=0, row=0 ,sticky="ew")
btn_save.grid(column=0, row=1 ,sticky="ew" )
frame_buttons.grid(column=0, row=0 ,sticky="ns" )
txt_edit.grid(column=1, row=0,sticky="nsew")


window.mainloop()