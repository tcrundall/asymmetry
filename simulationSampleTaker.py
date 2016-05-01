import random

UNI_DIM = 1000


# simulating universe as a 2D array of 1's and 0's
def init_univ(dim):
    universe = []

    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(random.randrange(-1,2,2))

        universe.append(row)

    sum = 0
    for i in range(dim):
        for j in range(dim):
            sum = sum + universe[i][j]

    return universe

def get_sample(universe, dim, x_start, y_start):
    sample = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(universe[y_start + i][x_start + j])

        sample.append(row)

    return sample

def print_array(array):
    for row in array:
        print row

# gets the symmetry of an array, assumes array is square and elements
# are either -1 or 1
def symmetry(array):
    dim = len(array)
    
    sum = 0
    for row in array:
        for element in row:
            sum = sum + element

    return float(sum) / (dim*dim)

def random_sample(universe, dim):
    x_start = random.randrange(0,UNI_DIM - dim)
    y_start = random.randrange(0,UNI_DIM - dim)

    return get_sample(universe, dim, x_start, y_start)

def list_of_symmetries(universe, dim, length):
    list = []

    for i in range(length):
        list.append(symmetry(random_sample(universe, dim)))

    return list

def main():
    universe = init_univ(UNI_DIM)
    sample = get_sample(universe, 5, 5, 5)
    print symmetry(universe)

    print

    print list_of_symmetries(universe, UNI_DIM/10, 10)

main()
