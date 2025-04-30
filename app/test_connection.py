import pymysql

# Your RDS Database details
host = 'swe-645.cmwmb0zaijgs.us-east-1.rds.amazonaws.com'
port = 3306
username = 'kush'
password = 'Password12345'
database = 'studentdb'

try:
    connection = pymysql.connect(
        host=host,
        user=username,
        password=password,
        database=database,
        port=port
    )
    print("✅ Successfully connected to the database!")
    connection.close()
except Exception as e:
    print("❌ Failed to connect to database!")
    print(e)
