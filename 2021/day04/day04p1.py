DIM = 5
class Board:
    def __init__(self):
        self.complete = False
        self.insert_counter = 0
        self.data = [None] * DIM * DIM
        self.drawn = [0] * DIM * DIM 

    def add_row(self, row):
        for num in row.split():
            self.add_num(int(num))

    def add_num(self, num):
        self.data[self.insert_counter] = num
        self.insert_counter += 1
    
    def draw_many(self, nums):
        for num in nums.split(','):
            num = int(num)
            self.draw(num)

    def draw(self, num):
        for i, val in enumerate(self.data):
            if num == val:
                self.drawn[i] = 1
    
    def sum_not_drawn(self):
        sum = 0
        for i, val in enumerate(self.data):
            if self.drawn[i] == 0:
                sum += val
        return sum

    def check_drawn(self, pos_list):
        for pos in pos_list:
            if self.drawn[pos] == 0:
                return False
        return True

    def check_complete(self):
        # row
        for i in range(DIM):
            pos_list = [num + i*DIM for num in range(DIM)]
            if self.check_drawn(pos_list):
                return True

        # cols
        for i in range(DIM):
            pos_list = [num+i for num in range(0, DIM*DIM, DIM)]
            if self.check_drawn(pos_list):
                return True

        return False 

        
# input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

draw_numbers = input[0].split(',')

boards = []
for l in input[1:]:
    if len(l) == 0:
        b = Board()
        boards.append(b)
    else:
        boards[-1].add_row(l)

for num in draw_numbers:
    num = int(num)
    for b in boards:
        if b.complete:
            continue

        b.draw(num)
        if b.check_complete():
            score = b.sum_not_drawn() * num
            print(score)
            b.complete = True

