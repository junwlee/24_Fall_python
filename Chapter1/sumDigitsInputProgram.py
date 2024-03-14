string_int = input("Write Integer: ")
string_length = len(string_int)
integer_int = int(string_int)
lst = [i for i in range(string_length)]
sortedListDesc = sorted(lst, reverse=True)

digitSum = 0
for j in sortedListDesc:
  digitSum += (integer_int // (10 ** j))
  integer_int -= (integer_int // (10 ** j)) * (10 ** j)

print(digitSum)