iq_levels = [('Rohan', 51), ('Raphael', 89), ('Chris', 67), ('Dan', 86)]
print("list")
print(iq_levels)

iq_levels.sort(key = lambda z: z[1])
print("sorted tuple: ")
print(iq_levels)
