import random


CARDINAL_DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def random_walk(n):
    """Return coordinates after 'n' step random walk"""
    x, y = 0, 0

    for _ in range(n):
        dx, dy = random.choice(CARDINAL_DIRECTIONS)
        x += dx
        y += dy
    return x, y


def monte_carlo_simulation(number_of_walks, walk_length, block_distance):
    """Return number of random walks that end within 'block_distance' of starting point"""
    no_transport = 0

    for walk in range(number_of_walks):
        x, y = random_walk(walk_length)
        distance = abs(x) + abs(y)

        if distance <= block_distance:
            no_transport += 1

    return no_transport


def main():
    block_distance = 5
    number_of_walks = 25_000

    print('Running {} rounds of monte carlo simulation per walk length...')
    print(f'Walk len | % closer than {block_distance} blocks')
    # Do walks with from block_distance to 25 steps
    # block_distance steps and less will always end within block_distance
    for walk_length in range(block_distance, 25):
        no_transport = monte_carlo_simulation(number_of_walks, walk_length, block_distance)
        no_transport_percentage = 100 * no_transport / number_of_walks
        print(f'     {walk_length}   |   {no_transport_percentage:.2f}')


if __name__ == '__main__':
    main()
