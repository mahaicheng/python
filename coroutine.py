def rangeN(a, b):
    i = a
    while i < b:
        yield i
        i += 1


if __name__ == "__main__":
    for i in rangeN(1, 10):
        print(i)
