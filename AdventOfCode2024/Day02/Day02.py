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
    # lastly I open up the file, I sum up all the save files, and apply the criteria I set up in the function above
    with open('input.txt') as file:
        return sum(safe_report(line.strip()) for line in file if line.strip())


# I print out the result of the safe reports
print(count_safe_reports())


# PART 2
def safe_report2(levels):
    # checking if a report is safe
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    return (all(1 <= abs(d) <= 3 for d in differences)  # between 1 and 3 (inclusive), returns true if it is
            and (all(d > 0 for d in differences)  # check is positive
            or all(d < 0 for d in differences)))  # checks if negative

# it can only contain either negatives or positives ^^


def can_be_safe(report):
    # checking if a report can be made safe by removing one level
    levels = list(map(int, report.split()))
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]  # remove the level at index i
        if safe_report2(modified_levels):  # checking if anything changed by calling the func safe_report2
            return True
    return False


def count_safe_reports2():
    with open('input.txt') as file:
        data = [line.strip() for line in file if line.strip()]
    return sum(safe_report2(list(map(int, report.split()))) or can_be_safe(report) for report in data)


print(count_safe_reports2())
