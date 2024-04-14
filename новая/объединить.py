import os

folder = "C:\\Users\\Юлия Ким\\Desktop\\Новая папка"
files = os.listdir(folder)


output_path = os.path.join(folder, "C:\\Users\\Юлия Ким\\Desktop\\Новая папка\\Новый текстовый документ.txt")

with open(output_path, "w") as output_file:
    for file_name in files:
        if file_name.endswith(".faa"):
            file_path = os.path.join(folder, file_name)
            with open(file_path, "r") as input_file:
                output_file.write(input_file.read())

print("Файлы объединены")

