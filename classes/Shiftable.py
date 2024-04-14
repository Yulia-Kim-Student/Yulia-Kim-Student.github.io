class ShiftableList(list):
    def check_right(func):
        def checker(left, right, *args, **kwargs):
            if type(right) == int:
                return func(left, right, *args, *kwargs)
            else:
                raise TypeError()
        return checker
    @check_right
    def __lshift__(self, other):
        other %= len(self)
        return self[other:] + self[:other]
    @check_right
    def __rshift__(self, other):
        other %= len(self)
        return self[-other:] + self[:-other]
l = ShiftableList([1, 2, 3])
a = l << 2
print(a)