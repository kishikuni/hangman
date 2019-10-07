# http://tinyurl.com/h9q2cpc

def hangman(word):
    # 間違いの回数
    wrong = 0
    # 文字列リスト
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word) # 文字列の掛け算は繰り返し
    win = False
    print("Welcome to Hang Man!")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a alphabet"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$' # Not to let match in following roop
        else:
            wrong += 1

        # display match words
        print(" ".join(board))

        # display left turns
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose... Answer is '{}'.".format(word))

hangman("cat")
