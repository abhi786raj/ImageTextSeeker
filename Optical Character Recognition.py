import shutil
import os
import re
import pytesseract as pytesseract

# Hope U Guys Will Enjoy This '
# handcrafted By Abhay, Akanksha, Udita & Harsh

# importing the required modules as per the plan execution !!
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

# setting the tesseract_cmd to the installed path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
config = 'digits'

# INITIAL GUI CODE USING TKINTER WITH ASKINPUT AS A FUNCTION TO CHECK FOR VALID STRING

# initializing root as Tk() & setting up the geometry & color of GUI Window
root = Tk()
root.geometry("900x500")
root.title("Text Detection In Gallery Images")
#root['bg'] = '#ffbf00'

# bool function to validate the Input String & prompting by
# Invalid Window if the input string is found to be incorrecct !!
def ask_input(s):
    if(s==''):
        return 0
    # using regular expression to check if our input string has all characters are alhabets or not
    pattern = re.compile("^[a-zA-Z]+$")
    if pattern.match(s):
        return 1
    else:
        if s.isdigit() == 0:
            # message box will give a popup if the given string is neither an alphabetical nor numeric
            messagebox.showwarning("Invalid QUERY","TRY AGAIN")
            return 0
        else:
            # returns 1, if the input string has all digits
            return 1

def save_in_file():
    # grabs the entry from search bar by using get function
    s = entry.get()
    if(ask_input(s)):
        # converts all letters of input string to lowercase for optimized word searching
        s = s.lower()
        # open pre-created text file
        text_file = open('C:\Optical-Character-Recognition\data.txt', "w")
        # write string to the above text file using write function
        # ( write function will automatically deletes the pre-stored data in our text file & rewrites it from scratch)
        n = text_file.write(s)
        # close file, using close function by saving the text file
        text_file.close()
        # as soon as the user provides an input & it gets validated using ask_input function,
        # destroy the GUI WINDOW by using destroy funtion
        root.destroy()
    else:
        # clears the entry bar by deleting the invalid text
        # delete function takes two entries, the 1st one is for starting of index as zero-based
        # indexing & the other one takes the ending upto which, one wants to delete the text
        entry.delete(0,'end')


label_0 = Label(root, text="Text Detection In Gallery Images",width=40,font=("Helvetica 14 bold", 20))
label_0.place(x=120,y=53)

label_1 = Label(root, text="Enter the text you want to search",width=45,font=("bold", 13))
label_1.place(x=170,y=165)
entryvalue=StringVar()

entry = Entry(root,textvariable=entryvalue)
entry.place(x=500,y=165)

Button(root, text='SEARCH',width=22,bg='blue',fg='white',command=save_in_file).place(x=360,y=270)

label_2 = Label(root, text="NOTE:",width=10,font=("bold", 13))
label_2.place(x=10,y=400)
label_3 = Label(root, text="* All the images that needs to be detected should be in the SOURCE Folder.",width=59,font=("bold", 11))
label_3.place(x=10,y=430)
label_4 = Label(root, text="* The searched images are Stored in the DESTINATION Folder.",width=50,font=("bold", 11))
label_4.place(x=10,y=460)


root.mainloop()

# deleting the pre-created destination folder & all the contents inside it using shutil module
source = "C:/Optical-Character-Recognition/images"
destination = "C:/Optical-Character-Recognition/destination-images/"
shutil.rmtree(destination)

#creating the destination folder  at the specified directory
directory = "destination-images/"
temp = "C:/Optical-Character-Recognition/"
path = os.path.join(temp, directory)
os.mkdir(path)

# to open a file explorer dialogue-box for the searched images at destination folder
os.startfile("C:\Optical-Character-Recognition\destination-images")

# open text file in read mode
text_file = open('C:\Optical-Character-Recognition\data.txt', "r")
# read whole file to a string
data = text_file.read()
# close file
text_file.close()

#copying the data string to variable s
s = data

# PYTESSERACT WORKING STARTS FROM HERE

for images in os.listdir(source):

    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        img = source + '\\' + images

        # EXTRACTING particular DATA FROM THE IMAGES
        lines = []
        results = pytesseract.image_to_data(img)
        for id, line in enumerate(results.splitlines()):
            if id != 0:
                line = line.split()
                if len(line) == 12:
                    lines.append(line)

        matches = []
        for line in lines:
            for word in line[-1:]:
                matches.append(word)

        matches_lower = []
        # pytesseract work ends here

        # Code to check whether string contains only number
        for words in matches:
            pattern = re.compile("^[a-zA-Z]+$")
            if pattern.match(words):
                matches_lower.append(words.lower())
            else:
                matches_lower.append(words)

        filter_object = filter(lambda a: s in a, matches_lower)
        if len(list(filter_object)) != 0:

            #MARKING THE IMAGE PART WHICH CONTAINS THE DATA
            # results = pytesseract.image_to_boxes(img)
            # ih, iw, ic = img.shape()
            # for box in results.splitlines():
            #     box = box.split(' ')
            #     print(box)
            #     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
            #     cv2.rectangle(img, (x, ih - y), (w, ih - h), (0, 255, 0), 2)
            #     cv2.putText(img, box[0], (x, ih - h), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

            original = r'C:\Optical-Character-Recognition\images' + '\\' + images
            print(original)
            target = r'C:/Optical-Character-Recognition/destination-images/' + images
            shutil.copyfile(original, target)

