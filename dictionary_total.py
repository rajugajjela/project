#!/bin/bash
print("printing the dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
print(dic)
print("Type of dictionary:",type(dic))

print("printing the dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
print(dic['NAME'])

print("printing the dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
x=dic.get('AGE')
print(x)

print("printing the keys in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
x=dic.keys()
print(x)

print("printing the values in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
x=dic.values()
print(x)

print("printing the items in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
x=dic.items()
print(x)

print("changing  the values in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
dic['NAME']='Rani'
dic['AGE']='25'
dic['GENDER']='Female'
print(dic)

print("updating operation in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Male'}
dic.update({"NAME":"Vamshi"})
print(dic)

print("pop operation in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Make'}
dic.pop('NAME')
print(dic)
 
print("clear operation in dictionary")
dic={'NAME':'Raju','AGE':'20','GENDER':'Make'}
dic.clear()
print(dic)
