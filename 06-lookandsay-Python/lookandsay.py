# First, you can read about look-and-say as here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
    print(type(a))
    b = ''.join(map(str, a))
    print(b)
    result = []
    repeat = b[0]
    a = b[1:]+" "
    count = 1
    for item in b:
        if item != repeat:
            result.append((str(count),repeat))
            count = 1
            repeat = item
        else:
            count += 1
    return result

print(lookandsay([3,3,4,4,5,6,6,7,7]))