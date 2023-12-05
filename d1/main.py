import re
import colorama

from aoc_utils import read_input, print_colored_text


def sum_pairs(input_lines):
    digits = [re.sub(r"\D", "", s) for s in input_lines]
    digits_to_sum = [[digit[0], digit[-1]] for digit in digits]
    total_sum = 0
    for pair_digit in digits_to_sum:
        total_sum += int(f"{pair_digit[0]}{pair_digit[1]}")
    return total_sum


# Press the green button in the gutter to run the script.
# Function to convert words to digits
def convert_words_to_digits(word_list):
    parse_dict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    return [parse_dict[word] if word in parse_dict else word for word in word_list]


def sum_pairs_words(input_lines):
    # print(input_lines)
    # digits = [re.sub(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b', '', s) for s in input_lines]
    converted_lists = [line.replace("one", "one1one")
                       .replace("two", "two2two")
                       .replace("three", "three3three")
                       .replace("four", "four4four")
                       .replace("five", "five5five")
                       .replace("six", "six6six")
                       .replace("seven", "seven7seven")
                       .replace("eight", "eight8eight")
                       .replace("nine", "nine9nine") for line in input_lines]
    """
    digits = [
        re.findall(r"(\*:one|two|three|four|five|six|seven|eight|nine|ten|\d)", line)
        #re.findall(f"one|two|three|four|five|six|seven|eight|nine|ten|1|2|3|4|5|6|7|8|9", line)
        for line in input_lines
    ]
    converted_lists = [convert_words_to_digits(sublist) for sublist in digits]"""
    total_sum = sum_pairs(converted_lists)
    return total_sum


if __name__ == "__main__":
    input_lines = read_input("d1")
    print(input_lines)
    total_sum_part1 = sum_pairs(input_lines)
    # BAD SOLUTION FOR PART 2 FIND ERROR:
    total_sum_part2 = sum_pairs_words(input_lines)
    print("🎄🎅🎁")
    print_colored_text(f"PART 1 RESPONSE: {total_sum_part1}", colorama.Fore.RED)
    print_colored_text(f"PART 2 RESPONSE: {total_sum_part2}", colorama.Fore.GREEN)
    print("🎄🎅🎁")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
