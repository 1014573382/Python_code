
with open('data.txt', 'r') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break