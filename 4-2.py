import re

if __name__ == "__main__":
    file = open("4-1_input.txt", "r")
    lines = file.read().split("\n")
    lines.sort()

    regex_string = "\[\d{4}-\d{2}-\d{2} \d{2}\:(\d{2})\] ([\w\d# ]+)"
    regex_1 = re.compile(regex_string)
    regex_string = "Guard #(\d+) begins shift"
    regex_2 = re.compile(regex_string)

    current_guard = 0
    start_minute = -1
    end_minute = -1
    guard_sleep = {}
    for line in lines:
        groups_1 = regex_1.search(line)
        message = groups_1.group(2)
        groups_2 = regex_2.search(message)
        if groups_2 == None:
            if message == "falls asleep":
                start_minute = int(groups_1.group(1))
            elif message == "wakes up":
                end_minute = int(groups_1.group(1))
                if current_guard not in guard_sleep:
                    guard_sleep[current_guard] = [0 for x in range(60)]
                for i in range(start_minute, end_minute):
                    guard_sleep[current_guard][i] += 1
        else:
            current_guard = int(groups_2.group(1))
    
    high_freq_sleepiest_minute = -1
    best_sleepiest_minute = -1
    sleepiest_guard = -1
    for guard in guard_sleep:
        freq_sleepiest_minute = max(guard_sleep[guard])
        if freq_sleepiest_minute > high_freq_sleepiest_minute:
            high_freq_sleepiest_minute = freq_sleepiest_minute
            best_sleepiest_minute = guard_sleep[guard].index(freq_sleepiest_minute)
            sleepiest_guard = guard

    
    print(sleepiest_guard * best_sleepiest_minute)



        