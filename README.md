Image Text Seeker

📜 Overview
Image Text Seeker is a Windows-based utility that allows users to search for specific text within a set of images. Utilizing Optical Character Recognition (OCR) powered by Tesseract, this tool scans images in a folder, identifies those containing the user-provided string, and copies them into a designated destination folder.

Whether you're working with images of documents, screenshots, or any kind of visual content, Image Text Seeker can help you quickly find images containing text without manually opening and scanning each one.

✨ Features
OCR Scanning: Uses Tesseract to read text from images.
Text Search: Allows users to search for specific text or digits in a set of images.
Automated Image Sorting: Copies the images that contain the searched text to a new folder.
Supports Multiple Formats: Works with .png, .jpg, and .jpeg images.
Easy-to-Use GUI: User-friendly interface built with Tkinter for seamless input and interaction.
🚀 How It Works
Select a Folder: Place all the images you want to scan in the SOURCE folder.
Input Search Text: Enter the text or numbers you're looking for using the graphical interface.
Results: The tool scans each image using OCR, and any image that contains the searched text is copied into the DESTINATION folder.
View Results: Open the DESTINATION folder to view the images containing the searched text.
🔧 Installation
To get started with Image Text Seeker, follow these steps:

Prerequisites
Python 3.x installed on your system.

Tesseract OCR installed. Download it from here.

Ensure Tesseract is installed in the default directory (C:\Program Files\Tesseract-OCR) or update the path accordingly in the script.

Required Python modules:

bash
Copy code
pip install pytesseract tkinter shutil os re
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/Image-Text-Seeker.git
cd Image-Text-Seeker
Setting Up Tesseract Path
Make sure to update the path to Tesseract in the Python script:

python
Copy code
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
Running the Program
bash
Copy code
python image_text_seeker.py
📂 Folder Structure
bash
Copy code
Image-Text-Seeker/
│
├── images/                  # SOURCE folder containing all images to be scanned
├── destination-images/       # DESTINATION folder for the resulting images
├── data.txt                 # Stores the input search string
├── image_text_seeker.py      # Main Python script for the application
└── README.md                 # Project Documentation
💻 Usage
Launch the App: Run the image_text_seeker.py script.
Enter Text: A GUI will pop up asking for the text you want to search for in the images.
Search: The program will scan all the images in the images folder.
View Results: The images containing the searched text will be copied to the destination-images folder.
🛠 Tech Stack
Python
Tesseract OCR
Tkinter (for GUI)
shutil (for file operations)
📸 Screenshots
Main Interface

Search Results

🤝 Contributors
This project was handcrafted by:

Abhay Raj Gupta
