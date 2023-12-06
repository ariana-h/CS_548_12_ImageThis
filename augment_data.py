import os 
import cv2 
import numpy as np 
import shutil

def apply_jitter(image, jitter_factor):
    height, width, _ = image.shape
    
    jitter_x = int(width * jitter_factor)
    jitter_y = int(height * jitter_factor)

    delta_x = np.random.randint(-jitter_x, jitter_x + 1)
    delta_y = np.random.randint(-jitter_y, jitter_y + 1)
    
    translation_matrix = np.float32([[1, 0, delta_x], [0, 1, delta_y]])
    jittered_image = cv2.warpAffine(image, translation_matrix, (width, height))

    return jittered_image


def apply_random_noise(image, noise_factor):
    noise = np.random.normal(0, noise_factor, image.shape)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)

    return noisy_image

  
def augment_and_save(input_folder, output_folder, jitter_factor, noise_factor):
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder) 
        
    os.makedirs(output_folder) 

    for root, _, files in os.walk(os.path.join(input_folder, 'A', 'train')): 
        for file in files: 
            if file.lower().endswith(('.png', '.jpg', '.jpeg')): 
                input_path = os.path.join(root, file) 
                output_path = os.path.join(output_folder, file) 
  
                image = cv2.imread(input_path)            
                #image = cv2.flip(image, 1)  # For both A and B train: horizontal flip 
                
                #image = apply_jitter(image, jitter_factor)
                #image = apply_random_noise(image, noise_factor)
                image = apply_jitter(image, jitter_factor)
                image = apply_random_noise(image, noise_factor)
                          
                cv2.imwrite(output_path, image) 
  

if __name__ == "__main__": 
    input_folders = ["Dataset/Contemporary/", "Dataset/Edwardian", "Dataset/Georgian"]
    
    for input_folder in input_folders:
        copied_folder = os.path.join(input_folder, 'A', 'train_copy')
        
        if not os.path.exists(copied_folder):
            #os.makedirs(copied_folder) 
            shutil.copytree(os.path.join(input_folder, 'A', 'train'), copied_folder) 
        
        output_folder = os.path.join(input_folder, 'A', 'train_aug')
        jitter_factor = 0.1
        noise_factor = 15
        
        augment_and_save(input_folder, output_folder, jitter_factor, noise_factor) 
        
        