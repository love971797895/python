#!usr/bin/python
#condfing=utf-8
#print("hello,Word");
print("OK!!!");
age = 26;
#print(age);
#print("this result is :"%result);

#  %d 代表的是一个int的值  %s 代表的是string的值
#print('this is my test result,frist is %d'%num1);

#name='Jeff.Mr';
name = input('please input your name...')
print('my name is %s'%name);

fav = input('please inout your favorite...')

print('************start**************')
print('Name:%s'%name)
print('Age:%d'%age)
print('Favorite:%s'%fav)
print('*************end**************')
input("this is wait for you...");

#if和else的判断
#对于python而言，必须要注意格式，如果这时候else前面有空格，则会编译失败
#对于其中的 : 表示当前条件结束
if age > 20:
	print('My age > 20');
else:
	print('My age < 20');
#python里面，缩进代表这代码属于上一个过程
