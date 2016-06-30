import psycopg2


class UserManager:

    def db_connect(func):
        def deco(self, *args):
            responce = None
            params = 'dbname=synergy user=synuser password=synergy host=localhost'
            con = psycopg2.connect(params)
            try:
                self.cursor = con.cursor()
                responce = func(self, *args)
            finally:
                self.cursor.close()
                con.commit()
                con.close()
            # print(responce)
            return responce
        return deco

    @db_connect
    def syncdb(self):
        with open('schema.sql') as fl:
            schema = fl.read()
            for command in schema.split('-*-'):
                self.cursor.execute(command)
                # print(self.cursor.statusmessage)

        print('... DB schema created ...')

    @db_connect
    def get(self):
        pass

    @db_connect
    def get_all(self):
        self.cursor.execute('select get_users();')
        users = self.cursor.fetchall()

        responce = []
        for user in users:
            cleared = user[0].replace('(', '').replace(')', '').split(',')
            responce.append({'id': cleared[0],
                             'name': cleared[1],
                             'email': cleared[2]})
        return responce

    @db_connect
    def search(self):
        pass

    @db_connect
    def add(self, values):
        self.cursor.execute('select add_user(%s);' % ','.join(["'" + str(x) + "'" for x in values]))
        responce = self.cursor.statusmessage
        return responce

    @db_connect
    def update(self):
        pass

    @db_connect
    def delete(self):
        pass


if __name__ == '__main__':
    UserManager().syncdb()
    UserManager().add(['bear', 'bear123@yahoo.com'])
    UserManager().add(['deer', 'deer87@yahoo.com'])
    UserManager().get_all()
