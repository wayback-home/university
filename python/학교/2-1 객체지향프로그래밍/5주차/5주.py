x = 1
y = x
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

y += 1
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = "abc"
y = x
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

y += "def"
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = [1, 2, 3]
y = x
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

y.append(4)
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = (1, 2, 3)
y = x
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

# y.append(4)
# print("\n" * 2)
# print(f"x = {x}, id(x) = {id(x)}")
# print(f"y = {y}, id(y) = {id(y)}")

y += (4,)
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = {1: 2}
y = x
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

y[2] = 3
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = [1, 2, 3]
y = x[:]
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

import copy

x = [1, 2, 3]
y = copy.deppcopy(x)
print("\n" * 2)
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")