# PART 1
# import the library that has regex
import re

with open('input.txt') as file:
    # calculate the total sum of results from valid `mul` instructions
    print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file.read())))

# PART 2

# corrected regex pattern
# capture mul, do, and don't as separate groups
with open('input.txt') as file:
    # new pattern, added do and don't
    instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", file.read())

total_sum = 0  # tracking the sum
skip = False  # do we skip the sum or not

for match in instructions:
    if match[3]:  # match do
        skip = False  # resume processing mul
    elif match[4]:  # match don't
        skip = True  # skip mul
    elif match[1] and match[2] and not skip:  # valid mul(X,Y)
        total_sum += int(match[1]) * int(match[2])

print(total_sum)
