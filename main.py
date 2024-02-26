import time
import sys
import random


class Game:
    def __init__(self):
        self.count_win_player_1 = 0
        self.count_win_player_2 = 0


def Begin_Game(func):
    def wrapper():
        if active:
            time.sleep(1)
            func()
        else:
            print("Приходите поиграть ещё!\n"
                  "      (*￣▽￣*)ブ")
            sys.exit()

    return wrapper


@Begin_Game
def rules():
    print("Пришло время узнать правила!\n")
    time.sleep(0.5)

    while True:
        user_input = input("Нажмите Enter для продолжения...")
        if user_input == "":
            time.sleep(0.5)
            break
        else:
            print("Пожалуйста, нажмите только клавишу Enter.")

    print('\n' * 24)
    time.sleep(0.5)
    print(
        """
1)Игровое поле:

Игра проводится на квадратном поле размером 3x3 клетки.

2)Участники:
Играют два участника: один ставит крестики, другой - нолики.

3)Цель игры:
Целью игры является расположить три своих символа (крестика или нолика) в ряд по горизонтали, вертикали или диагонали.

4)Ход игры:
Игроки по очереди ставят свои символы на свободные клетки поля.
Сначала крестик, затем нолик, и так далее.

5)Победа:
Игрок, который первым расположит три своих символа в ряд (горизонтально, вертикально или диагонально), объявляется победителем.

6)Ничья:
Если на игровом поле не осталось свободных клеток, а никто не выиграл, игра объявляется ничьей.

7)Стратегия:
Игроки стремятся как можно скорее выстроить свои символы в ряд, блокируя при этом попытки противника сделать то же самое.

8)Правила для выигрыша:
Если один из игроков выстроил три своих символа в ряд, игра заканчивается, и этот игрок объявляется победителем.
Если оба игрока выстроили три символа в ряд одновременно (что возможно только в случае нарушения правил игры), игра считается недействительной.\n""")

    print("Надеемся, что вы запомнили все правила и сможете победить!")
    while True:
        user_inpu = input("Нажмите Enter, чтоьы приступить к игре...")
        if user_inpu == "":
            print('\n' * 20)
            break
        else:
            print("Пожалуйста, нажмите только клавишу Enter.")


def game_board():
    Array_Matrix = [["-" for o in range(4)] for o in range(4)]

    for num in range(1, 4):
        Array_Matrix[num][0] = str(num)

    for num_1 in range(4):
        if num_1 == 0:
            Array_Matrix[0][0] = str(" ")
        else:
            Array_Matrix[0][num_1] = str(num_1)

    for row in range(4):
        print(Array_Matrix[row])
    return Array_Matrix


def fate_Move():
    print("Бросается жребий, определяется Кто будет ходить первым.")
    x = random.randint(0, 1)

    for i in range(5):
        time.sleep(0.35)
        print(".", end=' ')
    print(" ")
    time.sleep(0.3)
    if x == 1:
        print("Первый ход будет делать игрок №1, ходит 'X'.")
        return 1
    else:
        print("Первый ход будет делать игрок №2, ходит '0'.")
        return 2


def Make_move(Array_Matrix, row, column, lot):
    Array_Matrix[row][column] = str(lot)
    for row in range(4):
        print(Array_Matrix[row])


def Win_game(Array_Matrix, game):
    if Check_win(Array_Matrix, "X"):
        game.count_win_player_1 += 1
        print("Игрок 1 победил")
        return True
    if Check_win(Array_Matrix, "0"):
        game.count_win_player_2 += 1
        print("Игрок 2 победил")
        return True


def Check_win(Array_Matrix, symbol):
    for row in range(1, 4):
        if Array_Matrix[row][1] == Array_Matrix[row][2] == Array_Matrix[row][3] == symbol:
            return True
    for column in range(1, 4):
        if Array_Matrix[1][column] == Array_Matrix[2][column] == Array_Matrix[3][column] == symbol:
            return True
    if Array_Matrix[1][1] == Array_Matrix[2][2] == Array_Matrix[3][3] == symbol:
        return True
    if Array_Matrix[1][3] == Array_Matrix[2][2] == Array_Matrix[3][1] == symbol:
        return True


def Check_rules_in_make_move(row, colum):
    if row < 1 or row > 3 or colum < 1 or colum > 3:
        print("Неккоректно введены координаты!")
        return True
    else:
        return False


def checking_the_field_occupancy(Array_Matrix, row, colum):
    if Array_Matrix[row][colum] != '-':
        print("Это поле уже занято, выберите другое")
        return True
    else:
        return False


def End_game(count_game, game):
    print(f"Сыгранно игр: {count_game}")
    print(f"Побед у игрока 1: {game.count_win_player_1}")
    print(f"Побед у игрока 2: {game.count_win_player_2}")
    time.sleep(1)
    new_game = input("Если хотите начать новую игру НАЖМИТЕ ENTER:")
    if new_game == '':
        print("\n" * 15)
        return True
    else:
        print("Cпасибо за игру!!!\n")
        return False


count_game = 0


def Game_play(count_game, game):
    firs_player = fate_Move()
    time.sleep(1.5)
    print("\n" * 2)

    Array_Matrix = game_board()

    count_lot = 1

    while True:  # без понятия как сделать лучше ничью, кроме ограничение количества ходов.

        if count_lot % 2 == 0:
            if firs_player == 1:
                print(f"Ход игрока {firs_player + 1}")
                row, colum = int(input("Введите номер строки:")), int(input("Введите номер столбца:"))
                if Check_rules_in_make_move(row, colum) or checking_the_field_occupancy(Array_Matrix, row, colum):
                    continue
                else:
                    Make_move(Array_Matrix, row, colum, "0")
                    count_lot += 1

            elif firs_player == 2:
                print(f"Ход игрока {firs_player - 1}")
                row, colum = int(input("Введите номер строки:")), int(input("Введите номер столбца:"))
                if Check_rules_in_make_move(row, colum) or checking_the_field_occupancy(Array_Matrix, row, colum):
                    continue
                else:
                    Make_move(Array_Matrix, row, colum, "X")
                    count_lot += 1
        else:
            if firs_player == 1:
                print(f"Ход игрока {firs_player}")
                row, colum = int(input("Введите номер строки:")), int(input("Введите номер столбца:"))
                if Check_rules_in_make_move(row, colum) or checking_the_field_occupancy(Array_Matrix, row, colum):
                    continue
                else:
                    Make_move(Array_Matrix, row, colum, "X")
                    count_lot += 1

            elif firs_player == 2:
                print(f"Ход игрока {firs_player}")
                row, colum = int(input("Введите номер строки:")), int(input("Введите номер столбца:"))
                if Check_rules_in_make_move(row, colum) or checking_the_field_occupancy(Array_Matrix, row, colum):
                    continue
                else:
                    Make_move(Array_Matrix, row, colum, "0")
                    count_lot += 1

        if Win_game(Array_Matrix, game):
            count_game += 1
            if End_game(count_game, game):
                Game_play(count_game, game)
            else:
                break

        if count_lot > 9:
            print("\n")
            print("Ничья!!")
            count_game += 1
            if End_game(count_game, game):
                Game_play(count_game, game)
            else:
                break


act_Q = input("Добро пожаловать в игру «Крестики-Нолики»!\n"
              "Чтобы начачть игру нажмите «Q», иначе будет Выход\n"
              " Ввод ------>")

active = act_Q == 'Q'

rules()
game = Game()
Game_play(count_game, game)

