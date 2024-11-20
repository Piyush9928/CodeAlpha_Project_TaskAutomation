import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File type categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Others": []
}

def organize_files(directory):
    """Organize files in the specified directory."""
    if not os.path.exists(directory):
        messagebox.showerror("Error", "The specified directory does not exist!")
        return

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            folder_found = False

            for folder, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, destination_folder)
                    folder_found = True
                    break

            if not folder_found:
                # If no category matches, move to "Others"
                others_folder = os.path.join(directory, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, others_folder)

    messagebox.showinfo("Success", "Files organized successfully!")

def select_directory():
    """Open a directory selection dialog."""
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# GUI Setup
def main():
    root = tk.Tk()
    root.title("File Organizer")

    tk.Label(root, text="File Organizer", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Select a directory to organize its files.", font=("Arial", 12)).pack(pady=5)

    tk.Button(root, text="Choose Directory", command=select_directory, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

    tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white").pack(pady=10)

    root.geometry("400x200")
    root.mainloop()

if __name__ == "__main__":
    main()
