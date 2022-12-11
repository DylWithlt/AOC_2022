
from dataclasses import dataclass
from itertools import zip_longest as izip_longest
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from functools import cache
import re


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


with open('./Day11/input.txt', 'r') as f:
    monkeys = {}

    # Get all monkeys
    lcm = 1
    monkCount = 0
    for group in grouper(f, 7, ''):
        monkey = {}
        operation = group[2][group[2].index("=") + 1:].strip()

        digits = re.findall("\d+", group[1].strip())

        monkey["count"] = 0
        monkey["items"] = [int(x) for x in digits]

        # old = 79
        #
        monkey["operation"] = cache(
            lambda old, operation=operation: eval(operation))

        testDivisor = re.findall("\d+", group[3].strip())
        lcm *= int(testDivisor[0])
        test = "True if x % " + testDivisor[0] + " == 0 else False"
        monkey["test"] = cache(lambda x, test=test: eval(test))

        trueMonkey = re.findall("\d+", group[4].strip())
        monkey["ifTrue"] = int(trueMonkey[0])
        falseMonkey = re.findall("\d+", group[5].strip())
        monkey["ifFalse"] = int(falseMonkey[0])

        monkeys[monkCount] = monkey
        monkCount += 1

    def processItem(monkey, item):
        monkey["count"] += 1

        item = monkey["operation"](item) % greatest_divisor
        #item = int(item/3)
        test = monkey["test"](item)

        targetMonkey = (monkey["ifTrue"]
                        if test else monkey["ifFalse"])
        monkeys[targetMonkey]["items"].append(item)

    def process_round():
        for monkey in monkeys.values():
            with ThreadPoolExecutor() as ex:
                futures = [ex.submit(processItem, monkey, item)
                           for item in monkey["items"]]
                done = wait(
                    futures, return_when=ALL_COMPLETED)
                monkey["items"].clear()

    for x in range(10000):
        if x % 1000 == 0:
            print("X = ", x)
            for monk in monkeys.values():
                print(monk["items"])
            print("----------")
        process_round()

    newList = sorted(monkeys.values(), key=lambda k: k['count'])

    product = 1
    for monk in newList[-2:]:
        product *= monk["count"]
    print(product)
