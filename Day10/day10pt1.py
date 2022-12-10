cycles = [20, 60, 100, 140, 180, 220]

with open('./Day10/input.txt', 'r') as f:
    signals = [1]

    lines = f.readlines()
    for line in lines:
        info = line.strip().split()

        if info[0] == 'addx':
            X = 1 if len(signals) <= 0 else signals[-1]
            signals.append(X)
            signals.append(X + int(info[1]))
        else:
            X = 1 if len(signals) <= 0 else signals[-1]
            signals.append(X)
    print(signals)
    strenghts = []
    for x in cycles:
        strenghts.append(signals[x-1] * x)

    print(strenghts)
    print(sum(strenghts))
