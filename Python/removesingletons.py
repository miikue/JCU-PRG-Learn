

pool = [2, 5, 3, 6, 2, 5, 7, 3]

def non_unique(pool):
    for i in pool:
        if pool.count(i) == 1:
            pool.remove(i)



print(non_unique(pool), pool)