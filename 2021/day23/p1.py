 #############
 #...........#
 ###A#B#C#D###
   #A#B#C#D#
   #########

# r0 => hallway
# r1 => roomtop
# r2 => roomdown


def seq(a, b):
    if a < b:
        return range(a+1, b+1)
    else:
        return range(a-1, b-1, -1)

class Grid:
    cols = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    cost_dict = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    def __init__(self, s):
        top = [l for l in s[0:11]]
        rooms = [l for l in s[11:19]]
        self.cost = int(s[19:])
        self.grid = [[None]*11 for _ in range(3)]

        top = [l for l in top]
        rooms = [l for l in rooms]

        for c in range(len(self.grid[0])):
            v = top.pop(0)
            v = v if v != ' ' else None
            self.grid[0][c] = v

        for c in [2,4,6,8]:
            for r in [1,2]:
                v = rooms.pop(0)
                v = v if v != ' ' else None
                self.grid[r][c] = v
            
    def initstr(self):
        def c(v):
            if v is None:
                return " "
            else:
                return v
        s = "".join(c(l) for l in self.grid[0])
        for c in [2,4,6,8]:
            for r in [1,2]:
                s += self.grid[r][c]
        s += str(self.cost)
        return s

    def __hash__(self):
        return hash(self.initstr())

    def __eq__(self, o):
        return hash(self) == hash(o)
 
    def __ne__(self, o):
        return hash(self) != hash(o)
    
    def __repr__(self):
        grid_str = ""
        for r, row in enumerate(self.grid):
            rstr = ""
            for c,e in enumerate(row):
                if r > 0 and c not in [2,4,6,8]:
                    rstr += ' '
                elif not e:
                    rstr += '.'
                else:
                    rstr += e
            grid_str += rstr + "\n"
        return grid_str
    
    def copy(self):
        return Grid(self.initstr())


    def finished(self):
        return self.initstr().startswith('           AABBCCDD')

    def move(self, r1, c1, r2, c2, cost):
        val = self.grid[r1][c1]
        self.grid[r1][c1] = None
        self.grid[r2][c2] = val
        self.cost += cost

    def letters(self, row=None, col=None, letter=None, coords=False):
        letters = []
        for r in range(len(self.grid)):
            if row is not None and r != row:
                continue
            for c in range(len(self.grid[0])):
                if col is not None and c != col:
                    continue
                val = self.grid[r][c]
                if letter is not None:
                    if val != letter:
                        continue
                if val:
                    if coords:
                        letters.append((r,c,val))
                    else:
                        letters.append(val)
        return letters

    def move_from_r0(self, c):
        r = 0
        val = self.grid[r][c]
    
        if val is None: return False

        tc = self.cols[val]
        tv1 = self.grid[1][tc]
        tv2 = self.grid[2][tc]

        if tv1 is None and tv2 is None: tr = 2
        elif tv1 is None and tv2 == val: tr = 1
        else: return False
            
        for cc in seq(c, tc):
            vv = self.grid[0][cc]
            if vv: return False
        
        cost = (len(seq(c, tc)) + tr)*self.cost_dict[val]
        self.move(0, c, tr, tc, cost)
        return True

    def moves_to_h0(self, r, c):
        val = self.grid[r][c]
        if val is None: return []

        # bring to top
        for rr in seq(r, 0):
            vv = self.grid[rr][c]
            if vv is not None: return []

        # positive
        cost = lambda: self.cost_dict[val]*(abs(cc-c) + 2 - r)
        moves = []
        for cc in seq(c, 10):
            vv = self.grid[0][cc]
            if vv is not None:
                break
            if cc not in [2,4,6,8]:
                moves.append((0, cc, cost()))

        # negative
        for cc in seq(c, 0):
            vv = self.grid[0][cc]
            if vv is not None:
                break
            if cc not in [2,4,6,8]:
                moves.append((0, cc, cost()))
        
        return moves

results = []
seen = set()

# def process(grid):
#     global results
#     global seen

#     if grid in seen:
#         return

#     seen.add(grid)

#     if grid.finished():
#         results.append(grid.cost)

#     row0_letters = grid.letters(0, coords=True)

#     for _, c, _ in row0_letters:
#         g = grid.copy()
#         g.move_from_r0(c)
#         process(g)

#     row1_letters = grid.letters
#     for r, c, _ in 

g = Grid('A           ABBCCDD0')
print(g.moves_to_h0(2,2))
# row0_letters = g.letters(0, coords=True)
# for r, c, val in row0_letters:
#     g.move_from_r0(c)
# print([g.initstr()])
# print(g.grid[0])
# print(g.finished())
# # print(g.finished)
# # print(g)
