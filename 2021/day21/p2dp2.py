DP = {}
def count(turn, p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    key = (turn, p1, p2, s1, s2)
    if key in DP:
        return DP[key]

    ans = (0, 0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                roll = d1 + d2 + d3
                if turn == 0:
                    new_p1 = (p1 + roll) % 10
                    new_s1 = new_p1 + s1 + 1

                    new_key = (1-turn, new_p1, p2, new_s1, s2)
                    ans1, ans2 = count(*new_key)
                    DP[new_key] = (ans1, ans2)
                    
                    ans = ((ans[0] + ans1), (ans[1] + ans2))
                else:
                    new_p2 = (p2 + roll) % 10
                    new_s2 = new_p2 + s2 + 1

                    new_key = (1-turn, p1, new_p2, s1, new_s2)
                    ans1, ans2 = count(*new_key)
                    DP[new_key] = (ans1, ans2)

                    ans = ((ans[0] + ans1), (ans[1] + ans2))
    return ans

print(count(0, 3, 7, 0, 0))
