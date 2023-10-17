#etl elt 
import mysql.connector as mysql
con=mysql.connect(
    user='root',
    passwd='',
    database='db_students') 

""" def extract(file):
    data=[]
    lines=[]
    try:
        with open(file) as f:
            lines=f.readlines()
    except:
        print(file,'error')
    #print(lines)
    for line in lines:
        record=line.strip('\n').split(',')
        data.append(tuple(record))
    return data
print(extract('students.csv'))

def transform(data):
    results=[]
    for elt in data:
        results.append((int(elt[0]), elt[1], float(elt[2])))
    return results
print(transform(extract('students.csv'))) 

def load(data):
    Query='INSERT INTO t_scores (year,name,score) values(%s,%s,%s)'
    cursor=con.cursor()
    try:
        cursor.executemany(Query,data)
        con.commit()
    except Exception as e:
        print(e)
load(transform(extract('students.csv'))) """

if __name__=='__main__':
    print('im in etl')# test test