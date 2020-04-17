
# convert_dict = {"A":14,"K":13,"Q":12,"J":11,"T":10}
# for i in range(2, 10):
#     convert_dict[str(i)] = i
# print(convert_dict)

class Hand(object):
    def __init__(self, hand_str, position):
        hand_list = hand_str.split(".")
        self.raw_card = {}
        self.raw_card['S'] = list(hand_list[0])
        self.raw_card['H'] = list(hand_list[1])
        self.raw_card['D'] = list(hand_list[2])
        self.raw_card['C'] = list(hand_list[3])
        
        self.card = {}
        for suit in ['S', 'H', 'D', 'C']:
            self.card[suit] = [convert_dict[i] for i in self.raw_card[suit]]

        self.position = position # N/E/S/W

    def __str__(self):
        ret = "==" + self.position + "==\n"
        ret += "S:" + ''.join(self.raw_card['S']) + "\n" 
        ret += "H:" + ''.join(self.raw_card['H']) + "\n" 
        ret += "D:" + ''.join(self.raw_card['D']) + "\n" 
        ret += "C:" + ''.join(self.raw_card['C']) + "\n" 
        return ret
    

class Board(object):
    def __init__(self, board_str):
        field = {}
        if (board_str[0] == "N"):
            field = {"N" : 0, "E" : 1, "S" : 2, "W" : 3}
        
        board_list = board_str[2:].split(' ')
        self.hand = {}
        for player in field.keys(): # N/E/S/W
            self.hand[player] = Hand(board_list[field[player]], player)

    def __str__(self):
        # (TODO) Optimize output format
        ret = self.hand['N'].__str__() + "\n" + self.hand["E"].__str__() + "\n"
        ret += self.hand['S'].__str__() + "\n" + self.hand["W"].__str__() + "\n"
        return ret

board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"

if __name__ == "__main__":
    board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"
    board = Board(board_str)
    print(board)