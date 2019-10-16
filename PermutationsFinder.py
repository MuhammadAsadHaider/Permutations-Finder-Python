import random
import string
import time
from itertools import permutations

numberMap = {}

def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))

def sumOfNumMap(a):
    return sum([numberMap[i] for i in a])

def memoize(f):
    results = {}
    def helper(a):
        num = sumOfNumMap(a)
        if num not in results:
            results[num] = f(a)
        return results[num]
    return helper



@memoize
def task(a):
    res = []
    if (len(a) == 1):
        return a
    if (len(a) == 2):
        return [a[0]] + [a[1]], [a[1]] + [a[0]]
    for i in range(len(a)):
        k = [[a[i]] + j for j in task(a[:i] + a[i + 1:])]
        for l in k:
            res.append(l)
    return res



def preprocess(a):  # For Finding Repeated Items
    checkRepeat = {}
    repeated = {}    
    for i in range(len(a)):
        if (a[i] in checkRepeat):
            temp = a[i]
            a[i] = randomword()
            repeated[a[i]] = temp
        checkRepeat[a[i]] = 1
    r = list(checkRepeat)
    randNums = random.sample(range(1, 100), len(r)) 
    for j,k in enumerate(r):        
        numberMap[k] = randNums[j]
    return r, repeated


def main(a):
    a = list(a)
    final = {}
    x, y = preprocess(a)
    result = task(x)
    if (len(y) == 0):
        return result
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] in y:
                result[i][j] = y[result[i][j]]
        final["".join(str(z) for z in result[i])] = result[i]
    return list(final.values())



testInput = "123456789"       #Example of string with repeated items

t1 = time.time()
main(testInput)

print("Done", time.time() - t1, "seconds")




