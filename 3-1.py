import re

if __name__ == "__main__":
    file = open("3-1_input.txt", "r")
    lines = file.read().split("\n")
    bigassarray = [[0 for x in range(1000)] for y in range(1000)]

    regex_string = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    regex = re.compile(regex_string)
    for line in lines:
        groups = regex.search(line)
        id = int(groups.group(1))
        x = int(groups.group(2))
        y = int(groups.group(3))
        w = int(groups.group(4))
        h = int(groups.group(5))
        for i in range(w):
            for j in range(h):
                bigassarray[x + i][y + j] = bigassarray[x + i][y + j] + 1
    
    count = 0
    for list in bigassarray:
        for x in list:
            if x > 1:
                count = count + 1
    print(count)