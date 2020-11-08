import mysql.connector


class Connection:
    def __init__(self,host,user,passwd,database):
        self.con=mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database)
        
        self.mycursor=self.con.cursor()

    def query(self,req):
        self.mycursor.execute(req)

    def commit(self):
        self.con.commit()

    def close(self):
        self.mycursor.close()
        self.con.close()

"""if __name__=='__main__':
    try:
        c=Connection()
        print('connexion réussie')
        c.query('select * from customers')
        clients= c.mycursor.fetchall()
        for client in clients:
             print(client)
        c.close()
        print('con fermée')
    except:
        print('connexion échouée')"""
