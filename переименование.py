import os
import re
import string

folder_path = 'C:\\Users\\Юлия Ким\\Desktop\\Новая папка'  #  путь к папке с файлами

for filename in os.listdir(folder_path):
    if filename.endswith('.faa'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            first_line = file.readline().strip()

            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
            new_first_line = ''.join(c for c in first_line if c in valid_chars)
            new_filename = new_first_line + '_' + filename
            new_filename = re.sub(r'[<>:\"/\\|?*]', '', new_filename)

        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))