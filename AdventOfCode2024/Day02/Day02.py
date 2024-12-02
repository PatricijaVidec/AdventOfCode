# PART 1
# we have a sequence of 5 numbers, and we have to check if they are safe
# the level will be safe if the numbers are either only ** decreasing ** or only ** increasing **
# the levels can only differ by at least 1 or at most 3

# at the end we count how many reports are safe !

def safe_report(report):
    # checking if a report is safe based on the given criteria
    levels = list(map(int, report.split()))
    # calculates the differences between the levels (to se if there's an increase or decrease)
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # checking if all differences are either positive or negative
    increasing = all(diff > 0 for diff in differences)
    decreasing = all(diff < 0 for diff in differences)

    # checking if all differences are between 1 and 3 (where the 3 is also valid)
    valid = all(1 <= abs(diff) <= 3 for diff in differences)

    return (increasing or decreasing) and valid

def count_safe_reports():
    # lastly I upen up the file, I sum up all the save files, and apply the criteria I set up in the function above
    with open('input.txt') as file:
        return sum(safe_report(line.strip()) for line in file if line.strip())

# I print out the result of the safe reports
print(count_safe_reports())


# PART 2
