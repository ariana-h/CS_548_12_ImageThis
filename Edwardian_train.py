import CG.train as CGT 

def main():
    CGT.main(["--dataroot", "Dataset/Edwardian",
              "--model", "pix2pix",
              "--direction", "BtoA",
              "--name", "edwardian",
              "--verbose"])

if __name__ == "__main__":
    main()