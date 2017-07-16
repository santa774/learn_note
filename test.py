#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
from functools import reduce

class Animal(object):
	def run(self):
		print('Animal is running')

class Car(object):
	def run(self):
		print('Car is running')

def run_twice(Animal):
	Animal.run()
	Animal.run()

run_twice(Car())
# def fn(x, y):
# 	return x * 10 + y

# def char2num(s):
# 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# def str2float(s):
# 	dotindex = 0
# 	for x, y in enumerate(s):
# 		if '.'==y:
# 		    dotindex = x
# 	s1 = s[: dotindex] + s[dotindex+1 :]
# 	return (reduce(fn, map(char2num, s1)) / (pow(10, (len(s) -1 - dotindex))))

# print(str2float('12.566333'))




# def is_palindrome(num):
# 	li = str(num)
# 	length = len(li) // 2
# 	for x in range(length):
# 		if li[x] != li[-(x + 1)]:
# 		    return False
# 	return True

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88), ('zzz', 100)]

# def by_name(t):
# 	return t[0]

# def by_scout(t):
# 	return t[1]

# # print(by_name(L[2]))
# L2 = sorted(L, key=by_scout, reverse=True)
# print(L2)

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# def log(text):
# 	if isinstance(text, str):
# 		def decorator(func):
# 			@functools.wraps(func)
# 			def wrapper(*args, **kw):
# 				print('%s %s before' %(text, func.__name__))
# 				x = func(*args, **kw)
# 				print('%s %s after' %(text, func.__name__))
# 				return x
# 			return wrapper
# 		return decorator  
# 	else:
# 		@functools.wraps(text)
# 		def wrapper(*args, **kw):
# 			print('%s %s before' %(text, text.__name__))
# 			x = text(*args, **kw)
# 			print('%s %s after' %(text, text.__name__))
# 			return x
# 		return wrapper

# @log('abc')
# def something(num):
# 	print(num * num)

# something(9)

# def fun(x, y, z):
# 	print('x:', x, 'y:', y, 'z:', z)
# m2 = functools.partial(fun, z=10)
# m2(2,4, z=11)

