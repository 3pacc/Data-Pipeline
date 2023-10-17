from etl import con
def score_evolution(namevar):
    Query="SELECT year,score FROM T_SCORES where name='"+namevar+"'"
    cursor=con.cursor()
    cursor.execute(Query)
    
    #print(cursor.fetchall())
    return (cursor.fetchall())

print(score_evolution('a'))

def avg():
    QUERY='select year,avg(score) from t_scores group by year'
    cursor=con.cursor()
    cursor.execute(QUERY)
    return (cursor.fetchall())
print(avg())

    
#print('name of current module',__name__)

#delete from t_scores where id>27;
#select year,avg(score) from t_scores groupe by year;