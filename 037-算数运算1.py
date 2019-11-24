print(type(len))
a = int(123)
b = int(456)
print(a+b)
#
class New_int(int):
    def __add__(self, other):
        return int(self)+int(other)
n = New_int(2)
m = New_int(3)
print(m+n)