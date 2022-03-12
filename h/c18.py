from enum import Enum

# 枚举类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.GREEN.value)
print(VIP.GREEN.name)

# result = (VIP.GREEN) > (VIP.BLACK)
# print(result)
result = VIP.GREEN is VIP.GREEN
print(result)






