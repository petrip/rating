import pickle
import chess.pgn
import sys


f = open("lichess_db_standard_rated_2021-06.pgn")
count = 0
controls = {}
while f  and count < 10000:
    if count % 1000  == 0:
        print("-{}".format(count), end='')
        sys.stdout.flush()

    g = chess.pgn.read_headers(f)
    if not g:
        break
    try:
        g["WhiteRatingDiff"]
    except:
        continue
    count += 1
    try:
        controls[g["TimeControl"]] += 1
    except KeyError:
        controls[g["TimeControl"]] = 1


print("games found : ", count)
cnt = float(count)
for ctl in sorted(controls):
    amount = float(controls[ctl])
    ratio = 100 * amount/cnt
    print("time control: {} games : {}  ratio: {}  %".format(ctl, amount, round(ratio,2)))