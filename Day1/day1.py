with open('input.txt', 'r') as f:
    elvesCaloryCount = dict([])
    elf = 1

    for line in f.readlines():
        if line.strip() == "":
            elf += 1
            continue
        if not elf in elvesCaloryCount:
            elvesCaloryCount[elf] = 0
        elvesCaloryCount[elf] += int(line.strip())

    k = [x
         for x in sorted(elvesCaloryCount.values(), reverse=True)]

    print(k[1])
    print(sum(k[:3]))
