testval = 1e9

for n in range(int(1e6)):
    testval += 1e-6

print(testval - 1e9)