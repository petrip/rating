import pickle
import argparse

# assume input to be a binary  pickle file with each entry consisting
# of header dictionary 

class Rating():
    def __init__(self):
        self.predicted = 0
        self.correct = 0
        self.kukkuu = True
    
    def __str__(self):
        return "Games: {} points {}  ratio {}".format(self.predicted, self.correct, round(self.correct / self.predicted, 3))


class Glicko2(Rating):
    def __init__(self):
        super().__init__()

    def predict(self, header):
        # Predict  win for stronger player and white i equal
        # having white is actually up to 50 elo points worth
        # for purpose of these test ignoring draws is easiest
        if header["Result"] == "1/2-1/2" : return

        self.predicted += 1

        if header["WhiteElo"] > header["BlackElo"]:
            if header["Result"] == "1-0":
                self.correct += 1
        else:
            if header["Result"] == "0-1":
                self.correct += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file' , type=argparse.FileType('rb'), default='headers.pckl', help='Python pickle file containing header dicts')
    parser.add_argument('-m', '--max', type=int, default = 0, help='Maximum amount of games to load, for debugging purposes')
    args = parser.parse_args()
    if not args.file :
        parser.print_usage()

    glicko2 = Glicko2()
    games_loaded = 0
    while args.max == 0 or games_loaded < args.max:
        try:
            hdr = pickle.load(args.file)
        except EOFError:
            break
        if not hdr : break
        glicko2.predict(hdr)
        games_loaded += 1
    print(glicko2)    

 