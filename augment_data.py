import os 
import cv2 
import numpy as np 
import shutil

  
def change_color(image, target_color): 
    #Convert image to HSV 
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

    #Target color in HSV 
    target_hue = target_color[0] 
    target_saturation = target_color[1] 
    target_value = target_color[2] 

    hsv[:, :, 0] = (hsv[:, :, 0] + target_hue) % 180 
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] + target_saturation, 0, 255) 
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] + target_value, 0, 255) 
  
    #Back to BGR 
    result_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) 
    return result_image 

  
def augment_and_change_color(input_folder, output_folder, target_color): 
    copied_folder = os.path.join(input_folder, 'A', 'Train_Copy')
    shutil.copytree(os.path.join(input_folder, 'A', 'Train'), copied_folder) 
    
    if not os.path.exists(output_folder): 
        os.makedirs(output_folder) 

    for root, _, files in os.walk(os.path.join(input_folder, 'A', 'Train')): 
        for file in files: 
            if file.lower().endswith(('.png', '.jpg', '.jpeg')): 
                input_path = os.path.join(root, file) 
                output_path = os.path.join(output_folder, file) 
  
                image = cv2.imread(input_path)            
                #image = cv2.flip(image, 1)  # For both A and B train: horizontal flip 
                image = change_color(image, target_color) # Change the color            
                cv2.imwrite(output_path, image) 
  

if __name__ == "__main__": 
    input_folders = ["Dataset/Contemporary/", "Dataset/Edwardian", "Dataset/Georgian"]
    for input_folder in input_folders:
        output_folder = os.path.join(input_folder, 'A', 'Train_Aug')
        target_color = (30, 50, 20)  # Example target color in HSV format 

        augment_and_change_color(input_folder, output_folder, target_color) 
        
        