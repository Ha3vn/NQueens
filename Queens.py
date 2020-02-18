import time


def main():

    n = 0
    # prompts the user for a value of n between 1 and 16 inclusive
    while n < 1 or n > 16:
        n = int(input("Enter the size of board: "))
    print()
    # establishes a domain of the coordinates of all queens
    domain = set()
    # fills domain
    for row in range(n):
        for col in range(n):
            domain.add((row, col))
    # creates a set of incompatible points with a queen's position and removes them from domain
    incomp = {}
    for pos in domain:
        row, col = pos
        incomp[pos] = []
        inc = incomp[pos]
        for a in domain:
            if pos == a:
                continue
            # checks rows and diagonals
            dR = a[0] - row
            dC = a[1] - col
            if a[0] == row or row + dC == a[0] or col - dR == a[1]:
                inc.append(a)

    print("Number of solutions: " + str(rec_back(domain, n, incomp)))


def rec_back(domain, num, inc):

    # base cases
    if num == 0:
        return 1
    if len(domain) < num:
        return 0

    sum = 0
    # creates a list of points removed to add back in at the parent call's level
    removed2 = []
    # creates a copy of domain to iterate though
    copy = tuple(domain)
    num = num - 1
    for x in copy:
        # places one queen per column
        if x[1] != num:
            continue
        removed = []
        removed2.append(x)
        domain.remove(x)
        # removed incompatible points
        for a in inc[x]:
            if a in domain:
                domain.remove(a)
                removed.append(a)
        # recursive call
        sum += rec_back(domain, num, inc)
        # reintroduces removed points from a backtracked method
        domain.update(removed)
    domain.update(removed2)
    return sum


def hello():
    for i in range(1, 10):
        print("N: " + str(i))
        start = time.time()
        main(i)
        print("Elapsed: " + str((time.time() - start)) + " seconds")


# import profile
# profile.run('hello()')


hello()
