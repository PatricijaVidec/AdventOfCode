# PART 1

# find the word XMAS horizontally, vertically, diagonally, backwards, or even overlapping other words

with open('input.txt') as file:
    grid = [line.strip() for line in file]

target_word = "XMAS"
word_length = len(target_word)
rows, cols = len(grid), len(grid[0])

# Directions: (dx, dy)
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)
]


# Count occurrences
def count_occurrences():
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if all(
                        0 <= x + i * dx < rows and
                        0 <= y + i * dy < cols and
                        grid[x + i * dx][y + i * dy] == target_word[i]
                        for i in range(word_length)):

                    count += 1
    return count


print(count_occurrences())
