import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def enhance_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename()

    # Check if a file was selected
    if file_path:
        # Load the image using OpenCV
        original_image = cv2.imread(file_path)

        # Apply image enhancement here (you can customize this part)

        # For demonstration, let's apply a simple grayscale filter
        enhanced_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Create a dark-themed GUI window
        dark_theme = ttk.Style()
        dark_theme.configure('TButton', foreground='white', background='gray')
        dark_theme.configure('TLabel', foreground='white', background='gray')
        dark_theme.configure('TFrame', background='gray')

        # Create a new window
        window = tk.Tk()
        window.title("AI Image Enhancer")
        window.configure(bg='gray')

        # Display the original image
        original_label = ttk.Label(window, text="Original Image", style="TLabel")
        original_label.pack()
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        original_photo = cv2.imencode('.png', original_image)[1].tobytes()
        original_photo = tk.PhotoImage(data=original_photo)
        original_label.img = original_photo  # Keep a reference to the PhotoImage
        original_label.config(image=original_photo)

        # Display the enhanced image
        enhanced_label = ttk.Label(window, text="Enhanced Image", style="TLabel")
        enhanced_label.pack()
        enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
        enhanced_photo = cv2.imencode('.png', enhanced_image)[1].tobytes()
        enhanced_photo = tk.PhotoImage(data=enhanced_photo)
        enhanced_label.img = enhanced_photo  # Keep a reference to the PhotoImage
        enhanced_label.config(image=enhanced_photo)

        # Run the GUI
        window.mainloop()

if __name__ == "__main__":
    enhance_image()
