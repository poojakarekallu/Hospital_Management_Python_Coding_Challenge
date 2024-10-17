class PropertyUtil:
    @staticmethod
    def get_property_string():
        hostname = "DESKTOP\SQLEXPRESS"  # Your SQL Server instance name
        dbname = "Hospital_Management"           # Your database name

        connection_string = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={hostname};"
            f"Database={dbname};"
            "Trusted_Connection=yes;"
        )
        return connection_string
