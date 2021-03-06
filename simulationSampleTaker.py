from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

UNI_DIM = 100


def shuffle_list(list):
    dim = len(list)
    for i in range(dim-1, -1, -1):
        j = random.randrange(0,i+1)
        temp = list[i]
        list[i] = list[j]
        list[j] = list[i]

    return list

# simulating universe as a 2D array of 1's and 0's
def init_univ(dim):
    universe = []

    for i in range(dim*dim/2):
        universe.append(1)
        universe.append(-1)

    universe = shuffle_list(universe)

    #print sum(universe)
    return universe

def get_sample(universe, dim, x_start, y_start):
    sample = []
    for i in range(dim):
        for j in range(dim):
            sample.append(universe[(y_start + i)*UNI_DIM + x_start + j])

    return sample

def print_array(array, dim):
    for i in range(len(array)):
        if i%dim == 0:
            print()
        print(str(array[i]) + ", ", end="")
    print()

# gets the symmetry of an array, assumes array is square and elements
# are either -1 or 1
def symmetry(my_list, dim):
    #print(my_list)
    return float(sum(my_list)) / (dim*dim)

def random_sample(universe, dim):
    x_start = random.randrange(0,UNI_DIM - dim)
    y_start = random.randrange(0,UNI_DIM - dim)

    return get_sample(universe, dim, x_start, y_start)

def list_of_symmetries(universe, sample_dim, length):
    s_list = []

    for i in range(length):
        s_list.append(symmetry(random_sample(universe, sample_dim),sample_dim))

    return s_list

def main():
    UNI_DIM = SAMPLE_DIM*10
    if FIXED_UNIVERSE_SIZE:
        UNI_DIM = 1000
    universe = init_univ(UNI_DIM)

    my_list = list_of_symmetries(universe, SAMPLE_DIM, 1000)
    #print(my_list)
    print("For universe with dimension: " + str(UNI_DIM) + 
            " the standard deviation of samples is:\n" + str(np.std(my_list)))

    plt.hist(my_list)
    plt.title(str(SAMPLE_DIM) + " Sample Asymmetries with universe size: " 
            + str(UNI_DIM) + "\nStdev: " + str(np.std(my_list))
            + " mean: " + str(np.mean(my_list)))
    plt.xlabel("Asymmetry")
    plt.ylabel("Number of Samples")
    if FIXED_UNIVERSE_SIZE:
        plt.savefig(str(SAMPLE_DIM) + "_sample_fixed.png")
    else:
        plt.savefig(str(SAMPLE_DIM) + "_sample.png")
    #plt.show()

#for UNI_DIM in range(40, 8000, 50):
#    main()

SAMPLE_DIM = int(sys.argv[1])
if len(sys.argv) == 3:
    FIXED_UNIVERSE_SIZE = True
else:
    FIXED_UNIVERSE_SIZE = False

if (FIXED_UNIVERSE_SIZE):
    print("Fixed universe size at 1000")

main()
