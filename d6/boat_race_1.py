import re

import colorama

from aoc_utils import read_input, print_colored_text


def clean_time_distance(input_lines):
    splitted_lines = [input_line.split(" ") for input_line in input_lines]
    time_input = [int(re.sub(r"\D", "", s)) for s in splitted_lines[0] if re.sub(r"\D", "", s).isnumeric()]
    distance_input = [int(re.sub(r"\D", "", s)) for s in splitted_lines[1] if re.sub(r"\D", "", s).isnumeric()]
    return splitted_lines, time_input, distance_input


def calculate_possibilities(time_input, distance_input):
    wins_poss_total = 1
    for index_time, race_time in enumerate(time_input):
        wins_poss_race = 0
        for time in range(race_time):
            press_time = velocity = time
            rec_distance = (race_time - press_time) * velocity
            if rec_distance > distance_input[index_time]:
                wins_poss_race += 1
        wins_poss_total = wins_poss_total * wins_poss_race if wins_poss_race > 0 else 1
    return wins_poss_total


def put_together_time_distances(input_lines):
    print(input_lines)
    time = re.sub(r"\D", "", input_lines[0])
    distance = re.sub(r"\D", "", input_lines[1])
    print(time)
    print(distance)
    return int(time), int(distance)


if __name__ == "__main__":
    colorama.init()
    input_lines = read_input("d6")
    splitted_lines, time_input, distance_input = clean_time_distance(input_lines)
    time_2, distances_2 = put_together_time_distances(input_lines)
    print(
        f"🎄🎅🎁{colorama.Fore.GREEN} --- INPUT PART 1 --- 🎄🎅🎁\nLINES: {splitted_lines} \nTime: {time_input} \nDistances: {distance_input}\n🎄🎅🎁 ------------- {colorama.Fore.RESET}🎄🎅🎁")
    print(
        f"🎄🎅🎁{colorama.Fore.LIGHTYELLOW_EX} --- INPUT PART 2 --- 🎄🎅🎁\nLINES: {splitted_lines} \nTime: {time_input} \nDistances: {distance_input}\n🎄🎅🎁 ------------- {colorama.Fore.RESET}🎄🎅🎁")
    win_poss_total_1 = calculate_possibilities(time_input, distance_input)
    win_poss_total_2 = calculate_possibilities([time_2], [distances_2])
    print_colored_text(f"PART 1 RESPONSE: {win_poss_total_1}", colorama.Fore.RED)
    print_colored_text(f"PART 2 RESPONSE: {win_poss_total_2}", colorama.Fore.GREEN)
