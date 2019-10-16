import random



def numGenerator(seed,n):
    r = [seed]
    temp = []
    inValid = {}
    inValid[seed] = 1
    i = 0
    while len(r)<n:
        num = r[i] + random.randint(1,1000)
        if num not in inValid:
            for j in list(inValid.keys()):
                temp.append(j+num)
            for k in temp:
                inValid[k] = 1
            inValid[num] = 1
            r.append(num)
            i+=1
    return r

print(numGenerator(1,10))