import pickle
import chess.pgn
import sys


f = open("lichess_db_standard_rated_2021-06.pgn")
out = open("headers.pckl","wb")
#Grab just 5min games
count = 0
flip = 0
while f:
    g = chess.pgn.read_headers(f)
    if not g : break
    #skip unrated
    try:
        g["WhiteRatingDiff"]
    except:
        continue    
    if g["TimeControl"] == '300+0':
        count += 1
        if count % 2000 :
            if flip:
                print('.', end='')
            else:
                print(":",end='')
            sys.stdout.flush()
        pickle.dump(g, out)
print("games found : ", count)