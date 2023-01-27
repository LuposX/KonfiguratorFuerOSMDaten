from __future__ import annotations


from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple


class TagParserInterface(ABC):
    """
    The TagParser job is to parse the Tags the user inputted for the category creation and check if they are correct
    """

    @abstractmethod
    def parse_tags(self, tags: List[str]) -> List[Tuple[str, str]]:
        """
        This method parses a list of tags to a list of key, value pairs. The inputted list should be in the following format:
        ["key1=value1", "key2=value2", "key3=value3",...]

        Args:
            tags (List[str]): A list of tags that the user inputted should be in the following format: "key=value".

        Returns:
           List[Tuple[str, str]]: A list of key,value tag pairs.
        """
        pass
