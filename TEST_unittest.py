import unittest
import main


class TestCheckLogic(unittest.TestCase):

    # case where no pawns check each other
    def test_first_case(self):
        empty_list = [[0 for _ in range(100)] for _ in range(100)]
        bishop_check_list = []
        knight_check_list = []
        rook_check_list = []
        queen_check_list = []
        bishops = [(80, 20), (69, 42), (23, 33)]
        knights = [(3, 3), (4, 4)]
        rooks = [(0, 0), (1, 1), (2, 2)]
        queens = [(7, 6), (8, 9)]
        bishop_object = main.Bishop(bishops)
        temp_list = main.Bishop.put_on_board(bishop_object, "B", empty_list)
        knight_object = main.Knight(knights)
        temp_list = main.Knight.put_on_board(knight_object, "K", temp_list)
        rook_object = main.Rook(rooks)
        temp_list = main.Rook.put_on_board(rook_object, "R", temp_list)
        queen_object = main.Queen(queens)
        temp_list = main.Queen.put_on_board(queen_object, "Q", temp_list)
        bishop_test = main.Bishop.check_for_check_bishop(bishop_object, temp_list, bishop_check_list)
        knight_test = main.Knight.check_for_check_knight(knight_object, temp_list, knight_check_list)
        rook_test = main.Rook.check_for_check_rook(rook_object, temp_list, rook_check_list)
        queen_rook_test = main.Queen.check_for_check_rook(queen_object, temp_list, queen_check_list)
        queen_bishop_test = main.Queen.check_for_check_bishop(queen_object, temp_list, queen_check_list)
        main.visualise(temp_list)
        self.assertEqual(rook_test, [])
        self.assertEqual(knight_test, [])
        self.assertEqual(queen_rook_test, [])
        self.assertEqual(queen_bishop_test, [])
        self.assertEqual(bishop_test, [])
        print("\nCase one positive")

    # case where all pawns check each other
    def test_second_case(self):
        empty_list = [[0 for _ in range(100)] for _ in range(100)]
        bishop_check_list = []
        knight_check_list = []
        rook_check_list = []
        queen_check_list_rook = []
        queen_check_list_bishop = []
        bishops = [(2, 8)]
        knights = [(4, 6)]
        rooks = [(0, 0), (0, 1)]
        queens = [(1, 4), (2, 5)]
        bishop_object = main.Bishop(bishops)
        temp_list = main.Bishop.put_on_board(bishop_object, "B", empty_list)
        knight_object = main.Knight(knights)
        temp_list = main.Knight.put_on_board(knight_object, "K", temp_list)
        rook_object = main.Rook(rooks)
        temp_list = main.Rook.put_on_board(rook_object, "R", temp_list)
        queen_object = main.Queen(queens)
        temp_list = main.Queen.put_on_board(queen_object, "Q", temp_list)
        bishop_test = main.Bishop.check_for_check_bishop(bishop_object, temp_list, bishop_check_list)
        knight_test = main.Knight.check_for_check_knight(knight_object, temp_list, knight_check_list)
        rook_test = main.Rook.check_for_check_rook(rook_object, temp_list, rook_check_list)
        queen_rook_test = main.Queen.check_for_check_rook(queen_object, temp_list, queen_check_list_rook)
        queen_bishop_test = main.Queen.check_for_check_bishop(queen_object, temp_list, queen_check_list_bishop)
        main.visualise(temp_list)
        self.assertEqual(rook_test, [((0, 0), (0, 1)), ((0, 1), (0, 0))])
        self.assertEqual(knight_test, [((4, 6), (2, 5))])
        self.assertEqual(queen_rook_test, [((2, 5), (2, 8))])
        self.assertEqual(queen_bishop_test, [((1, 4), (2, 5)), ((2, 5), (1, 4))])
        self.assertEqual(bishop_test, [((2, 8), (4, 6))])
        print("\nCase two positive")

    # case where some pawns are checked some by multiple other pawns
    def test_third_case(self):
        empty_list = [[0 for _ in range(100)] for _ in range(100)]
        bishop_check_list = []
        knight_check_list = []
        rook_check_list = []
        queen_check_list_rook = []
        queen_check_list_bishop = []
        bishops = [(3, 3)]
        knights = [(2, 2)]
        rooks = [(0, 0), (0, 1)]
        queens = [(1, 0)]
        bishop_object = main.Bishop(bishops)
        temp_list = main.Bishop.put_on_board(bishop_object, "B", empty_list)
        knight_object = main.Knight(knights)
        temp_list = main.Knight.put_on_board(knight_object, "K", temp_list)
        rook_object = main.Rook(rooks)
        temp_list = main.Rook.put_on_board(rook_object, "R", temp_list)
        queen_object = main.Queen(queens)
        temp_list = main.Queen.put_on_board(queen_object, "Q", temp_list)
        bishop_test = main.Bishop.check_for_check_bishop(bishop_object, temp_list, bishop_check_list)
        knight_test = main.Knight.check_for_check_knight(knight_object, temp_list, knight_check_list)
        rook_test = main.Rook.check_for_check_rook(rook_object, temp_list, rook_check_list)
        queen_rook_test = main.Queen.check_for_check_rook(queen_object, temp_list, queen_check_list_rook)
        queen_bishop_test = main.Queen.check_for_check_bishop(queen_object, temp_list, queen_check_list_bishop)
        main.visualise(temp_list)
        self.assertEqual(rook_test, [((0, 0), (1, 0)), ((0, 0), (0, 1)), ((0, 1), (0, 0))])
        self.assertEqual(knight_test, [((2, 2), (1, 0)), ((2, 2), (0, 1))])
        self.assertEqual(queen_rook_test, [((1, 0), (0, 0))])
        self.assertEqual(queen_bishop_test, [((1, 0), (0, 1))])
        self.assertEqual(bishop_test, [((3, 3), (2, 2))])
        print("\nCase three positive")
