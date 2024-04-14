class RomanNumber:
    def __init__(self, number):
        if str(number).isdigit():
            if self.is_int(number):
                self.int_value = int(number)
                self.rom_value = self.roman_number()
            else:
                self.int_value = None
                self.rom_value = None
        else:
            if self.is_roman(number):
                self.rom_value = number
                self.int_value = self.decimal_number()
            else:
                self.rom_value = None
                self.int_value = None


    def __add__(self, other):
        if isinstance(other, RomanNumber):
            result = self.decimal_number() + other.decimal_number()
            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            result = self.decimal_number() - other.decimal_number()
            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            result = self.decimal_number() * other.decimal_number()
            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            if other.decimal_number() == 0:
                print('ошибка')
                return RomanNumber(None)

            result = self.decimal_number() // other.decimal_number()

            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __mod__(self, other):
        if isinstance(other, RomanNumber):
            if other.decimal_number() == 0:
                print('ошибка')
                return RomanNumber(None)

            result = self.decimal_number() % other.decimal_number()

            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __pow__(self, other):
        if isinstance(other, RomanNumber):
            result = self.decimal_number() ** other.decimal_number()
            if 0 < result < 4000:
                return RomanNumber(result)
            else:
                print('ошибка')
                return RomanNumber(None)
        else:
            print('ошибка')
            return RomanNumber(None)

    def __truediv__(self, other):
        if isinstance(other, RomanNumber):
            if other.decimal_number() == 0:
                print('ошибка')
                return RomanNumber(0)

            result = self.decimal_number() / other.decimal_number()

            if result != self.decimal_number() // other.decimal_number() or result >= 4000:
                print('ошибка')
                return RomanNumber(0)

            return RomanNumber(int(result))
        else:
            print('ошибка')
            return RomanNumber(0)

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
        el_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500:
            'D', 900: 'CM', 1000: 'M'}
        result = ''
        int_value = self.int_value
        for value, number in sorted(el_roman.items(), reverse=True):
            while int_value >= value:
                result += number
                int_value -= value
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


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II') )
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)