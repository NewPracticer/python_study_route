# 循环
# while for

# CONDITION = True 
# while CONDITION:
#     print('123456')
#     CONDITION = False

# counter =1 
# while counter <=10:
#     counter += 1
#     print(counter)
# else:
#     print('EOF')

# a = ['apple','orange','banana',(1,2,3)]
# for x in a:
#     for y in x:
#         print(y,end=' ')
#         break;
# else:
#     print('fruit is gone')

# for x in range(0,8,2):
#     print(x, end = ' | ')

# for x in range(8,0,-2):
#     print(x, end = ' | ')

a = [1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end = ' | ')
    
print(a[0:len(a):2])
    