def engine_one(regex, string):
    return regex == '' or regex == '.' or match_literally(regex, string)


def match_literally(regex, string):
    return regex == string


def engine_two(regex, string):
    if len(string) == 0:
        return len(regex) == 0
    elif len(regex) == 0:
        return True
    elif regex[0] == '\\':
        return engine_two(regex[1::], string)
    elif len(regex) > 1 and regex[1] in "?*+":
        if regex[0] == '.':
            return regex[1] == '*' or \
                   (regex[1] == '+' and engine_one(regex[0], string[0])) or \
                   (regex[1] == '?' and engine_two(regex[0], string))
        result = handle_optional_metacharacters(regex[0], regex[1], string)
        if result is not None:
            return engine_two(regex[2::], result)
        else:
            return False
    elif not engine_one(regex[0], string[0]):
        return False
    else:
        return engine_two(regex[1::], string[1::])


def engine_three(regex, string):
    if engine_two(regex, string):
        return True
    elif len(string) <= len(regex.replace("\\", "")):
        return False
    else:
        return engine_three(regex, string[1::])


def engine_four(regex, string):
    if regex.startswith("^") and regex.endswith("$"):
        return engine_two(regex[1:len(regex) - 1], string) and \
               engine_two(reverse_regex(regex[1: len(regex) - 1]), string[::-1])
    elif regex.startswith("^"):
        return engine_two(regex[1:len(regex)], string)
    elif regex.endswith("$"):
        return engine_two(reverse_regex(regex[0: len(regex) - 1]), string[::-1])
    else:
        return engine_three(regex, string)


# def engine_four(regex, string):
#     if regex.startswith("^") and regex.endswith("$"):
#         return engine_two(regex[1:len(regex) - 1], string) and \
#                engine_two(regex[1: len(regex) - 1][::-1], string[::-1])
#     elif regex.startswith("^"):
#         return engine_two(regex[1:len(regex)], string)
#     elif regex.endswith("$"):
#         return engine_two(regex[0: len(regex) - 1][::-1], string[::-1])
#     else:
#         return engine_three(regex, string)

def handle_optional_metacharacters(char, meta, string):
    if meta == "?":
        return zero_or_one(char, string)

    elif meta == "+":
        return zero_or_more(char, string) if len(string) != 0 and engine_one(char, string[0]) else None
    elif meta == "*":
        return zero_or_more(char, string)


def zero_or_one(char, string):
    if len(string) == 0 or not engine_one(char, string[0]):
        return string
    else:
        return string[1::]


def zero_or_more(char, string):
    if len(string) == 0 or not engine_one(char, string[0]):
        return string
    else:
        return zero_or_more(char, string[1::])


def reverse_regex(regex):
    result = ""
    prev = ""
    for i in range(len(regex)):
        char = regex[i]
        if char in "?*+":
            result = result[:len(result) - 1] + char + result[len(result) - 1]
        elif prev == "\\":
            result = result[:len(result) - 1] + char + prev
        else:
            result = result + char

        prev = char

    return result[::-1]


if __name__ == "__main__":


    inputs = input()

    split_input = inputs.split("|")

    reg = split_input[0]
    st = split_input[1]

    print(engine_four(reg, st))



