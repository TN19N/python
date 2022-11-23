from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce


if __name__ == '__main__' :

    x = [1, 2, 3, 4, 5]

    print(ft_map(lambda dum: dum + 1, x))

    print(list(ft_map(lambda t: t + 1, x)))

    print(ft_filter(lambda dum: not (dum % 2), x))

    print(list(ft_filter(lambda dum: not (dum % 2), x)))

    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

    print(ft_reduce(lambda u, v: u + v, lst))
