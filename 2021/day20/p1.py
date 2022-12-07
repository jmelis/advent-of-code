
def print_image(image):
    for row in image:
        line = "".join([str(i) for i in row])
        print(line.replace('0','.').replace('1','#'))

def pad(image):
    DIM = 100
    hlength = DIM*2 + len(image)
    newimage = []
    for _ in range(DIM):
        newimage.append([0 for _ in range(hlength)])
    for row in image:
        newimage.append([0 for _ in range(DIM)]+row+[0 for _ in range(DIM)])
    for _ in range(DIM):
        newimage.append([0 for _ in range(hlength)])
    return newimage


def val(image, r, c, retval=0):
    try:
        v = image[r][c]
    except IndexError:
        return retval
    return v

around = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 0),  (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

# # ex
# algo="..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
# input = """
# #..#.
# #....
# ##..#
# ..#..
# ..###
# """.replace('.',"0").replace('#','1')

# input
algo = "##.....##.#.#####.#...###...#.##..#....##..#.##.#.#....##.....#.##.##.#.#.#...#.#.#.###.##..#.#.#.#..#.##.#...#..#.#.#..#####.##.#..#..##.#..#.#...#.....#.###..#..#####.##...#..##..##...#.#...##.##..##...##.##.#......#...##.##.#####.#....####....######.#.#.......#.############.###..#..#......####......#..##.####.##....#..#.#.###..#.####.####.#.##.##.##..###.#..#.......#....#..########....##..##.#...#.#.###.###.###..#..#.###..#....#.###..#.##.##..###.#.#####....###.##.###.....#######........#.#.##...##.#...."
input = open('input.txt').read().replace('.',"0").replace('#','1')

image = [[int(i) for i in row] for row in input.splitlines()]
image = pad(image)
print_image(image)
print()
for i in range(50):
    newimage = [[0 for _ in range(len(image))] for _ in range(len(image[0]))]
    for r, row in enumerate(image):
        for c, v in enumerate(row):
            binarystr = ""
            for (tr, tc) in around:
                rr = r + tr
                cc = c + tc
                binarystr += str(val(image, rr, cc, retval=(i%2)))
            dec = int(binarystr, 2)
            newval = 1 if algo[dec] == '#' else 0
            newimage[r][c] = newval
    image = newimage
    print_image(image)
    print()

lit = 0 
for row in image:
    lit += sum(row)
print(lit)
