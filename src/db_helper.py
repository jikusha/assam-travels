class DbHelper:
    def __init__(self, conn):
        self.conn = conn

    def execute_query_with_params(self, query, params):
        try:
            cur = self.conn.cursor()
            cur.execute(query, params)
            self.conn.commit()
        except Exception as ex:
            print(f"Execution is failed due to {ex}")
            raise ex
        finally:
            self.conn.close()