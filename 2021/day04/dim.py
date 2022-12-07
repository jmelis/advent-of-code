DIM = 5
for i in range(DIM):
    pos_list = [num+i for num in range(0, DIM*DIM, DIM)]
    print(pos_list)
