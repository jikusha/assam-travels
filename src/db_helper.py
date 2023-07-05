class DbHelper:
    def __init__(self, conn):
        self.conn = conn

    def execute_query_with_params(self, query, params):
        try:
            cur = self.conn.cursor()
            cur.execute(query, params)
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            close_connection(cur, self.conn)

    def get_user_by_email(self, query, params):
        inputs = {}
        try:
            cur = self.conn.cursor()
            cur.execute(query, params)
            row =  cur.fetchone()
            return row
        except Exception as ex:
            raise ex
        finally:
            close_connection(cur, self.conn)

def close_connection(cur, conn):
    cur.close()
    conn.close()