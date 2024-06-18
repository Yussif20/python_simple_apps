import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")

        self.text_area = tk.Text(root, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill='x')

        self.open_button = tk.Button(self.button_frame, text="Open File", command=self.open_file)
        self.open_button.pack(side='left')

        self.save_button = tk.Button(self.button_frame, text="Save As", command=self.save_as)
        self.save_button.pack(side='left')

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"),
                                                          ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Open File", f"Failed to read file\n{e}")

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Save As", f"Failed to save file\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    root.mainloop()
