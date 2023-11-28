import os

file_paths = ["Dataset/Contemporary/A/Train", "Dataset/Contemporary/B/Train", 
              "Dataset/Edwardian/A/Train", "Dataset/Edwardian/B/Train", 
              "Dataset/Georgian/A/Train", "Dataset/Georgian/B/Train"]

for file_path in file_paths:
    files = os.listdir(file_path)
    for f in files:
        if '.jpg' in f:
            newname = f.split('_')[0]
            newname = newname + '.jpg'
            os.rename(os.path.join(file_path,f), os.path.join(file_path,newname))
