# 조합, itertools를 이용
import argparse
import itertools
import timeit


def measure_time(func):
    def wrapper(*args, **kwargs):
        result = None
        execution_time = timeit.timeit(lambda: func(*args, **kwargs), number=10000000)
        print(f"############ Execution time for {func.__name__}: {execution_time:.4f} seconds")
        return result

    return wrapper

@measure_time
def make_ncr_with_library(animals, grouped_animals):
    c = itertools.combinations(animals, grouped_animals)
    return len(list(c))


# 조합, 직접 구현
def factorial(nr):
    result = 1
    for i in range(1, nr+1):
        result = result * i
    return result


@measure_time
def make_ncr(n, r):
    return int(factorial(n) / ((factorial(n-r)) * factorial(r)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Echo your input')
    parser.add_argument('--n', help='number of animals')
    parser.add_argument('--r', help='number of grouped animals')
    args = parser.parse_args()
    number_of_animals = int(args.n)
    grouped_animals = int(args.r)

    animals = (i for i in range(number_of_animals))

    make_ncr_with_library(animals, grouped_animals)
    make_ncr(number_of_animals, grouped_animals)

############ Execution time for make_ncr_with_library: 1.9908 seconds
############ Execution time for make_ncr: 6.6465 seconds