import Constants


def ft_sqrt(num):
    if num <= 0:
        return 0
    root = num / 3
    while True:
        last = root
        root = (root + num / root) / 2
        diff = root - last
        if -Constants.MINDIFF <= diff <= Constants.MINDIFF:
            break
    return root


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
    return 0


if __name__ == "__main__":
    main()
