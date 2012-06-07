class Polynomial(object):
    def __new__(cls, coeffs, varname='x'):
        self = object.__new__(cls)
        self._varname = varname
        if isinstance(coeffs, (list, tuple)):
            self._coeffs = {exp: coeff for exp, coeff in enumerate(coeffs)
                if coeff}
        elif isinstance(coeffs, dict):
            self._coeffs = {exp: coeffs[exp] for exp in coeffs if coeffs[exp]}
        else:
            raise ValueError(
            'coeffs must be an instance of list, tuple or dict')
        return self

    def __call__(self, **varvalues):
        result = 0
        cls = self.__class__
        varname = self._varname

        if self._varname not in varvalues:
            return self
        
        for exp in self._coeffs:
            coeff = self._coeffs[exp]
            if isinstance(exp, cls):
                exp = exp(**varvalues)
            if isinstance(coeff, cls):
                coeff = coeff(**varvalues)
            result += coeff * varvalues[varname] ** exp

        return result

    def __repr__(self):
        return ('{}({}, {})'.format(self.__class__.__name__,
            repr(self._coeffs), repr(self._varname)))

    def __add__(self, other):
        result_coeffs = {}
        if isinstance(other, self.__class__):
            if self._varname != other._varname:
                raise ValueError('adding two unlike Polynomial')

            for exp in other._coeffs.keys():
                result_coeffs[exp] =  other._coeffs[exp]
        else:
            result_coeffs[0] = other

        for exp in self._coeffs:
            result_coeffs.setdefault(exp, 0)
            result_coeffs[exp] += self._coeffs[exp]
        return self.__class__(result_coeffs, self._varname)

    __radd__ = __add__

    def __neg__(self):
        """Returns a Polynomial whose coefficients' signs are flipped."""
        return self.__class__({exp: -self._coeffs[exp] for exp in self._coeffs},
            self._varname)

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __mul__(self, other):
        result_coeffs = {}
        if (isinstance(other, self.__class__) and
            self._varname == other._varname):
            for i in self._coeffs:
                self_coeff = self._coeffs[i]
                for j in other._coeffs:
                    exp = i + j
                    result_coeffs.setdefault(exp, 0)
                    result_coeffs[exp] += self_coeff * other._coeffs[j]
        else:
            for exp in self._coeffs:
                result_coeffs[exp] = self._coeffs[exp] * other

        return self.__class__(result_coeffs, self._varname)
            
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return NotImplemented
        result_coeffs = {exp: self._coeffs[exp] / other
                for exp in self._coeffs}
        return self.__class__(result_coeffs, self._varname)

    def __pow__(self, other):
        if isinstance(other, int):
            result = self
            if other == 0:
                return self.__class__({0: 1}, self._varname)
            power = abs(other)
            while power != 1: 
                power, excess = divmod(power, 2)
                result = result * result
                if excess:
                    result = result * self
                
            if other < 0:
                result_coeffs = {-1: result}
            return result
        return NotImplemented
