import os


def load_txt_files_from_folder(folder_path):
  
    if not os.path.exists(folder_path):
        raise ValueError(f"The specified folder path does not exist: {folder_path}")

    
    if not os.path.isdir(folder_path):
        raise ValueError(f"The specified path is not a folder: {folder_path}")

     all_file_contents = set()

   
    for filename in os.listdir(folder_path):
               if filename.endswith('.txt'):
                      file_path = os.path.join(folder_path, filename)

                     with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                                      all_file_contents.add(line.strip())

    return all_file_contents


def merge_files_into_new_file(folder_path, output_file_path):
  
    contents = load_txt_files_from_folder(folder_path)

       contents_list = list(contents)

 
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

      with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in contents_list:
            file.write(line + '\n')

    print(f"All files have been merged into {output_file_path}")



folder_path = 'D:\\PY\\datasets (2)\\datasets\\no' 
output_file_path = 'D:\\PY\\3.txt'  try:
    merge_files_into_new_file(folder_path, output_file_path)
except ValueError as e:
    print(e)