
convert_dict = {"A":14,"K":13,"Q":12,"J":11,"T":10}
for i in range(2, 10):
    convert_dict[str(i)] = i
print(convert_dict)

class Hand(object):
    def __init__(self, hand_str, position):
        hand_list = hand_str.split(".")
        self.spade_raw = list(hand_list[0])
        self.heart_raw = list(hand_list[1])
        self.diamond_raw = list(hand_list[2])
        self.club_raw = list(hand_list[3])

        self.spade = [convert_dict[i] for i in self.spade_raw]
        self.heart = [convert_dict[i] for i in self.heart_raw]
        self.diamond = [convert_dict[i] for i in self.diamond_raw]
        self.club = [convert_dict[i] for i in self.club_raw]

        self.position = position # N/E/S/W

    def __str__(self):
        ret = "==" + self.position + "==\n"
        ret += "S:" + ''.join(self.spade_raw) + "\n" 
        ret += "H:" + ''.join(self.heart_raw) + "\n" 
        ret += "D:" + ''.join(self.diamond_raw) + "\n" 
        ret += "C:" + ''.join(self.club_raw) + "\n" 
        return ret
    

class Board(object):
    def __init__(self, board_str):
        field = {}
        if (board_str[0] == "N"):
            field = {"N" : 0, "E" : 1, "S" : 2, "W" : 3}
        
        board_list = board_str[2:].split(' ')
        self.north = Hand(board_list[field['N']], 'N')
        self.east = Hand(board_list[field['E']], 'E')
        self.south = Hand(board_list[field['S']], 'S')
        self.west = Hand(board_list[field['W']], 'W')

    def __str__(self):
        # (TODO) Optimize output format
        ret = self.north.__str__() + "\n" + self.south.__str__() + "\n"
        ret += self.east.__str__() + "\n" + self.west.__str__() + "\n"
        return ret

board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"

if __name__ == "__main__":
    board_str = "N:AJT9.732.9764.T5 85.A96.T32.A9874 KQ73.QT8.AJ8.KQ3 642.KJ54.KQ5.J62"
    board = Board(board_str)
    print(board)