# Hope U Guys Will Enjoy This
import concurrent
import functools
import shutil
import os
import re
import docx
import pdfplumber
import pytesseract
import cv2
import time
import concurrent.futures
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pickle
import tkinter as tk
from tkinter import filedialog

# -------------------------------------------------------------------------------------
# setting the tesseract_cmd to the installed path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def delete_destination():
    destination = "C:/ImageTextSeeker/destination-folder/"
    if os.path.exists(destination) and os.path.isdir(destination):
        shutil.rmtree(destination)


def create_destination():
    # deleting the pre-created destination folder & all the contents inside it using shutil module
    # add an if condition tpo make check for destination folder
    # creating the destination folder  at the specified directory
    directory = "destination-folder/"
    temp = "C:/ImageTextSeeker/"
    desti_path = os.path.join(temp, directory)
    os.mkdir(desti_path)


def is_matching_or_contained(search_string, word):
    return search_string == word or search_string in word


def is_string_matching_or_contained(string_to_check, word_list):
    filter_func = functools.partial(is_matching_or_contained, string_to_check)
    return any(filter(filter_func, word_list))


# --------------------------------------------------------------------
# BASIC MODE
# # PYTESSERACT WORKING STARTS FROM HERE
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     return threshold_img
#
#
# def extract_words_from_image(image_path):
#     # preprocessed_img = preprocess_image(image_path)
#     # text = pytesseract.image_to_string(preprocessed_img)
#     text = pytesseract.image_to_string(image_path)
#     words_list = text.split()  # Split the text into individual words
#     return words_list
#
# # ----------------------------------------------------------------------------------
# M.T. --->> M.P.

#
# def ocr_on_single_image(image_path):
#     # img = Image.open(image_path)
#     text = pytesseract.image_to_string(image_path)
#     text = text.split()
#     # print(text)
#     dic[os.path.basename(image_path)] = text
#     # return text
#
#
# def ocr_on_batch_images(image_paths, num_threads_per_batch=4):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = {executor.submit(ocr_on_single_image, image_path): image_path for image_path in image_paths}
#
#         batch_results = {}
#         for future in concurrent.futures.as_completed(futures):
#             image_path = futures[future]
#             try:
#                 text = future.result()
#                 text = text.lower()
#                 text = text.split()
#                 # print(text)
#                 # text.append(image_path)
#                 # print(image_path)
#                 # print(text)
#                 batch_results[os.path.basename(image_path)] = text
#             except Exception as e:
#                 print(f"OCR failed for image '{image_path}': {e}")
#
#     return batch_results
#
#
# def concurrent_multiprocess_and_threaded_ocr(image_paths, num_processes=4, num_threads_per_batch=4):
#     with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as process_executor:
#         futures = {process_executor.submit(ocr_on_batch_images, image_paths[start:start + num_threads_per_batch],
#                                            num_threads_per_batch): (image_paths[start:start + num_threads_per_batch])
#                    for start in range(0, len(image_paths), num_threads_per_batch)}
#
#         all_batch_results = {}
#         for future in concurrent.futures.as_completed(futures):
#             batch_results = future.result()
#             # print(batch_results)
#             # for image_name, extracted_words in batch_results.items():
#             #     print(f"Image: {image_name}\nExtracted Words: {extracted_words}\n")
#             #     print("------------------------------------------------------")
#             dic.update(batch_results)

# ----------------------------------------------------------------------------------
# M.P.
def extract_text(image_path):
    image_basename = os.path.basename(image_path)
    text = pytesseract.image_to_string(image_path)
    text = text.lower()
    return image_basename, text


def process_images(image_list):
    num_workers = min(len(image_list), os.cpu_count())  # Use the number of available CPU cores

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(extract_text, image_path): image_path for image_path in image_list}

        result_dict = {}
        for future in concurrent.futures.as_completed(futures):
            image_path = futures[future]
            image_basename, text = future.result()
            result_dict[image_basename] = text.split()

    return result_dict


def extract_text_from_pdf(pdf_paths):
    for pdf_path in pdf_paths:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)

            for page_num in range(num_pages):
                page = pdf.pages[page_num]
                text += page.extract_text()
        text = text.lower()
        words_list = text.split()
        # words_list.append(pdf_path)
        # print(pdf_path)
        # print(words_list)
        file = os.path.basename(pdf_path)
        dic[file] = words_list


def extract_text_from_docx(docx_paths):
    for docx_path in docx_paths:
        words_list = []
        doc = docx.Document(docx_path)
        for paragraph in doc.paragraphs:
            paragraph = paragraph.text.lower()
            # print(docx_path)
            # print(paragraph)
            word_from_docx = (paragraph.split())
            words_list.extend(word_from_docx)
        # words_list.append(docx_path)
        file = os.path.basename(docx_path)
        dic[file] = words_list


def get_source():
    return dic["source"]


def get_query():
    return dic["query"]


if __name__ == "__main__":

    # setting the tesseract_cmd to the installed path
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    # config = 'digits'

    folder_path = 'C:\ImageTextSeeker'
    if os.path.exists(folder_path) is False:
        os.makedirs(folder_path)

    # db_path = 'C:/ImageTextSeeker/save.p'
    # if os.path.exists(db_path) is False:
    #     dic = {}
    #     pickle.dump(dic, open('C:/ImageTextSeeker/save.p', "wb"))

    # fn for implementing json based datbase
    # dic = pickle.load(open('C:/ImageTextSeeker/save.p', "rb"))
    # dic["query"] = "i"
    delete_destination()


    def save_to_pickle():
        search_query = entry_query.get()
        directory_path = entry_directory.get()

        if not search_query or not directory_path:
            lbl_status.config(text="Please enter a valid search query and directory path.", fg="red")
            return

        try:
            with open('C:/ImageTextSeeker/search_data.pkl', 'rb') as file:
                data = pickle.load(file)
        except (FileNotFoundError, EOFError):
            data = {}

        data["source"] = directory_path
        data["query"] = search_query

        with open('C:/ImageTextSeeker/search_data.pkl', 'wb') as file:
            pickle.dump(data, file)

        lbl_status.config(text="Data saved successfully.", fg="green")
        root.destroy()


    root = tk.Tk()
    root.title("Search Data Input")
    root.geometry("500x300")

    # Configure the background color of the GUI
    root.configure(bg="#f0f0f0")

    # Labels
    lbl_query = tk.Label(root, text="Enter Search Query:", bg="#f0f0f0")
    lbl_query.pack(pady=5)

    # Entry for search query
    entry_query = tk.Entry(root)
    entry_query.pack(pady=5)

    # Labels
    lbl_directory = tk.Label(root, text="Choose Directory:", bg="#f0f0f0")
    lbl_directory.pack(pady=5)

    # Entry for directory
    entry_directory = tk.Entry(root)
    entry_directory.pack(pady=5)


    # Browse directory button
    def browse_directory():
        directory = filedialog.askdirectory()
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)


    btn_browse = tk.Button(root, text="Browse", command=browse_directory)
    btn_browse.pack(pady=5)

    # Save button
    btn_save = tk.Button(root, text="Enter", command=save_to_pickle)
    btn_save.pack(pady=10)

    # Status label
    lbl_status = tk.Label(root, text="", fg="green", bg="#f0f0f0")
    lbl_status.pack(pady=5)

    root.mainloop()
    # ========================================================================================

    start_time = time.time()

    # source = "C:\pk"
    dic = {}
    with open('C:/ImageTextSeeker/search_data.pkl', 'rb') as file:
        dic = pickle.load(file)

    source = dic["source"]
    destination_folder = 'C:/ImageTextSeeker/destination-folder'
    list_dict_keys = list(dic.keys())
    # print(source)
    image_paths = []
    pdf_paths = []
    docx_paths = []
    for root, _, files in os.walk(source):
        for file in files:
            if file not in list_dict_keys:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_paths.append(os.path.join(root, file))
                if file.lower().endswith('.pdf'):
                    pdf_paths.append(os.path.join(root, file))
                if file.lower().endswith('.docx'):
                    docx_paths.append(os.path.join(root, file))

    # # concurrent_multiprocess_and_threaded_ocr(image_paths, num_processes=4, num_threads_per_batch=4)
    # for image_path in image_paths:
    #     ocr_on_single_image(image_path)
    if len(image_paths) > 0:
        res = process_images(image_paths)
        dic.update(res)
    extract_text_from_pdf(pdf_paths)
    extract_text_from_docx(docx_paths)
    list_dict_keys = list(dic.keys())
    flag = 1

    # this commented part is for future , dont remove this ( going to be used for more of a generalised search )
    # for item in list_dict_keys:
    #     if item not in ("source", "query"):
    #         source_file = dic[item][-1]
    #         dic[item].pop()
    #         if is_string_matching_or_contained(get_query(), dic[item]):
    #             if flag == 1:
    #                 os.startfile(destination_folder)
    #                 flag = 0
    #             destination_file = os.path.join(destination_folder, item)
    #             shutil.copy(source_file, destination_file)
    #         dic[item].append(source_file)

    for root, _, files in os.walk(source):
        for file in files:
            if file in list_dict_keys:
                # source_file = dic[file][-1]
                source_file = os.path.join(root, file)
                # dic[file].pop()

                # print(dic[file])
                # print(dic["query"])
                # print(file)
                if any(dic["query"] in keyword for keyword in dic[file]):
                    # if is_string_matching_or_contained(get_query(), dic[file]):u
                    if flag == 1:
                        create_destination()
                        os.startfile(destination_folder)
                        flag = 0
                    # print(dic[file])
                    destination_file = os.path.join(destination_folder, file)
                    shutil.copy(source_file, destination_file)
                # dic[file].append(source_file)
    # print(list(dic.keys()))
    # pickle.dump(dic, open("save.p", "wb"))
    print(dic)
    with open('C:/ImageTextSeeker/search_data.pkl', 'wb') as file:
        pickle.dump(dic, file)
    process_time = time.time() - start_time
    # print(process_time)
