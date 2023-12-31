import os 
import shutil 

def combine_folders(train_aug, destination_folder): 
    if not os.path.exists(destination_folder): 
        os.makedirs(destination_folder) 

    for root, _, files in os.walk(train_aug): 
        for file in files: 
            source_path = os.path.join(root, file) 
            destination_path = os.path.join(destination_folder, file) 

            counter = 1 
            while os.path.exists(destination_path): 
                filename, extension = os.path.splitext(file) 
                new_filename = f"{filename}{extension}"
                destination_path = os.path.join(destination_folder, new_filename) 
                counter += 1 

            shutil.copy2(source_path, destination_path) 
    
    
def double_images(train, destination_folder): 
    if not os.path.exists(destination_folder): 
        os.makedirs(destination_folder) 

    for root, _, files in os.walk(train): 
        for file in files: 
            source_path = os.path.join(root, file) 
            destination_path = os.path.join(destination_folder, file) 

            counter = 1 
            while os.path.exists(destination_path): 
                filename, extension = os.path.splitext(file) 
                new_filename = f"0{filename}{extension}"
                destination_path = os.path.join(destination_folder, new_filename) 
                counter += 1 

            shutil.copy2(source_path, destination_path) 
    
    
if __name__ == "__main__": 
    train_paths = ["Dataset/Contemporary/", "Dataset/Edwardian/", "Dataset/Georgian/"]
    for input in train_paths:
        train_aug = os.path.join(input, 'A', 'train_aug')
        destination_folder = os.path.join(input, 'A', 'train')

        # Add a 0 before each filename in Train_Aug/ 
        for root, _, files in os.walk(train_aug): 
            for file in files: 
                source_path = os.path.join(root, file) 
                filename, extension = os.path.splitext(file) 
                new_filename = f"0{filename}{extension}" 
                new_path = os.path.join(root, new_filename) 
                os.rename(source_path, new_path) 
                
        combine_folders(train_aug, destination_folder) 
                
                
        train = os.path.join(input, 'B', 'train')
        destination_folder = train
  
        double_images(train, destination_folder) 
        


        


    