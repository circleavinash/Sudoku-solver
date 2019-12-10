import copy
import numpy as np
from time import time
from time import sleep
import math


def getFirstEmpty(sud):
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                return i, j
    return None


def str_to_sud(string):
    string = string.split("]")
    sud = []
    for i in string:
        sub = []
        for j in i:
            if j in [str(k) for k in range(1, 10)]:
                sub.append(int(j))
        if sub:
            sud.append(sub)
    return sud



def getSuduko():
    sud = []
    print("Enter zeros in place of spaces.\n")
    for i in range(9):
        lis = input('Enter row:').split(' ')
        t = []
        for j in range(9):
            if lis[j] == ' ':
                t.append(0)
            else:
                t.append(int(lis[j]))
        sud.append(t)
    return sud


def print_sud(sud):
    print()
    for a in range(len(sud)):
        print(" " * 5, end=" ")
        for b in range(len(sud)):
            print(sud[a][b], end=" ")
            if b in [2, 5]:
                print('|', end=" ")
        if a in [2, 5]:
            print("\n", " " * 5, "- " * 10, end=" ")
        print()


def boxElements(sud, x, y):
    box = []
    x, y = int(math.floor(x / 3)) * 3, int(math.floor(y / 3)) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            box.append(sud[i][j])
    return box


def getPossible(sud, i, j, rev=False):
    all_ele = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    possible = []
    if sud[i][j] == 0:
        present = set(sud[i] + list(np.array(sud)[:, j]) + boxElements(sud, i, j))
        possible = sorted(list(all_ele - present), reverse=rev)##################################
    return possible


def specSolve(sudoku, depth=0, back_tracks=0, calls=0, rev=False):
    sudoku1 = copy.deepcopy(sudoku)
    empty = getFirstEmpty(sudoku)
    calls += 1
    if empty:
        x, y = empty
        possible = getPossible(sudoku1, x, y, rev)
        # print(" " * depth, depth)
        if possible:
            for i in possible:
                
                sudoku2 = copy.deepcopy(sudoku1)
                sudoku2[x][y] = i
                sudoku3, back_tracks, calls = specSolve(copy.deepcopy(sudoku2), depth + 1, back_tracks, calls, rev)
                if '0' not in str(sudoku3):
                    return sudoku3, back_tracks, calls
        else:
            back_tracks += 1
            #print("bc")
    return sudoku1, back_tracks, calls


s1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
      [6, 8, 0, 0, 7, 0, 0, 9, 0],
      [1, 9, 0, 0, 0, 4, 5, 0, 0],
      [8, 2, 0, 1, 0, 0, 0, 4, 0],
      [0, 0, 4, 6, 0, 2, 9, 0, 0],
      [0, 5, 0, 0, 0, 3, 0, 2, 8],
      [0, 0, 9, 3, 0, 0, 0, 7, 4],
      [0, 4, 0, 0, 5, 0, 0, 3, 6],
      [7, 0, 3, 0, 1, 8, 0, 0, 0]]  # 45    ascending:0.03125s      descending:0.046875

s2 = [[0, 0, 0, 0, 0, 0, 0, 0, 7],
      [7, 0, 4, 0, 0, 0, 8, 9, 3],
      [0, 0, 6, 8, 0, 2, 0, 0, 0],
      [0, 0, 7, 5, 2, 8, 6, 0, 0],
      [0, 8, 0, 0, 0, 6, 7, 0, 1],
      [9, 0, 3, 4, 0, 0, 0, 8, 0],
      [0, 0, 0, 7, 0, 4, 9, 0, 0],
      [6, 0, 0, 0, 9, 0, 0, 0, 0],
      [4, 5, 9, 0, 0, 0, 1, 0, 8]]  # 49    ascending:1s      descending:0.453125s


s2_1 = [[0, 0, 0, 3, 2, 9, 1, 0, 0],
        [9, 0, 0, 0, 1, 0, 8, 6, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [3, 0, 7, 4, 0, 0, 0, 0, 2],
        [6, 0, 0, 9, 0, 2, 0, 0, 8],
        [8, 0, 0, 0, 0, 6, 5, 0, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 4, 3, 0, 9, 0, 0, 0, 6],
        [0, 0, 5, 8, 4, 1, 0, 0, 0]]    # 51    ascending:1.296875s      descending:0.828125s


s2_2 = [[1, 0, 2, 0, 0, 0, 7, 0, 3],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [8, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 8, 0, 5, 3, 7, 0, 1, 0],
        [0, 0, 4, 0, 0, 0, 9, 0, 0],
        [0, 6, 0, 4, 9, 1, 0, 2, 0],
        [6, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 2, 0, 9, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 1]]    # 51    ascending:0.40625      descending:0.296875s


s3 = [[0, 3, 0, 0, 0, 0, 0, 4, 0],
      [0, 1, 0, 0, 9, 7, 0, 5, 0],
      [0, 0, 2, 5, 0, 8, 6, 0, 0],
      [0, 0, 3, 0, 0, 0, 8, 0, 0],
      [9, 0, 0, 0, 0, 4, 3, 0, 0],
      [0, 0, 7, 6, 0, 0, 0, 0, 4],
      [0, 0, 9, 8, 0, 5, 4, 0, 0],
      [0, 7, 0, 0, 0, 0, 0, 2, 0],
      [0, 5, 0, 0, 7, 1, 0, 8, 0]]  # 53    ascending:9.984375s      descending:7.5s

s3_1 = [[0, 0, 1, 0, 7, 5, 0, 0, 0],
        [5, 0, 0, 0, 9, 0, 8, 0, 3],
        [0, 0, 0, 1, 0, 0, 0, 0, 5],
        [7, 0, 5, 3, 0, 0, 1, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 4, 0, 0, 6, 7, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [9, 0, 2, 0, 5, 0, 0, 0, 4],
        [0, 0, 0, 2, 3, 0, 6, 0, 0]]    # 53    ascending:0.3125s      descending:0.46875s

s4 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 3, 6, 0, 0, 0, 0, 0],
      [0, 7, 0, 0, 9, 0, 2, 0, 0],
      [0, 5, 0, 0, 0, 7, 0, 0, 0],
      [0, 0, 0, 0, 4, 5, 7, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 3, 0],
      [0, 0, 1, 0, 0, 0, 0, 6, 8],
      [0, 0, 8, 5, 0, 0, 0, 1, 0],  # toughest
      [0, 9, 0, 0, 0, 0, 4, 0, 0]]  # 60    ascending: 28s      descending:1148s


s5 = [[0, 0, 0, 6, 0, 0, 4, 0, 0],
      [7, 0, 0, 0, 0, 3, 6, 0, 0],
      [0, 0, 0, 0, 9, 1, 0, 8, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 5, 0, 1, 8, 0, 0, 0, 3],
      [0, 0, 0, 3, 0, 6, 0, 4, 5],
      [0, 4, 0, 2, 0, 0, 0, 6, 0],
      [9, 0, 3, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 1, 0, 0]]  # 58    ascending: 492s descending: 212s


# test_sud = s4
# s_ans = None
# # test_sud = getSuduko()from_mem = 0
# if 1:
#     t = time()
#     store = str(test_sud)
#     s_ans, back_tracks, calls = specSolve(test_sud)
#     print("Time taken:", time() - t)
#     print("Number of back tracks:", back_tracks)
#     print("Number of calls:", calls)
# #print(ans)
# print("Number of unknown:", str(test_sud).count('0'))
# print_sud(s_ans)




# t = time()
# #check(8, 0, 0, s2)
# getPossible(s2, 0, 0)
# print("Time taken:", time() - t)

