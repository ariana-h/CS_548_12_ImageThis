import os

file_paths = ["Dataset/Contemporary/A/train", "Dataset/Contemporary/B/train", 
              "Dataset/Edwardian/A/train", "Dataset/Edwardian/B/train", 
              "Dataset/Georgian/A/train", "Dataset/Georgian/B/train"]

for file_path in file_paths:
    files = os.listdir(file_path)
    for f in files:
        if '.jpg' in f:
            newname = f.split('_')[0]
            newname = newname + '.jpg'
            os.rename(os.path.join(file_path,f), os.path.join(file_path,newname))
