if __name__ == "__main__":
    file = open("2-1_input.txt", "r")
    lines = file.read().split("\n")
    str_len = len(lines[0])

    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            a = lines[i]
            b = lines[j]
            diff_count = []
            for k in range(str_len):
                if not a[k] == b[k]:
                    diff_count.append(k)
            if len(diff_count) == 1:
                print(a[:diff_count[0]] + a[diff_count[0] + 1:])

    
        
        