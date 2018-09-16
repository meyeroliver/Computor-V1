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
