import os
import sys
import re

def txt_to_md(file_path):
	if not file_path.endswith(".txt"):
		print("Требуется файл с расширением txt")
		return
	content = ""
	with open(file_path, "r", encoding="utf-8") as file:
		content = file.read()
	new_content = content.replace(".\n", ".  \n") \
	.replace(":\n", ":  \n") \
	.replace("!\n", "!  \n") \
	.replace("?\n", "?  \n") \
	.replace(";\n", ";  \n") \
	.replace(",\n", ",  \n") \
	.replace("\n–", "  \n–") \
	.replace("\n***", ".\n\n\\***  ") \
	.replace("    ", "  ")
	
	file_md_path = file_path.replace(".txt", ".md")
	with open(file_md_path, "w", encoding="utf-8") as file_md:
		file_md.write(new_content)

if __name__ == "__main__":
	# Проверяем, что передан путь к файлу в командной строке
	if len(sys.argv) < 2:
		print("Не задан входящий параметр")
	else:
		file_path = sys.argv[1]
		txt_to_md(file_path)
