import Constants


def ft_sqrt(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    root = float(num / 3)
    while True:
        last = root
        root = (root + num / root) / 2
        diff = float(root - last)
        if -Constants.MINDIFF <= diff <= Constants.MINDIFF:
            break
    return root


def ft_abs(num):
    return -1 * num


def ft_complex(real, imaginary):
    my_complex = []
    my_complex.append(real / 2)
    my_complex.append(imaginary/2)
    return my_complex


def ft_power(num, power):
    i = 0
    summer = 1
    while True:
        if i >= power:
            break
        summer *= num
        i += 1
    return summer


def main():
    print(ft_sqrt(1))


if __name__ == "__main__":
    main()
