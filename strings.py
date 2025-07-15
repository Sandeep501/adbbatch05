# name = "Harish"
# # print(name[2])
# print(name[0:4]) # -> Hari
# print(name[0:4:2])
# print(name[:4:2])
# print(name[::2]) # --> length of var + 1 for stop
# print(name[::])
# print(name[:4])
# print(name[:])
# index -> [start: stop: step=1]
# H-0, a-1, r-2, i-3 ... h-5


# marvel = (input("Enter any charecter: ")).strip()

# " Good Morning         "


marvel = "antmantbdvsdtbbhst"

# a-0, n-1, t-2, m-3, a-4, n-5, t-6

# I-0, r-1, o-2, n-3, M-4, a-5, n-6 (-1)

# print(marvel[4:])
# print(marvel[4])
# print(marvel[6])
# print(marvel[-1])
# print(type(marvel))
print(marvel.index('a', 1))
# print(marvel.upper())
# print(marvel.replace("@", ""))
# print(marvel[2])
print(marvel.index('t', 2))
