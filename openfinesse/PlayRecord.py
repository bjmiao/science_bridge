from Board import Board
import copy
class PlayRecord(object):

    def __init__(self, board, trump):
        # trump = S/H/D/C/NT
        self.trump = trump
        self.board = board
        self.board_backup = copy.deepcopy(board)
        self.nstrick = 0
        self.ewtrick = 0

    def trick_winner(self, cards, leader):
        # cards : [("C", 14), ("D",2), ("S", 13), ("C", 2)], representing the card from N,E,S,W
        # leader : N/E/S/W
        # output : 'N', 'E', 'S', 'W' : who wins this trick
        card_player_map = {"N" : card[0], "E":card[1], 'S': card[2], "W": card[3] }
        largest_player = None
        if self.trump == "NT":
            ruling_suit = card_player_map[leader][0]
            largest_spot = card_player_map[leader][1]
            print(ruling_suit, largest_spot)
            largest_player = leader
            for player, card in card_player_map.items():
                if (card[0] == ruling_suit and card[1] > largest_spot):
                    largest_spot = card[1]
                    largest_player = player
            return largest_player
        else :
            ruling_suit = card_player_map[leader][0]
            largest_spot = card_player_map[leader][1]
            for player, card in card_player_map.items():
                if (ruling_suit == self.trump):
                    if (card[0] == self.trump and card[1] > largest_spot):
                        largest_spot = card[1]
                        largest_player = player
                else :
                    if (card[0] == self.trump):
                        ruling_suit, largest_spot = self.trump, card[1]
                        largest_player = player
                    elif (card[0] == ruling_suit and card[1] > largest_spot):
                        largest_spot = card[1]
                        largest_player = player
        return largest_player

    def can_play_list(self, player):
        ret = []
        this_hand = self.board.hand[player]
        SUIT = ['S','H','D','C']
        for suit in SUIT:
            for card in this_hand.card[suit]:
                ret.append((suit, card))
        return ret
    def recover_board(self):
        self.board = copy.deepcopy(self.board_backup)
        self.nstrick = 0
        self.ewtrick = 0
        print(self.board.south.spade)

if __name__ == "__main__":
    board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"
    board = Board(board_str)
    print(board)
    pr = PlayRecord(board, "S")

    print(pr.can_play_list('N'))
    print(pr.can_play_list('W'))
    print(pr.can_play_list('E'))
    print(pr.can_play_list('S'))

    # print(pr.board.south.spade)
    # pr.recover_board()

    # print(board)