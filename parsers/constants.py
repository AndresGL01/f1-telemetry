from enum import Enum


class StructTypes(Enum):
    """
    Shortcut for the parsers struct types to make it more legibles.
    """
    CHAR = 'c'
    CHAR8 = 'b'
    UCHAR8 = 'B'
    INT16 = 'h'
    UINT16 = 'H'
    INT32 = 'L'
    UINT32 = 'l'
    INT64 = 'q'
    UINT64 = 'Q'
    FLOAT = 'f'
    DOUBLE = 'd'
    ARR = 's'

    @classmethod
    def fmt_str(cls, fmt: list, byte_order: str = '<') -> str:
        """

        :param fmt: A list of StructTypes that define a format
        :param byte_order: Order of the bytes in the incoming messages
            Example: Little Endian -> <
                     Native -> =
        :return: Format in String like '<HHLLlBf'
        """
        return byte_order + ''.join(map(lambda fmt_item: fmt_item.value, fmt))
