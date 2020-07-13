state = 'B'
# gotomap[('E', 0)] = 1
with open('goto') as f:
    i = -1
    for line in f:
        line = line[:-1]
        i = i + 1
        if line == "N":
            continue
        else:
            print("gotomap[('%s', %d)] = %s" % (state, i, line))
