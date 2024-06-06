import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class AustriaImageDisplay:
    def __init__(self, master):
        self.master = master
        master.title("Display a Cute view")  # Changed title

        self.label = tk.Label(master, text="Click to see the view in Austria!")
        self.label.pack()

        self.show_button = tk.Button(master, text="Show Image", command=self.open_image)
        self.show_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.image_label = tk.Label(master)  # This label will display the image
        self.image_label.pack()

    def open_image(self):
        """
        This function opens a picture of a cute animal (replace with your image details)
        """
        image_path = "C:\\Users\\ofekv\\Desktop\\Nexy Py\\Chapter 6\\gui\\haifa.jpg" 
        if image_path:  # Check if a file was selected
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            print("Image loaded successfully!")


def main():
    root = tk.Tk()
    my_gui = AustriaImageDisplay(root)
    root.mainloop()


if __name__ == "__main__":
    main()
