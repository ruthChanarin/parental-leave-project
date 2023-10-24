
import pandas as pd

data = pd.read_csv('./parental_leave.csv', encoding = "ISO-8859-1")
df = pd.DataFrame(data)

print(df)