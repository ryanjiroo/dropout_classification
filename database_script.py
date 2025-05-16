import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data.csv", sep=';', encoding='windows-1252')

URL = "postgresql://postgres:[YOUR_PASSWORD]@db.xnudsitiqeidzoryistz.supabase.co:5432/postgres"
 
engine = create_engine(URL)
df.to_sql('student_performance', engine)