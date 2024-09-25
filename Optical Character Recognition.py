import os
import shutil
import re
import pytesseract
from tkinter import *
from tkinter import messagebox

# Set path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Global configuration for Tesseract (optional, for digits only)
config = 'digits'

# GUI Setup
def initialize_gui():
    root = Tk()
    root.geometry("900x500")
    root.title("Text Detection In Gallery Images")

    # GUI Labels and Entry fields
    Label(root, text="Text Detection In Gallery Images", width=40, font=("Helvetica 14 bold", 20)).place(x=120, y=53)
    Label(root, text="Enter the text you want to search", width=45, font=("bold", 13)).place(x=170, y=165)
    
    entry_value = StringVar()
    entry = Entry(root, textvariable=entry_value)
    entry.place(x=500, y=165)
    
    Button(root, text='SEARCH', width=22, bg='blue', fg='white', command=lambda: save_search_query(entry, root)).place(x=360, y=270)

    Label(root, text="NOTE:", width=10, font=("bold", 13)).place(x=10, y=400)
    Label(root, text="* All the images must be in the SOURCE folder.", width=59, font=("bold", 11)).place(x=10, y=430)
    Label(root, text="* Searched images are stored in the DESTINATION folder.", width=50, font=("bold", 11)).place(x=10, y=460)

    root.mainloop()

# Validate input and save search string to a file
def save_search_query(entry, root):
    search_string = entry.get().strip()
    if validate_input(search_string):
        with open(r'C:\Optical-Character-Recognition\data.txt', 'w') as text_file:
            text_file.write(search_string.lower())
        root.destroy()
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid string (alphabetic or numeric).")
        entry.delete(0, 'end')

# Input validation
def validate_input(s):
    pattern = re.compile("^[a-zA-Z0-9]+$")
    return bool(pattern.match(s))

# OCR processing and copying matching images
def process_images():
    try:
        source_folder = r'C:/Optical-Character-Recognition/images'
        destination_folder = r'C:/Optical-Character-Recognition/destination-images/'

        # Clear and recreate destination folder
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
        os.mkdir(destination_folder)

        # Load search string
        with open(r'C:/Optical-Character-Recognition/data.txt', 'r') as file:
            search_string = file.read().strip()

        # Process each image in source folder
        for image_file in os.listdir(source_folder):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(source_folder, image_file)
                try:
                    # Extract text using OCR
                    ocr_data = pytesseract.image_to_string(image_path).lower()
                    if search_string in ocr_data:
                        # Copy image to destination if match is found
                        shutil.copy(image_path, destination_folder)
                        print(f"Match found: {image_file}")
                except Exception as e:
                    print(f"Error processing {image_file}: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Main function to run the app
if __name__ == '__main__':
    initialize_gui()
    process_images()
