import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from stat import S_IWRITE, S_IREAD, S_IEXEC

def create_directory(path):
    os.makedirs(path, exist_ok=True)
    messagebox.showinfo("Success", f"Directory '{path}' created.")

def list_directory(path):
    if os.path.exists(path):
        contents = "\n".join(os.listdir(path))
        messagebox.showinfo("Directory Contents", f"Contents of '{path}':\n{contents}")
    else:
        messagebox.showerror("Error", f"Path '{path}' does not exist.")

def move_item(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
        messagebox.showinfo("Success", f"Moved '{src}' to '{dst}'.")
    else:
        messagebox.showerror("Error", f"Source '{src}' does not exist.")

def rename_item(src, dst):
    if os.path.exists(src):
        os.rename(src, dst)
        messagebox.showinfo("Success", f"Renamed '{src}' to '{dst}'.")
    else:
        messagebox.showerror("Error", f"Source '{src}' does not exist.")

def copy_item(src, dst):
    if os.path.exists(src):
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)
        messagebox.showinfo("Success", f"Copied '{src}' to '{dst}'.")
    else:
        messagebox.showerror("Error", f"Source '{src}' does not exist.")

def delete_item(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        messagebox.showinfo("Success", f"Deleted '{path}'.")
    else:
        messagebox.showerror("Error", f"Path '{path}' does not exist.")

def change_attributes(path, read_only=False, execute=False):
    if os.path.exists(path):
        mode = S_IREAD
        if not read_only:
            mode |= S_IWRITE
        if execute:
            mode |= S_IEXEC
        os.chmod(path, mode)
        messagebox.showinfo("Success", f"Changed attributes for '{path}'.")
    else:
        messagebox.showerror("Error", f"Path '{path}' does not exist.")

def search_items(path, name):
    if os.path.exists(path):
        results = []
        for root, dirs, files in os.walk(path):
            for item in dirs + files:
                if name in item:
                    results.append(os.path.join(root, item))
        messagebox.showinfo("Search Results", "\n".join(results) if results else "No items found.")
    else:
        messagebox.showerror("Error", f"Path '{path}' does not exist.")

def set_permissions(path, permissions):
    if os.path.exists(path):
        os.chmod(path, permissions)
        messagebox.showinfo("Success", f"Permissions for '{path}' set to '{oct(permissions)}'.")
    else:
        messagebox.showerror("Error", f"Path '{path}' does not exist.")

def create_file(path):
    with open(path, 'w') as f:
        f.write("")
    messagebox.showinfo("Success", f"File '{path}' created.")

def read_file(path):
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'r') as f:
            contents = f.read()
        messagebox.showinfo("File Contents", f"Contents of '{path}':\n{contents}")
    else:
        messagebox.showerror("Error", f"File '{path}' does not exist.")

def edit_file(path, content):
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'a') as f:
            f.write(content)
        messagebox.showinfo("Success", f"Content added to '{path}'.")
    else:
        messagebox.showerror("Error", f"File '{path}' does not exist.")

def choose_path(title):
    return filedialog.askdirectory(title=title)

def choose_file(title):
    return filedialog.askopenfilename(title=title)

def main():
    def on_create_directory():
        path = filedialog.askdirectory(title="Select Directory")
        if path:
            create_directory(path)

    def on_list_directory():
        path = filedialog.askdirectory(title="Select Directory")
        if path:
            list_directory(path)

    def on_move_item():
        src = choose_file("Select Source")
        dst = filedialog.askdirectory(title="Select Destination")
        if src and dst:
            move_item(src, dst)

    def on_rename_item():
        src = choose_file("Select File/Folder to Rename")
        if src:
            dst = filedialog.asksaveasfilename(title="Enter New Name")
            if dst:
                rename_item(src, dst)

    def on_copy_item():
        src = choose_file("Select Source")
        dst = filedialog.askdirectory(title="Select Destination")
        if src and dst:
            copy_item(src, os.path.join(dst, os.path.basename(src)))

    def on_delete_item():
        path = choose_file("Select File/Folder to Delete")
        if path:
            delete_item(path)

    def on_change_attributes():
        path = choose_file("Select File/Folder")
        if path:
            read_only = messagebox.askyesno("Set Read-Only?", "Do you want to set this item as read-only?")
            execute = messagebox.askyesno("Set Executable?", "Do you want to set this item as executable?")
            change_attributes(path, read_only, execute)

    def on_create_file():
        path = filedialog.asksaveasfilename(title="Enter File Name")
        if path:
            create_file(path)

    def on_read_file():
        path = choose_file("Select File to Read")
        if path:
            read_file(path)
    root = tk.Tk()
    root.title("File Manager")

    tk.Button(root, text="Create Directory", command=on_create_directory).pack(fill="x")
    tk.Button(root, text="List Directory", command=on_list_directory).pack(fill="x")
    tk.Button(root, text="Move Item", command=on_move_item).pack(fill="x")
    tk.Button(root, text="Rename Item", command=on_rename_item).pack(fill="x")
    tk.Button(root, text="Copy Item", command=on_copy_item).pack(fill="x")
    tk.Button(root, text="Delete Item", command=on_delete_item).pack(fill="x")
    tk.Button(root, text="Change Attributes", command=on_change_attributes).pack(fill="x")
    tk.Button(root, text="Create File", command=on_create_file).pack(fill="x")
    tk.Button(root, text="Read File", command=on_read_file).pack(fill="x")
    tk.Button(root, text="Exit", command=root.quit).pack(fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()
