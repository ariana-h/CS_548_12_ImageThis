import CG.test as CGT 

def main():
    CGT.main(["--dataroot", "Dataset/Contemporary",
              "--model", "pix2pix",
              "--name", "contemporary",
              "--direction", "BtoA"])
              
if __name__ == "__main__":
    main()