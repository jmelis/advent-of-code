DP = {}
def count(p1, p2, s1, s2, first=False):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    if first:
        p1 = p1 - 1
        p2 = p2 - 1

    key = (p1, p2, s1, s2)
    if key in DP:
        return DP[key]

    ans = (0, 0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                roll = d1 + d2 + d3
                new_p1 = (p1 + roll) % 10
                new_s1 = new_p1 + s1 + 1

                new_key = (p2, new_p1, s2, new_s1)
                ans1, ans2 = count(*new_key)

                ans = ((ans[0] + ans2), (ans[1] + ans1))
                DP[new_key] = (ans1, ans2)
                    
    return ans

ans = count(4, 8, 0, 0, True)
print(max(ans))
