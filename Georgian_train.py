import CG.train as CGT 

def main():
    CGT.main(["--dataroot", "Dataset/Georgian",
              "--model", "pix2pix",
              "--direction", "BtoA",
              "--name", "georgian",
              "--verbose"])

if __name__ == "__main__":
    main()