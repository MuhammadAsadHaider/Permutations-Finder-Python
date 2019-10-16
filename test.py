import random
import string
import time



def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))


def memoize(f):
    results = {}
    def helper(a):
        if str(a) not in results:
            results[str(a)] = f(a)
        return results[str(a)]
    return helper


@memoize
def task(a):   
    res = [] 
    if (len(a) == 1):
        return a
    if (len(a) == 2):
        return [a[0]] + [a[1]], [a[1]] + [a[0]]    
    k = task(a[1:])  
    for l in k:
        res.append(l)  
    return res

def finaliser(a):
    t = task(a)
    print(t)
    r = [[a[i]]+[a[i-1] if wd == a[i] else wd for wd in j] for i in range(len(a)) for j in t]
    return r

finaliser("abcde")



def preprocess(a):  # For Finding Repeated Items
    checkRepeat = {}
    repeated = {}
    for i in range(len(a)):
        if (a[i] in checkRepeat):
            temp = a[i]
            a[i] = randomword()
            repeated[a[i]] = temp
        checkRepeat[a[i]] = 1
    return list(checkRepeat), repeated


def main(a):
    a = list(a)
    final = {}
    x, y = preprocess(a)
    result = finaliser(x)
    if (len(y) == 0):
        return result
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] in y:
                result[i][j] = y[result[i][j]]
        final["".join(str(z) for z in result[i])] = result[i]
    return list(final.values())



# testInput = "123456789a"

# t = time.time()
# print(len(main(testInput)))

# print("Done", time.time() - t, "seconds")





