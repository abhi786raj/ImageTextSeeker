Image Text Seeker

📜 Overview :- 

Image Text Seeker is a simple and efficient Windows utility that scans a folder of images for specific user-provided text using Optical Character Recognition (OCR) powered by Tesseract. When text is found in an image, the tool automatically copies that image to a designated folder, helping users quickly locate relevant images without the need to manually open each one.

✨ Features :- 

OCR Scanning: Extracts text from images using Tesseract.
Text Search: Finds and matches specific text or numbers within images.
Automatic Sorting: Copies matching images to a separate folder for easy access.
Multi-Format Support: Works with .png, .jpg, and .jpeg image formats.
User-Friendly GUI: Simple interface using Tkinter for intuitive operation.

🚀 How It Works :-

Place Images: Store all images you want to scan in the SOURCE folder.
Input Text: Enter the text or numbers you want to search using the graphical interface.
Scan and Sort: The program scans each image, and if the text is found, the matching images are copied to the DESTINATION folder.
View Results: Open the DESTINATION folder to access the identified images.

🔧 Installation :-

  * Prerequisites :-
    
     * Python 3.x
     * Tesseract OCR (Download from: https://github.com/tesseract-ocr/tesseract). Install at C:\Program Files\Tesseract-OCR or update the path in the script if installed elsewhere.
    * Required Python Modules :- pytesseract, tkinter, shutil, os, re, bash
    
    * pip install pytesseract tkinter shutil os re
    
    * Clone the Repository :- https://github.com/abhi786raj/ImageTextSeeker.git
    
    * cd Image-Text-Seeker
    
    * Update Tesseract Path


  Ensure that the Python script points to the correct path for Tesseract:

    python
    Copy code :- pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    Running the Program :- python image_text_seeker.py

    
📂 Folder Structure :- 

    Image-Text-Seeker/
    │
    
    ├── images/                  # SOURCE folder containing images to scan
    
    ├── destination-images/       # DESTINATION folder for matching images
    
    ├── data.txt                 # Stores the input search text
    
    ├── image_text_seeker.py      # Main Python script
    
    └── README.md                 # Project Documentation


💻 Usage :- 

  Run the Script: Start the program by running image_text_seeker.py.
  
  Enter Text: Provide the text you wish to search for through the GUI.
  
  Search and Copy: The app scans images in the images folder and copies the ones containing the searched text to the destination-images folder.

🛠 Tech Stack :- 

  Python
  
  Tesseract OCR
  
  Tkinter (GUI)
  
  shutil (file handling)

  
🤝 Contributor :- Project crafted with care by Abhay Raj Gupta.
