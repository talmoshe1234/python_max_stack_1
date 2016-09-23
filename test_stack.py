from upgraded_stack import UpgradedStack


s = UpgradedStack()

print(s.is_empty())
s.push(3)
s.push(4)
s.push(4)
s.push(1)
s.push(2)
s.push(5)
print(s.max_val())
print(s.size())
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.max_val())
print(s.size())
