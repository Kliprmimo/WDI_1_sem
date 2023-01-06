# Na szachownicy o wymiarach 100x100 umieszczamy N gońców,M hetmanów,L skoczków,K wież(N,M,L,K<25)
# Położenie figur jest opisywane przez tablicę
# Proszę napisać funkcję, która zwróci położenie figur wzajemnie się szachujących.
# Do funkcji należy przekazać położenie figur.
# Należy zwizualizować rozkład figur na szachownicy.
# Testy powinny uwzględniać między innymi:
#
# Przypadek, w którym nie występuje szachowanie.
# Przypadek, w którym szachują się dwie figury każdego typu.
# Przypadek, w którym szachują się więcej niż dwie figury każdego typu.
import random
from colorama import Fore
from colorama import Style

bishops = []
knights = []
rooks = []
queens = []
list_board = [[0 for _ in range(100)] for _ in range(100)]
bishop_check_list = []
knight_check_list = []
rook_check_list = []
queen_check_list = []


def generate_random_pawns_positions():
    for _ in range(20):
        bishops.append((random.randint(0, 99), random.randint(0, 99)))
        knights.append((random.randint(0, 99), random.randint(0, 99)))
        rooks.append((random.randint(0, 99), random.randint(0, 99)))
        queens.append((random.randint(0, 99), random.randint(0, 99)))


def visualise(list_to_visualise):
    for row in list_to_visualise:
        print("")
        for pawn in row:
            if pawn == 0:
                print(pawn, end="")
            else:
                print(f"{Fore.RED}{pawn}{Style.RESET_ALL}", end="")


class Pawn:
    def __init__(self, coord_list):
        self.coord_list = coord_list

    def put_on_board(self, letter, list_to_fill):
        for coord in self.coord_list:
            x, y = coord
            if list_to_fill[x][y] == 0:
                list_to_fill[x][y] = letter
            else:
                list_to_fill[x][y] = 0
                print("Pawns cant stand on each other!")
        return list_to_fill


class Bishop(Pawn):
    def __init__(self, coord_list):
        super().__init__(coord_list)

    def check_for_check_bishop(self, board_list, check_list):
        for bishop_coords in self.coord_list:
            x, y = bishop_coords
            i = 1
            while x + i < 100 and y + i < 100:
                if board_list[x + i][y + i] != 0:
                    check_list.append(((x, y), (x + i, y + i)))
                    break
                else:
                    i += 1
            i = -1
            while x + i >= 0 and y + i >= 0:
                if board_list[x + i][y + i] != 0:
                    check_list.append(((x, y), (x + i, y + i)))
                    break
                else:
                    i -= 1
            i = 1
            while x - i >= 0 and y + i < 100:
                if board_list[x - i][y + i] != 0:
                    check_list.append(((x, y), (x - i, y + i)))
                    break
                else:
                    i += 1
            i = -1
            while 0 <= x - i < 100 and 100 > y + i >= 0:
                if board_list[x - i][y + i] != 0:
                    check_list.append(((x, y), (x - i, y + i)))
                    break
                else:
                    i -= 1
        return check_list


class Knight(Pawn):
    def __init__(self, coord_list):
        super().__init__(coord_list)

    def check_for_check_knight(self, board_list, check_list):

        for knight_coords in self.coord_list:
            x, y = knight_coords
            if 0 <= x - 2 < 100 and 0 <= y + 1 < 100:
                if board_list[x - 2][y + 1] != 0:
                    check_list.append(((x, y), (x - 2, y + 1)))
            if 0 <= x - 1 < 100 and 0 <= y + 2 < 100:
                if board_list[x - 1][y + 2] != 0:
                    check_list.append(((x, y), (x - 1, y + 2)))
            if 0 <= x + 1 < 100 and 0 <= y + 2 < 100:
                if board_list[x + 1][y + 2] != 0:
                    check_list.append(((x, y), (x + 1, y + 2)))
            if 0 <= x + 2 < 100 and 0 <= y + 1 < 100:
                if board_list[x + 2][y + 1] != 0:
                    check_list.append(((x, y), (x + 2, y + 1)))
            if 0 <= x + 2 < 100 and 0 <= y - 1 < 100:
                if board_list[x + 2][y - 1] != 0:
                    check_list.append(((x, y), (x + 2, y - 1)))
            if 0 <= x + 1 < 100 and 0 <= y - 2 < 100:
                if board_list[x + 1][y - 2] != 0:
                    check_list.append(((x, y), (x + 1, y - 2)))
            if 0 <= x - 1 < 100 and 0 <= y - 2 < 100:
                if board_list[x - 1][y - 2] != 0:
                    check_list.append(((x, y), (x - 1, y - 2)))
            if 0 <= x - 2 < 100 and 0 <= y - 1 < 100:
                if board_list[x - 2][y - 1] != 0:
                    check_list.append(((x, y), (x - 2, y - 1)))
        return check_list


class Rook(Pawn):
    def __init__(self, coord_list):
        super().__init__(coord_list)

    def check_for_check_rook(self, board_list, check_list):

        for rook_coords in self.coord_list:
            x, y = rook_coords
            i = -1
            while 100 > x + i >= 0:
                if board_list[x + i][y] != 0:
                    check_list.append(((x, y), (x + i, y)))
                    break
                else:
                    i -= 1
            i = 1
            while 100 > x + i >= 0:
                if board_list[x + i][y] != 0:
                    check_list.append(((x, y), (x + i, y)))
                    break
                else:
                    i += 1
            i = -1
            while 100 > y + i >= 0:
                if board_list[x][y + i] != 0:
                    check_list.append(((x, y), (x, y + i)))
                    break
                else:
                    i -= 1
            i = 1
            while 100 > y + i >= 0:
                if board_list[x][y + i] != 0:
                    check_list.append(((x, y), (x, y + i)))
                    break
                else:
                    i += 1
        return check_list


class Queen(Rook, Bishop):
    def __init__(self, coord_list):
        super().__init__(coord_list)


def run_simulation():
    temp_list = [[0 for _ in range(100)] for _ in range(100)]
    generate_random_pawns_positions()
    bishop_object = Bishop(bishops)
    temp_list = Bishop.put_on_board(bishop_object, "B", temp_list)
    knight_object = Knight(knights)
    temp_list = Knight.put_on_board(knight_object, "K", temp_list)
    rook_object = Rook(rooks)
    temp_list = Rook.put_on_board(rook_object, "R", temp_list)
    queen_object = Queen(queens)
    temp_list = Queen.put_on_board(queen_object, "Q", temp_list)
    bishop_check_list_final = Bishop.check_for_check_bishop(bishop_object, temp_list, bishop_check_list)
    knight_check_list_final = Knight.check_for_check_knight(knight_object, temp_list, knight_check_list)
    rook_check_list_final = Rook.check_for_check_rook(rook_object, temp_list, rook_check_list)
    queen_rook_check_list_final = Queen.check_for_check_rook(queen_object, temp_list, queen_check_list)
    queen_bithop_check_list_final = Queen.check_for_check_bishop(queen_object, temp_list, queen_check_list)
    print(f"bishop checks: {bishop_check_list_final}")
    print(f"Knight checks: {knight_check_list_final}")
    print(f"Rook checks: {rook_check_list_final}")
    print(f"Queen checks: {queen_rook_check_list_final}{queen_bithop_check_list_final}")
    visualise(temp_list)


if __name__ == '__main__':
    run_simulation()
