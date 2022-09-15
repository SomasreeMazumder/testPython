'''def print_rangoli(size):
    width = size * 4 - 3
    string = ''

    for i in range(1, size + 1):
        for j in range(0, i):
            string += chr(96 + size - j)
            if len(string) < width:
                string += '-'
        for k in range(i - 1, 0, -1):
            string += chr(97 + size - k)
            if len(string) < width:
                string += '-'
        print(string.center(width, '-'))
        string = ''

    for i in range(size - 1, 0, -1):
        string = ''
        for j in range(0, i):
            string += chr(96 + size - j)
            if len(string) < width:
                string += '-'
        for k in range(i - 1, 0, -1):
            string += chr(97 + size - k)
            if len(string) < width:
                string += '-'
        print(string.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
'''





def print_rangoli(size):
    # your code goes here
    import string as p
    design = p.ascii_lowercase
    #print(design)
    L = []
    # print("valueL",L)
    for i in range(n):
        #print("ivalue", i)
        #print("nvalue", n)
        #m = design[i:n]
        #print("mvalue", m)

        s = "-".join(design[i:n])
        #print("svalue", s)


        #print(s[1:])
        #print(s[::-1])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
        #print(L)
    print('\n'.join(L[:0:-1] + L))
    #print(L[:0:-1])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
