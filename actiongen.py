symbol = '$'

with open('action') as f:
    i = -1
    for line in f:
        line = line[:-1]
        i = i + 1
        if line == "N":
            continue
        else:
            new_line = line.split(' ')
            if new_line[0] == 's':
                print("actions_map[('%s', %d)] = 's %s'" % (symbol, i, new_line[1]))
            elif new_line[0] == 'r':
                left, right = ' '.join(new_line[1:]).split(',')
                print("actions_map[('%s', %d)] = 'r ' + str(prodID[('%s', '%s')])" % (symbol, i, left, right))
            else:
                print("actions_map[('%s', %d)] = 'a'" % (symbol, i))
