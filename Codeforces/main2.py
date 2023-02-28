import itertools
from collections import deque
import math

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def insr2():
    s = input()
    return list(s[:len(s)])
def invr(): return map(int, input().split())

tc = inp()
for i in range(0, tc):
    n, m = invr()
    p = inlt()
    ini = list(range(1, n + 1))
    res = [0] * 999
    count = 0
    index = 0
    for ip in p:
        tempini = ini.copy()
        if ip in ini:
            ini.remove(ip)
            ini.insert(0, ip)
            count += 1
            continue
        ini.insert(0, ip)
        ini.pop()
        if ini != tempini:
            count += 1
            res[-index - 1] = count
        else:
            res[-index - 1] = -1
        index += 1
    for i in range(0, len(res)):
        if res[i] == 0:
            res[i] = -1
    res = res[-n:]
    # print as string
    print(' '.join(map(str, res)))














