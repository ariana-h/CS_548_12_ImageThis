import CG.train as CGT 

def main():
    CGT.main(["--dataroot", "Dataset/Contemporary",
              "--model", "pix2pix",
              "--direction", "BtoA",
              "--name", "contemporary",
              "--verbose",])
    # --gpu_ids = -1

if __name__ == "__main__":
    main()