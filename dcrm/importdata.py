import csv
import mysql
import mysql.connector
# Connect DB server and database
conn = mysql.connector.connect(user='root', password='10081998',
                               host='localhost', database='django')
cursor = conn.cursor()
# open the csv file
mock_data_files = ['./../mockdata/MOCK_DATA_1.csv',
                   './../mockdata/MOCK_DATA_2.csv', './../mockdata/MOCK_DATA_3.csv']

for data_file in mock_data_files:
    with open(data_file, mode='r', encoding='utf8') as csv_file:
        # read csv using reader class
        csv_reader = csv.reader(csv_file)
        # skip header
        header = next(csv_reader)
        # Read csv row wise and insert into table
        for row in csv_reader:
            InsertDataQuery = f"INSERT INTO django (created_at, first_name, last_name, email, phone, address, city, state, zipcode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            print('Data Inserted! : django')
            cursor.execute(InsertDataQuery)

    conn.commit()
    cursor.close()
