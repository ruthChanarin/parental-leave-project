
import pandas as pd
import pyodbc 


# import the csv file
data = pd.read_csv('./parental_leave.csv', encoding = "ISO-8859-1")
df = pd.DataFrame(data)


# to check column names
print(df.columns)


# initial look at dataframe
df.head


# check for null values
df.isna().sum()


# drop empty columns
df.drop(["Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9"], axis='columns', inplace=True)

# could also have used dropna() to drop any columns where all values are empty
df.dropna(axis="columns", how="all")


# let's drop rows with na values in the industry column, since we can't fill that with an 
# average, and the missing data would impair industry-based comparisons

df.dropna(subset=['Industry'], inplace=True)


# now, we'll fill in the na values in the unpaid maternity leave, and paid and unpaid 
# paternity columns with a column average

df[['Unpaid Maternity Leave', 'Paid Paternity Leave', 'Unpaid Paternity Leave']] = df[['Unpaid Maternity Leave', 'Paid Paternity Leave', 'Unpaid Paternity Leave']].fillna(df[['Unpaid Maternity Leave', 'Paid Paternity Leave', 'Unpaid Paternity Leave']].mean())


# Let's check for duplicates
df.duplicated().sum()


# Now the data set is clean & ready for further processing!


# Let's connect to the SQL Server

# server_name = 'f01d8b0b1a56'
# database_name = 'parental-leave'
# username = 'sa'
# password = 'Strong.Pwd-123'

# connection_string = f'DRIVER=SQL Server;SERVER={server_name};DATABASE=master;UID={username};PWD={password}'

# try:
#     conn = pyodbc.connect(connection_string, autocommit=True)
# except pyodbc.Error as e:
#     print(f"Error connecting to SQL Server: {e}")
#     exit()

conn = pyodbc.connect('Driver={SQL Server};'
'Server=localhost'
'Database=parental-leave;'
'Trusted_Connection=yes;')


cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE parental-leave-data (
			company nvarchar(50),
			industry nvarchar(50),
            paid_maternity_leave int,
            unpaid_maternity_leave int,
            paid_paternity_leave int,
            unpaid_paternity_leave int,
			)
               ''')