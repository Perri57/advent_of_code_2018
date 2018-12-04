import re

if __name__ == "__main__":
    file = open("3-1_input.txt", "r")
    lines = file.read().split("\n")
    bigassarray = [[0,0,0,0,0] for x in range(len(lines))]

    regex_string = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    regex = re.compile(regex_string)
    for i in range(len(lines)):
        groups = regex.search(lines[i])
        bigassarray[i][0] = int(groups.group(1))
        bigassarray[i][1] = int(groups.group(2))
        bigassarray[i][2] = int(groups.group(3))
        bigassarray[i][3] = int(groups.group(4))
        bigassarray[i][4] = int(groups.group(5))
    
    for i in range(len(bigassarray)):
        overlapped = False
        rect1 = bigassarray[i]
        for j in range(len(bigassarray)):
            if i == j:
                continue
            else:
                rect2 = bigassarray[j]
                minx1 = rect1[1]
                miny1 = rect1[2]
                maxx1 = minx1 + rect1[3]
                maxy1 = miny1 + rect1[4]
                minx2 = rect2[1]
                miny2 = rect2[2]
                maxx2 = minx2 + rect2[3]
                maxy2 = miny2 + rect2[4]
                if maxx1 > minx2 and minx1 < maxx2 and maxy1 > miny2 and miny1 < maxy2:
                    overlapped = True
                    break
        if not overlapped:
            print(rect1[0])
            break
        