from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    strings = re.findall(r'\S+', text)

    if not strings:
        return None, None

    strings.sort(key=len)

    return strings[0], strings[-1]
