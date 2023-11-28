import CG.test as CGT 

def main():
    CGT.main(["--dataroot", "Dataset\Edwardian",
              "--model", "pix2pix",
              "--direction", "BtoA"])
              
if __name__ == "__main__":
    main()