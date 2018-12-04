if __name__ == "__main__":
    file = open("1-1_input.txt", "r")
    lines = file.read()
    freq = 0

    for line in lines.split("\n"):
        if line == "":
            continue
        freq = freq + int(line)
    
    print(freq)