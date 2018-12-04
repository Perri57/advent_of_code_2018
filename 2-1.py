if __name__ == "__main__":
    file = open("2-1_input.txt", "r")
    lines = file.read()
    num_twice = 0
    num_thrice = 0

    for line in lines.split("\n"):
        if not line == "":
            count = {}
            twice = False
            thrice = False
            for char in line:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] = count[char] + 1
            for char in count:
                if count[char] == 2:
                    twice = True
                elif count[char] == 3:
                    thrice = True
            if twice:
                num_twice = num_twice + 1
            if thrice:
                num_thrice = num_thrice + 1
    
    print(num_twice * num_thrice)
            