# Image-to-Image Translation with Conditional Adversarial Networks

## Overview
This is the code repository for the paper “Image-to-Image Translation: Segmentation Labels to Building Facades using Architectural Styles” as part of the CS 548-12 course taught by Dr. Michael J. Reale at SUNY Polytechnic in Fall 2023.

**Contributors:** Ariana Huhko, Jaime Morse 

**Description:** We are using a pix2pix model to perform image-to-image translation of facade segmentation labels into building facade images based on their architecture styles. The original Facades Dataset we used from Kaggle was modified by classifying the training images based on the architecture styles of the buildings. By doing this, we were able to split the data into three architectural styles with the intention to fix issues seen using the original dataset such as color and style differences between the input labels and the outputted building facade images.
 
## Data
### Instructions to download and prepare the data
The original dataset is located: https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset

The modified dataset is in the Dataset folder of this repository. There are three subfolders which represent the three different architectural styles chosen. Each architectural style will be run separately.

#### Architectural Styles:

![](https://lh7-us.googleusercontent.com/hlam0QGf9KcdIBXQRWpATM936C-tpZhWR6H2FX1Gu-hewwJEdAiGp7GnW9CXvUC_qxtelByw-R0V9Q42Xh4BBpzflIXvWP2zCypHor5PTM2wEJSSWxIafMmFR6KSHpInkJrIQZK0d_4_E7pmf_eQq8I)


#### File Hierarchy:

![](https://lh7-us.googleusercontent.com/lN-XHqsWWZW5FevhYJ2ebbbw_qaiZe0thYHy3pr5pdJzJl0DiD3HE6tC1VGxSlrWUmLa7HfqOjG5cMzx6eX4Gt8Nx21uH5a5uY6Da-Q4lf7BgCXpxTOq862zHl4XD0t2quo2EFYa2SygSqzoW8RxHGQ)

### Prepare data
These next two scripts can be run once. They do not have to be run for every architectural style individually.

Run the `augment_data.py` script first to increase the amount of training data; this script augments the building facades to add random jitter and random noise. 

Then, run the `combine_A_aug_and_train.py` script to combine the original training data and the augmented training data into one folder.

### Generating Pairs
Use the provided python script in the CG folder to generate training data in the form of pairs of images {A,B}, where A and B are {segmentation labels, building facades}.


Use the architectural style dataset folders within subfolders `A` and `B` {Contemporary, Edwardian, Georgian}. 


Corresponding images in a pair {A,B} have the same size and have the same filename, e.g., `/path/to/data/A/train/1.jpg` is considered to correspond to `/path/to/data/B/train/1.jpg`. The `rename_train_images.py` script has already been run to remove the  `"_A"` and `"_B"` from the original dataset we downloaded. The images are all be 256x256.


To concatenate the A and B images to match the model requirements, use the following script via the command line for each architectural style dataset.


#### In a bash terminal run:
`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Contemporary/A --fold_B Dataset/Contemporary/B --fold_AB Dataset/Contemporary --no_multiprocessing`

#### Output would show: 
>[fold_A] =  Dataset/Contemporary/A
[fold_B] =  Dataset/Contemporary/B
[fold_AB] =  Dataset/Contemporary
[num_imgs] =  1000000
[use_AB] =  False
[no_multiprocessing] =  False
split = test, use 18/18 images
split = test, number of images = 18
split = train, use 87/87 images
split = train, number of images = 87
split = train_aug, use 0/0 images
split = train_aug, number of images = 0
split = train_copy, use 0/0 images
split = train_copy, number of images = 0


#### From this:


![](https://lh7-us.googleusercontent.com/6mKijR9LbzrayXcDLK8Sg9Z-CoYKcg4ZDTSbw6ak8meS76XC_V47pVxAMLhNhJQvL9AFj3h79Lf9-HVHFupYtyhxd8KwVk6JkJ0Xni4mruhscLs6UUFdjzLQXnS7jLWssHarGmOQWAd9_qorE7sovGM)


#### To this:

![](https://lh7-us.googleusercontent.com/rgcVo4FIeNz_3W-hFFxrEeTdhuTO_mJfxLaxE0cd-GydCHH4ghWjYOVtOWoFwwAjJ_2lDU0afgFKYutXsDXWni84xO6RBDWU8IzMw_1q4nsj2AYTc-jV3BpQx5-ZBtJoGS9UJp-NvzpoJRwL7B1nNCw)


#### Run these commands to combine the other two datasets:
`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Edwardian/A --fold_B Dataset/Edwardian/B --fold_AB Dataset/Edwardian --no_multiprocessing`

`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Georgian/A --fold_B Dataset/Georgian/B --fold_AB Dataset/Georgian --no_multiprocessing`


## Models
Use the CG folder in this repository to access the necessary models. This project uses the pix2pix model.

Checkpoints and resulting images from each of the models can be downloaded from OneDrive using the following link: https://sunypoly-my.sharepoint.com/:f:/g/personal/huhkoa2_sunypoly_edu/EoU1MC9Mjo1Ho4pvX9t2R2QBfu_POXRr4kIiZO5CooiPoA?e=ZWTKMJ

## Software Dependencies
• Linux

• Python 3

• NVIDIA GPU + CUDA CuDNN

• PyTorch 2.1.0+cpu

## Running the Project
Clone this repo using `git clone git@github.com:ariana-h/CS_548_12_ImageThis.git`

### Running the scripts
As a recap, run these scripts in order:

`python augment_data.py`

`python combine_A_aug_and_train.py`

Then use the command line to run:

`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Contemporary/A --fold_B Dataset/Contemporary/B --fold_AB Dataset/Contemporary`

`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Edwardian/A --fold_B Dataset/Edwardian/B --fold_AB Dataset/Edwardian`

`python CG/datasets/combine_A_and_B.py --fold_A Dataset/Georgian/A --fold_B Dataset/Georgian/B --fold_AB Dataset/Georgian`


### Train the model(s)
Run the train scripts for each corresponding architecture style. These scripts provide arguments to the Pix2Pix model located in the CG directory, and will create checkpoints to resume training if necessary. The output of the training scripts should include the epoch number, the amount of time it took per epoch, and the losses.

`python Contemporary_train.py`

`python Edwardian_train.py`

`python Georgian_train.py`

#### Output: 
The model will be printed out before the training occurs.
>(epoch: 1, iters: 100, time: 0.037, data: 0.098) G_GAN: 2.193 G_L1: 30.763 D_real: 0.369 D_fake: 0.140 
End of epoch 1 / 200     Time Taken: 7 sec
learning rate 0.0002000 -> 0.0002000
(epoch: 2, iters: 26, time: 0.038, data: 0.001) G_GAN: 2.425 G_L1: 28.517 D_real: 0.208 D_fake: 0.269 
(epoch: 2, iters: 126, time: 0.033, data: 0.003) G_GAN: 3.713 G_L1: 40.982 D_real: 0.265 D_fake: 0.020 
End of epoch 2 / 200     Time Taken: 4 sec
learning rate 0.0002000 -> 0.0002000
(epoch: 3, iters: 52, time: 0.184, data: 0.002) G_GAN: 2.706 G_L1: 42.334 D_real: 0.051 D_fake: 0.085 
(epoch: 3, iters: 152, time: 0.037, data: 0.002) G_GAN: 2.939 G_L1: 42.566 D_real: 0.108 D_fake: 0.105 
End of epoch 3 / 200     Time Taken: 5 sec
learning rate 0.0002000 -> 0.0002000
(epoch: 4, iters: 78, time: 0.035, data: 0.003) G_GAN: 3.324 G_L1: 49.385 D_real: 0.012 D_fake: 0.153 
End of epoch 4 / 200     Time Taken: 4 sec
learning rate 0.0002000 -> 0.0002000
(epoch: 5, iters: 4, time: 0.037, data: 0.002) G_GAN: 2.787 G_L1: 35.735 D_real: 0.041 D_fake: 0.084 
(epoch: 5, iters: 104, time: 0.191, data: 0.000) G_GAN: 2.509 G_L1: 41.648 D_real: 0.063 D_fake: 0.397 
saving the model at the end of epoch 5, iters 870
End of epoch 5 / 200     Time Taken: 8 sec
learning rate 0.0002000 -> 0.0002000
…


### Test the model(s)
Run the evaluate script for each corresponding architecture style. These scripts provide arguments to the Pix2Pix model located in the CG directory. The resulting images will be shown in a new folder named results.

`python Contemporary_evaluate.py`

`python Edwardian_evaluate.py`

`python Georgian_evaluate.py`

An example of the outputs for each model is shown below with the generated images, the real segmentation label, and the real building facade:

**Contemporary** 

![](https://lh7-us.googleusercontent.com/Ket_ZdwvgSWPtBgq3ZtV8rZU-hUEkJr6UHqt-r083JJ_TwGWSQygfu2RWrk4b67dZwOqVKm-nbDrC3HdvsPIfetbliuI93fl3m5BUB_keSH-sa_rVv1m5tGsfz0AduUuuPj7sMHkZgQlsbNVFHFu0fc)

**Edwardian**

![](https://lh7-us.googleusercontent.com/rAvgwuslfyYgl1GrX6ywpzIrgEytra8btLKZU5JZbYf5bw0fPT4fBG4u1Jrf7Hk4d6w22-EA6a1BsWvhRF53r1bsKtJ8YqmITe0bzWBdX03-xhXFkbytcDtj68xML5_E19WQ5RrBSUDyRkr6dPhACJs)

**Georgian**

![](https://lh7-us.googleusercontent.com/GVXo81R69JKRKI-ZDLcsyVFzHPpaEEEVyD-tsux4sxd0Jk7Z8v0TCCve9zVciBJfbFFU8VvO-MCDJpiP8ClJ9-5lGdf7qTZY-IHcFTX9Sb1rsjhhjxlvu7YGx_46yRuHlKavUjoQ-98_5IaHh9G32tw)

## Getting the original dataset from Kaggle instead of using the repository's
The original dataset that was used for CycleGAN was taken from: https://www.kaggle.com/datasets/balraj98/facades-dataset but it has to be modified for Pix2Pix.

**To obtain and modify the dataset:**
1. Download the dataset from https://www.kaggle.com/datasets/balraj98/facades-dataset.
2. It will download as `archive.zip`.
3. Unzip the file to a folder in your repository.
4. Copy the relative path of the unzipped folder.
5. Paste the path for the `original_path` variable under main in the `arrange_data.py` script in scripts.
6. Run the `arrange_data.py` script.
7. Copy the relative file paths to the `folder_paths` array under main in the `rename_filenames.py` script in scripts.
8. Run the `rename_filenames.py` script.






