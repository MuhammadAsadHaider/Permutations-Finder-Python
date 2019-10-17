import random
import string
import time
from itertools import permutations
from copy import deepcopy

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
            allPermutations(num,results[num])
        return results[num]
    return helper


def allPermutations(num,res):
    res = list(res)    
    dataList = deepcopy(inputData)
    dataList.remove(res[0][0])
    r = [k if k != res[0][0] else i for i in dataList for j in res for k in j if i not in j]    
    t = [[r[i]]+[r[i+1]] for i in range(0,len(r)-1,2)]
    print(t)
    
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

def numGenerator(seed,n):
    r = [seed]
    temp = []
    inValid = {}
    inValid[seed] = 1
    i = 0
    while len(r)<n:
        num = r[i] + random.randint(1,1000000)
        if num not in inValid:
            for j in list(inValid.keys()):
                temp.append(j+num)
            for k in temp:
                inValid[k] = 1
            inValid[num] = 1
            r.append(num)
            i+=1
    return r

def preprocess(a):  # For Finding Repeated Items
    checkRepeat = {}
    repeated = {}   
    global inputData
    inputData = a 
    for i in range(len(a)):
        if (a[i] in checkRepeat):
            temp = a[i]
            a[i] = randomword()
            repeated[a[i]] = temp
        checkRepeat[a[i]] = 1
    r = list(checkRepeat)
    randNums = numGenerator(1,len(a))
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



testInput = "abcd"       #Example of string with repeated items

t1 = time.time()
print(len(main(testInput)))

print("Done", time.time() - t1, "seconds")



