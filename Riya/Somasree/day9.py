def three_sum(n):
    result = []
    n.sort()
    print(n)

    # for i in range(len(n) - 2):
    # print('iiiiiiiiiii',i)

    for i in range(len(n) - 2):
        # print('iiiiiiiiiiiiiiiiii', n[-1])
        if i > 0 and n[i] == n[i - 1]:
            continue

        l, r = i + 1, len(n) - 1
        print('ifirst', i)
        print('lfirst', l)
        print('rfirst', r)
        while l < r:
            s = n[i] + n[l] + n[r]
            if s > 0:
                r -= 1
                # print('rrrrrrrrrrrrrrrr', r)
            elif s < 0:
                l += 1
                # print('lllllllllllllllll', l)
            else:
                result.append((n[i], n[l], n[r]))
                # print(result)
                print('n[r]', n[r])
                r -= 1
                print("l,r", l, r)
            '''  while l < r and n[l] == n[l + 1]:
                  l += 1'''
            while l < r and n[r] == n[r - 1]:
                r -= 1
                l += 1
                return result

                # r -= 1


x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
print(three_sum(x))
