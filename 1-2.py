if __name__ == "__main__":
    file = open("1-1_input.txt", "r")
    lines = file.read()
    freq = 0
    past_freq = set()
    past_freq.add(freq)
    found = False

    while not found:
        for line in lines.split("\n"):
            if not line == "":
                freq = freq + int(line)
                if freq in past_freq:
                    found = True
                    break
                else:
                    past_freq.add(freq)
    
    print(freq)