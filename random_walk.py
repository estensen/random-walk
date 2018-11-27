import random


CARDINAL_DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def random_walk(n):
    """Return coordinates after n step random walk"""
    x, y = 0, 0

    for _ in range(n):
        dx, dy = random.choice(CARDINAL_DIRECTIONS)
        x += dx
        y += dy
    return x, y


# Try 25 times
for i in range(1, 25):
    walk = random_walk(i)
    print(f'{walk} Distance from home {abs(walk[0]) + abs(walk[1])}')
