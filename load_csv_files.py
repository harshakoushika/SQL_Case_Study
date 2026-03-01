import pandas as pd
from sqlalchemy import create_engine

print("Program Started")

# Create connection
engine = create_engine("mysql+pymysql://root:123456@localhost/university_db")

files = [
    'artist',
    'canvas_size',  
    'image_link',
    'museum_hours',
    'museum',
    'product_size',
    'subject',
    'work'
]

for file in files:
    print(f"Loading {file}.csv ....")

    df = pd.read_csv(f"{file}.csv")

    # 🔥 MUST be inside loop
    df.to_sql(file, con=engine, if_exists='replace', index=False)

print("✅ All files loaded successfully")