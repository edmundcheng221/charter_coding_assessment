"""

Ex: "xxxy", 2 => "xxy"
Ex: "xxyy", 1 => "xy"
Ex: "xxxxyyyyxx", 1 => "xyx"

"""


def formatString(string:str, max_num:int):
    output = ""
    previous = None
    current = 1
    for current_char in string:
        if current_char == previous and current < max_num:
            current += 1
            output += current_char
        else:
            if current_char != previous:
                current = 1
                output += current_char
        previous = current_char
    return output


if __name__ == '__main__':
    print(formatString("xxxxyyyyxx", 1))