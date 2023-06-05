from PlayRecord import PlayRecord
from Board import Board

def main(pr):
    # انجام عملیات مربوطه و بدست آوردن مقادیر NStrick و EWtrick
    NStrick = "var NStrick"
    EWtrick = "var EWtrick"
    return NStrick, EWtrick

if __name__ == "__main__":
    board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"
    board = Board(board_str)
    pr = PlayRecord(board, "NT")
    NStrick, EWtrick = main(pr)
    print("NStrick:", NStrick)
    print("EWtrick:", EWtrick)
