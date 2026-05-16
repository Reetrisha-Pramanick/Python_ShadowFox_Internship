count_1 = 0
count_6_inRows = 0
count_6 = 0
for i in range(25):
    round1 = int(input("Roll your dice for the 1st round: "))
    round2 = int(input("Roll your dice for the 2nd round: "))
    if round1 == 6 and round2 == 6:
        count_6_inRows = count_6_inRows + 1
        print("Number of times 6 in a row were rolled: ", count_6_inRows)
    if round1 == 6:
        count_6 = count_6 + 1
        print("Number of times a 6 was rolled: ", count_6)
    if round2 == 6:
        count_6 = count_6 + 1
        print("Number of times a 6 was rolled: ", count_6)
    if round1 == 1:
        count_1 = count_1 + 1
        print("Number of times a 1 was rolled: ", count_1)
    if round2 == 1:
        count_1 = count_1 + 1
        print("Number of times a 1 was rolled: ", count_1)
print("Number of times 6 in a row were rolled: ", count_6_inRows)
print("Number of times a 6 was rolled: ", count_6)
print("Number of times a 1 was rolled: ", count_1)
