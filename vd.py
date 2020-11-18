import mysql.connector

x = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '161537'
)

print(x)

y = x.cursor()
#y.execute('create database ttt')
y.execute('show databases')

for i in y:
    print(i)
    