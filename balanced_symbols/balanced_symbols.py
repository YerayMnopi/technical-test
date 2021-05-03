from collections import deque


class BalancedSymbols:
    """
    Checks if a given string is balanced.

    Attributes:
        symbols: The opening and closing symbols to check is the string is porpertly balanced.
        comments: The strings that indicates the opening and closing of a comment.
        stack: It stores the opened symbols
        bypass_mode: If the bypass mode is enabled, the check of balanced symbols is disabled. Useful for comments.
    """

    symbols = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    comments = ('/*', '*/')

    stack = deque()

    bypass_mode = False

    def __init__(self):
        self.count = 0

    def check_str_is_balanced(self, string_to_check: str) -> bool:
        """
        Checks if a given string is balanced.
        :param string_to_check: str
        :return: A boolean value indicating if the string is balanced
        """

        if not string_to_check:
            return True

        for index, char in enumerate(string_to_check):

            self.enable_bypass_for_comments(index, char, string_to_check)

            if self.bypass_mode:
                continue
            elif char in self.symbols.keys():
                self.stack.append(char)
            elif char in self.symbols.values():
                latest_opening_symbol = self.stack.pop()

                if char != self.symbols[latest_opening_symbol]:
                    return False

        return True

    def enable_bypass_for_comments(self, index: int, char: str, string_to_check: str) -> None:
        """
        Checks the opening and closing of a comment within the string to check.
        :param index: The index of the current char that is being checked
        :param char: The char being checked
        :param string_to_check: The string being checked
        :return:
        """
        if index + 1 == len(string_to_check):
            return
        elif not self.bypass_mode and char + string_to_check[index + 1] == self.comments[0]:
            self.bypass_mode = True
        elif self.bypass_mode and char + string_to_check[index + 1] == self.comments[1]:
            self.bypass_mode = False




