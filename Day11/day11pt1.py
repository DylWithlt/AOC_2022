
from dataclasses import dataclass
from itertools import zip_longest as izip_longest
import re


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


with open('./Day11/input.txt', 'r') as f:
    monkeys = []

    # Get all monkeys
    for group in grouper(f, 7, ''):
        monkey = {}

        digits = re.findall("\d+", group[1].strip())

        monkey["count"] = 0
        monkey["items"] = [int(x) for x in digits]

        operation = group[2][group[2].index("=") + 1:].strip()
        # old = 79
        #
        monkey["operation"] = lambda old, operation=operation: eval(operation)

        testDivisor = re.findall("\d+", group[3].strip())
        test = "True if x % " + testDivisor[0] + " == 0 else False"
        monkey["test"] = lambda x, test=test: eval(test)

        trueMonkey = re.findall("\d+", group[4].strip())
        monkey["ifTrue"] = int(trueMonkey[0])
        falseMonkey = re.findall("\d+", group[5].strip())
        monkey["ifFalse"] = int(falseMonkey[0])

        monkeys.append(monkey)

    def process_round():
        for monkey in monkeys:
            for item in monkey["items"]:
                monkey["count"] += 1

                original = item
                item = monkey["operation"](item)
                item = int(item/3)
                test = monkey["test"](item)

                targetMonkey = (monkey["ifTrue"]
                                if test else monkey["ifFalse"])
                monkeys[targetMonkey]["items"].append(item)
            monkey["items"].clear()

    for x in range(1000):
        process_round()

    newList = sorted(monkeys, key=lambda k: k['count'])

    product = 1
    for monk in newList[-2:]:
        product *= monk["count"]
    print(product)
