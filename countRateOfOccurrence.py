#!/usr/local/bin/python3

normalNums = {}
powerBall = {}

count = 0

with open('Lnums', 'r') as lotto:
    for draw in lotto:
        i = 1;
        for numbers in draw.split():
            if i < 6:
                if numbers in normalNums:
                    normalNums[numbers] += 1
                else:
                    normalNums[numbers] = 1
            if i == 6:
                if numbers in powerBall:
                    powerBall[numbers] += 1
                else:
                    powerBall[numbers] = 1
            i += 1
        count += 1

print("\nThe percentage of each number being chosen over the last {} times is".format(count))

# sorted by number drawn
#for i in sorted(normalNums):
#    print(i, ':', normalNums[i], '%')

# sorted by percentage
for k in sorted(normalNums, key=normalNums.get, reverse=True):
    print(k, ':', ("%.2f" % (normalNums[k] * 100 / count)), "%")

print("\n\nThe distribution of the powerball over the last {} times is".format(count))

# sorted by number drawn
#for i in sorted(powerBall):
#    print(i, ':', powerBall[i], '%')

# sorted by percentage
for k in sorted(powerBall, key=powerBall.get, reverse=True):
    print(k, ':', ("%.2f" % (powerBall[k] * 100 / count)), "%")


