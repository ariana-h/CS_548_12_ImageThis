import CG.test as CGT 

def main():
    CGT.main(["--dataroot", "Dataset/Georgian",
              "--model", "pix2pix",
              "--name", "georgian",
              "--direction", "BtoA"])
              
if __name__ == "__main__":
    main()