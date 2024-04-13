class RomanNumber:
    def __init__(self, number):
        if str(number).isdigit():
            if self.is_int(number):
                self.int_value = int(number)
                self.rom_value = self.roman_number()
            else:
                self.int_value = None
                print('ошибка')
        else:
            if self.is_roman(number):
                self.rom_value = number
                self.int_value = self.decimal_number()
            else:
                self.rom_value = None
                print('ошибка')

    @staticmethod
    def is_int(value):
        if (0 < value < 4000) and isinstance(value, int):
            return True
        return False
    @staticmethod
    def is_roman(value):
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

    def roman_number(self):
        if self.int_value is None:
            return None
        el_roman = {1: 'I', 4:'IV',5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',90: 'XC', 100: 'C', 400: 'CD', 500:
            'D', 900: 'CM', 1000: 'M'}
        result = ''
        for value, number in sorted(el_roman.items(), reverse=True):
            while self.int_value >= value:
                result += number
                self.int_value -= value
        return result
    def decimal_number(self):
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


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))