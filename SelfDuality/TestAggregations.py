import aggregationslib.aggregation
import mysql.connector


class SaveData:
    def __init__(self, table='a1', indexes=3003, aggregation=aggregationslib.aggregation.arithmetic, p=None, r=None):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port='3309',
            user="root",
            password="",
            database="selfduality"
        )

        self.indexes = indexes
        self.aggregation = aggregation
        self.table = table

        self.p = p
        self.r = r

        self.sql1 = "SELECT * from normal WHERE id ="
        self.sql2 = "SELECT * from reversed WHERE id ="

        self.sql3 = "INSERT INTO " + table + "(id, mean, mean_rev, diff) VALUES (%s, %s, %s, %s)"
        self.truncate = "truncate " + table

        self.create = "CREATE TABLE IF NOT EXISTS " + table + "( id INT PRIMARY KEY AUTO_INCREMENT, mean FLOAT, mean_rev FLOAT, diff FLOAT );"

    def execute(self):
        mycursor = self.mydb.cursor()

        mycursor.execute(self.create)
        self.mydb.commit()

        mycursor.execute(self.truncate)
        self.mydb.commit()

        for i in range(1, self.indexes + 1):
            mycursor.execute(self.sql1 + str(i))
            row = mycursor.fetchall()

            mycursor.execute(self.sql2 + str(i))
            row_rev = mycursor.fetchall()

            if self.r == None or self.p == None:
                mean = self.aggregation(row[0][1:])
                mean_rev = self.aggregation(row_rev[0][1:])
            elif self.r == None:
                mean = self.aggregation(row[0][1:], r=self.r)
                mean_rev = self.aggregation(row_rev[0][1:], r=self.r)
            elif self.p == None:
                mean = self.aggregation(row[0][1:], p=self.r)
                mean_rev = self.aggregation(row_rev[0][1:], p=self.r)

            table = "{0:<25} {1:<25} {2:<25}"
            diff = 1 - (mean + mean_rev)
            print(table.format(mean, mean_rev, diff), row)
            mycursor.execute(self.sql3, [i, float(mean), float(mean_rev), float(diff)])
            self.mydb.commit()
        print("Saved:", self.table)
        mycursor.close()

    def __del__(self):
        self.mydb.close()


a1 = SaveData().execute()
a2 = SaveData(table='a1', aggregation=aggregationslib.aggregation.exponential).execute()
