# 1. 输出以下图案
#     ```
#     *****
#     *****
#     *****
#     *****
#     ```

# for i in range(0,4):
#     print('*'*5)

# 2. 输出10行内容，
#     ```
#     *
#     **
#     ***
#     ****
#     *****
#     ```

# for i in range(0,10):
#     for i in range(0,i+1):
#         print('*',end='')
#     print()

# 3. 输出9行内容，，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789。
#     ```
#     1
#     12
#     123
#     1234
#     ```

# for i in range(0,10):
#     for i in range(1,i+1):
#         print(i,end='')
#     print()

# 4. 计算从1加到100的值并输出。

# num=0
# for i in range(1,101):
#     num+=i
# print(num)
#
# 5. 计算10的阶乘（1x2x3x4x5x6x7x8x9x10）（写出非递归解法或递归解法）

# num=1
# for i in range(1,11):
#     num=num*i
# print(num)
#
# 6. 计算从1到1000以内所有奇数的和并输出。

# num=0
# for i in range(1,1000,2):
#     num=num+i
# print(num)
#
# 7. 给定一个整数n，判断是否是质数（质数是只能被1和它自身整除的数）

# n=2
# total=0
# if n==1:
#     print('既不是质数又不是合数')
# for i in range(1,333):
#     if n%i==0:
#         total=total+1
# if total==2:
#     print('是质数')
# if total>2:
#     print('是合数')
#
# 8. 五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321

# total=0
# for i in range(10000,100000):
#     b5=i//10000
#     b4=(i-b5*10000)//1000
#     b3=(i-b5*10000-b4*1000)//100
#     b2=(i-b5*10000-b4*1000-b3*100)//10
#     b1=(i-b5*10000-b4*1000-b3*100-b2*10)
#     if b5==b1 and  b4==b2:
#         total+=1
#         print(i)
# print(total)

# 9. 输出所有的三位水仙花数(其各位数字立方和等于该数本身),例如 153=1^3 + 5^3+ 3^3 。

# for i in range(100,1000):
#     s3=i//100
#     s2=(i-s3*100)//10
#     s1=(i-s3*100-s2*10)
#     if s3*s3*s3+s2*s2*s2+s1*s1*s1==i:
#         print(i)


