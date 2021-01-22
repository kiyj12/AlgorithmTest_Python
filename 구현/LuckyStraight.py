score = input()

half = int(len(score) / 2)

sum_one = 0
sum_two = 0

for i in range(half):
    sum_one += int(score[i])

for i in range(half,len(score)):
    sum_two += int(score[i])

if sum_one == sum_two:
    print("LUCKY")
else:
    print("READY")