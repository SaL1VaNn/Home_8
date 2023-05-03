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


def sort_progtam(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            extention = item.split('.')[-1].upper()
            if extention not in extention_list:
                extention_list.append(extention)
