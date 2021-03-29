def test(s, last):
    if last < 0:
        return 0

    if s[-1] == "0":
        return 2 * test(s, last - 1)

    return 1 + 2 * test(s, last - 1)


test("110100111", 4)
print(test("110100111", 4))