class OrdinalNumber:
    def __init__(self, number = 0):
        self.number = -1
        self.deg = None
        self.next = None
        if type(number) == int:
            self.number = number
            if number != 0:
                self.deg = OrdinalNumber()
                self.next = OrdinalNumber()
        else:
            number = number.strip()
            if number.find('{') == -1:
                last = number.find('+')
                if last == -1:
                    if number[0] not in '0123456789':
                        self.deg = OrdinalNumber(1)
                        if number.find('*') == -1:
                            self.number = 1
                        else:
                            self.number = int(number[number.find('*') + 1:])
                    else:
                        self.number = int(number)
                        self.deg = OrdinalNumber()
                    self.next = OrdinalNumber()
                else:
                    self.deg = OrdinalNumber(1)
                    self.next = OrdinalNumber(number[last + 1:])
                    first = number.find('*')
                    if first == -1:
                        self.number = 1
                    else:
                        self.number = int(number[first + 1 : last])
            else:
                counter = 0
                first = number.find('{')
                last = -1
                for i in range(first, len(number), 1):
                    if number[i] == '{':
                        counter += 1
                    elif number[i] == '}':
                        counter -= 1
                    if counter == 0:
                        last = i
                        break
                self.deg = OrdinalNumber(number[first + 1 : last])
                number = number[last + 1:]
                first = number.find('*')
                last = number.find('+')
                if last == -1:
                    last = len(number)
                    self.next = OrdinalNumber()
                if first > last or first == -1:
                    self.number = 1
                else:
                    self.number = int(number[first + 1: last])
                if last != len(number):
                    number = number[last + 1:]
                    self.next = OrdinalNumber(number)

    def implicit_converter_from_int(f):
        """convert number from int into OrdinalNumber as second argumnet to f"""
        def ret(this, number, *args, **kwargs):
            if type(number) == int:
                number = OrdinalNumber(number)
            return f(this, number, *args, **kwargs)
        return ret
    
    def cut_head(self):
        """get the major part of KNF"""
        head = self.copy()
        head.next = OrdinalNumber()
        return head

    def is_zero(self):
        """check whether self is zero ordinal"""
        if self.number == 0:
            self.deg = None
            self.next = None
        if (self.deg is None) ^ (self.next is None):
            raise EOFError
        return self.deg is None
    
    def is_number(self):
        """check whether self is natural number"""
        return self.is_zero() or self.deg.is_zero()

    def copy(self):
        """get copy of self"""
        if self.is_zero():
            return OrdinalNumber()
        ret = OrdinalNumber(self.number)
        ret.deg = self.deg.copy()
        ret.next = self.next.copy()
        return ret
    
    def __eq__(self, other):
        if not other.is_zero() and not self.is_zero():
            return self.deg == other.deg and self.number == other.number and self.next == other.next
        return other.is_zero() and self.is_zero()
    
    def __ne__(self, other):
        return not self == other
    
    def __le__(self, other):
        if self.is_zero():
            return True
        if other.is_zero():
            return False
        if self.deg == other.deg:
            if self.number == other.number:
                return self.next <= other.next
            return self.number <= other.number
        return self.deg <= other.deg
    
    def __lt__(self, other):
        return self <= other and self != other
    
    def __ge__(self, other):
        return not self < other
    
    def __gt__(self, other):
        return not self <= other
    
    @implicit_converter_from_int
    def __iadd__(self, other):
        if self.is_zero():
            return other
        if other.is_zero():
            return self
        if other.deg < self.deg:
            self.next += other
        elif other.deg == self.deg:
            self.number += other.number
            self.next = other.next
        else:
            return other
        return self
    
    @implicit_converter_from_int
    def __add__(self, other):
        ret = self.copy()
        ret += other
        return ret
    
    @implicit_converter_from_int
    def __radd__(self, other):
        return other + self
    
    @implicit_converter_from_int
    def __imul__(self, other):
        if type(other) == int:
            other = OrdinalNumber(other)
        if other.is_zero() or self.is_zero():
            self = OrdinalNumber()
        else:
            tail = self.next
            head = self.cut_head()
            self = OrdinalNumber()
            current = other
            while not current.is_zero():
                head_copy = head.copy()
                head_copy.deg += current.deg
                if current.is_number():
                    head_copy += tail
                    head_copy.number *= current.number
                else:
                    head_copy.number = current.number
                self += head_copy
                current = current.next
        return self
    
    @implicit_converter_from_int
    def __mul__(self, other):
        ret = self.copy()
        ret *= other
        return ret
    
    @implicit_converter_from_int
    def __rmul__(self, other):
        return other * self
    
    @implicit_converter_from_int
    def __xor__(self, other):
        if self < OrdinalNumber(2):
            return self
        if other.is_number():
            result = OrdinalNumber(1)
            for i in range(other.number):
                result *= self
            return result
        head = other.cut_head()
        result = self.cut_head()
        if self.is_number():
            result.deg = OrdinalNumber(1)
        result.number = 1
        result.deg *= head
        if head.deg.is_number() and self.is_number():
            result = OrdinalNumber(1)
            result.deg = head.copy()
            result.deg.deg.number -= 1
        result *= self ** other.next
        return result        
    
    @implicit_converter_from_int
    def __ixor__(self, other):
        self = self ^ other
        return self
    
    @implicit_converter_from_int
    def __pow__(self, other):
        return self ^ other
    
    @implicit_converter_from_int
    def __rpow__(self, other):
        return other ^ self
    
    @implicit_converter_from_int
    def __rxor__(self, other):
        return other ^ self
    
    @implicit_converter_from_int
    def __ipow__(self, other):
        self ^= other
        return self

    def get_string(self, format = 'normal'):
        """get string representation"""
        if self.is_number():
            return f'{self.number}'
        if format == 'normal':
            base_symbol = 'w'
            prod_symbol = '*'
        elif format == 'latex':
            base_symbol = '\omega'
            prod_symbol = '\cdot'
        ret = f'{base_symbol}'
        if self.deg != OrdinalNumber(1):
            ret += f' ^ {{{self.deg.get_string(format)}}}'
        if self.number != 1:
            ret += f' {prod_symbol} {self.number}'
        if not self.next.is_zero():
            ret += f' + {self.next.get_string(format)}'
        return ret
    
    def __str__(self):
        return self.get_string()
    
    def __repr__(self):
        return self.get_string('latex')