class RomanNumber:
    """
    It is a class representing Roman numerals and providing arithmetic operations on them.

    Attributes
    -----------
    - rom_value: Roman numeral representation of the integer value

    Methods
    --------
    - is_roman(value): Checks if a given value is a valid Roman numeral.
    - decimal_number(self): Converts a Roman numeral to its equivalent integer value.
    """
    def __init__(self, rom_value):
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ошибка')

    @staticmethod
    def is_roman(value):
        """
        Check if a value is a valid Roman numeral.
        :param value: The value to be checked.
        :return: True if the value is a valid Roman numeral, False otherwise.
        """
        right = 'IVXLCDM'
        for char in value:
            if char not in right:
                return False
        if ('IIII' in value or value.count('V') > 1 or 'XXXX' in value
                or value.count('L') > 1 or 'CCCC' in value or value.count('D') > 1
                or 'MMMM' in value):
            return False
        for i in range(len(value) - 1):
            if right.index(value[i]) < right.index(value[i + 1]):
                if value[i] == 'I' and value[i + 1] not in 'VX':
                    return False
                if value[i] == 'X' and value[i + 1] not in 'LC':
                    return False
                if value[i] == 'C' and value[i + 1] not in 'DM':
                    return False
        return True

    def decimal_number(self):
        """
        Convert an integer value to its Roman numeral representation.
        :return: The integer representation of the Roman numeral value.
        """
        if self.rom_value is None:
            return None
        roman_el = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 0
        for el in reversed(self.rom_value):
            value = roman_el.get(el)
            if value < prev:
                result -= value
            else:
                result += value
            prev = value
        return result

    def __str__(self):
        '''
        Returns a string representation of a point.
        :return: String representation of the point.
        '''
        return f'{self.rom_value}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with teams' info
        '''
        return self.__str__()


num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))
