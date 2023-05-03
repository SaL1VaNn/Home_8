import os
import shutil

IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO_FILE = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENT = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC = ('MP3', 'OGG', 'WAV', 'AMR')
ARHIVES = ('ZIP', 'GZ', 'TAR')

images_list = []
video_list = []
doc_list = []
music_list = []
arhives_list = []
unknown_list = []

extention_list = []
unknown_extenstion = []


def sort_program(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            extension = item.split('.')[-1].upper()
            if extension in IMAGES:
                images_list.append(item)
            elif extension in VIDEO_FILE:
                video_list.append(item)
            elif extension in DOCUMENT:
                doc_list.append(item)
            elif extension in MUSIC:
                music_list.append(item)
            elif extension in ARHIVES:
                arhives_list.append(item)
            else:
                unknown_list.append(item)
        else:
            sort_program(item_path)


folder_path = "C:\\Users\\Admin\\Desktop"
sort_program(folder_path)


print("Images:", images_list)
print("Videos:", video_list)
print("Documents:", doc_list)
print("Music:", music_list)
print("Archives:", arhives_list)
print("Unknown files:", unknown_list)
