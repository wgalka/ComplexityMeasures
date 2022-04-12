import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port='3309',
    user="root",
    password="",
    database="selfduality"
)
mycursor = mydb.cursor()

table_name = 'a1'

mycursor.execute("select diff from " + table_name)
data = mycursor.fetchall()
print(data)
mean = [x[0] for x in data]
print(data)

ind = [x for x, _ in enumerate(mean)]

plt.rcParams["figure.figsize"] = (20,3)

plt.bar(ind, mean, color='red')
plt.ylabel('1-(mean(x) + mean(1-x)).py')

plt.savefig('diff_'+table_name+'.png', dpi=300)
plt.show()
