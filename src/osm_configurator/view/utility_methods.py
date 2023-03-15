from typing import Final

# Final Variables
EMPTY_CHARACTER: Final = " "
CONNECTION_CHARACTER: Final = "-"
DOTS: Final = "..."
SINGLE_DOT: Final = "."
LINE_BREAK: Final = "\n"


def reformat_string(string: str, line_length: int, rows: int, dots: bool, rows_unlimited: bool,
                    word_break: bool) -> str:
    """
    This Method takes a string and information on how to reformat it. It will reformat the string based in the
    other attributes, to make it look cleaner.
    It will cut the string into pieces by adding line breaks after a given amount of characters is met, and do this
    for the amount of rows asked for.
    Already existing Line breaks won't be overriden, instead will be used, as if the method has used one.
    If the given string is longer than what can be put in the given restrictions, the rest is simply ignored
    and deleted.

    Args:
        string (str): The string that shall be reformatted
        line_length (int): How many characters are allowed in one line, has to be positive
        rows (int): How many rows/line breaks are allowed max, can ent up being shorter, has to be positive
        dots (bool): States if dots '...' shall be added at the end of the string, if parts where cut, and line_length is at least 3
        rows_unlimited (bool): If True, then the row limit will be ignored
        word_break (bool): If True, words can be cut via '-', if False whole words get put in new rows if line_length
                           is met

    Returns:
        str: The new reformatted string
    """
    if line_length < 1:
        raise ValueError("line_length has to be positive integer!")
    if rows < 1:
        raise ValueError("rows has to be positive integer!")

    new_string: str = ""

    rows_left = rows

    string_length = len(string)

    index = 0
    last_empty_index = 0

    while rows_left > 0:
        characters_left = line_length

        # Going along a line and adding everything into the new string
        # Also remembering what the last empty character was
        new_row: bool = True
        while characters_left > 0:

            if index >= string_length:
                break

            if (string[index] == EMPTY_CHARACTER) and new_row:
                index += 1
                #characters_left -= 1
                continue

            new_string = new_string + string[index]
            if string[index] == EMPTY_CHARACTER:
                last_empty_index = index

            # If there is already a line break whe use it
            if string[index] == LINE_BREAK:
                if not rows_unlimited:
                    rows_left -= 1
                    if rows_left <= 0:
                        break

            index += 1
            characters_left -= 1
            new_row: bool = False

        if index >= string_length:
            break
        else:
            if rows_left == 1 and dots:
                # Only removing stuff till we hit a line break
                for x in range(3):
                    if not new_string[len(new_string) - 1] == LINE_BREAK:
                        new_string = new_string[0:len(new_string) - 1:1]
                    else:
                        break

                # Dots only will be added if we have the line_length can support 3 characters
                if line_length >= len(DOTS):
                    new_string = new_string + DOTS
            elif rows_left > 1 and word_break and (string[index] is not EMPTY_CHARACTER):
                # Deleting last character
                new_string = new_string[0:len(new_string) - 1:1]
                new_string = new_string + CONNECTION_CHARACTER
                # lowering the index by one, since the last character was just replaced by a connection symbol
                index -= 1

                new_string = new_string + LINE_BREAK
            else:
                new_string = new_string + LINE_BREAK

        if not rows_unlimited:
            rows_left -= 1

    return new_string
