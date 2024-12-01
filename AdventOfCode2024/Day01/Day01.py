#PART 1

# open the file name, read the lines and then split into two parts, that we put into the left and right list
left_list, right_list = zip(*[map(int, line.split()) for line in open('input.txt')])

# Sort the list from the smallest number to the biggest
left_sorted, right_sorted = sorted(left_list), sorted(right_list)

# Calculate the total distance by summing the absolute differences (because some are negative)
total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

print(total_distance)
#result

#PART 2

#i go through the left_list and for every the same number that's the same as the left one i multiply
similarity_score = sum(left * right_list.count(left) for left in left_list)
print(similarity_score)
