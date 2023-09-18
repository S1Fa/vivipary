import os
import re
import argparse

def rename_files_in_dir(directory_path):

	# 将相对路径转换为绝对路径
	directory_path = os.path.abspath(directory_path)

	if not os.path.exists(directory_path):
		print(f'directory {directory_path} not exist')
		return

	try:
		os.chdir(directory_path)
		for file in os.listdir(directory_path):
			new_name = re.sub('_pro|_cds', '', file)
			os.rename(file, new_name)
			print(f'rename {file} as {new_name}')

	except Exception as e:
		print(f"There is an error: {e} when renaming file names")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="重命名指定目录中的所有文件")

	parser.add_argument("directory", type=str, help="要重命名文件的目录路径")

	args = parser.parse_args()
	rename_files_in_dir(args.directory)

