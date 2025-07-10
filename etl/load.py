import os
import pandas as pd
import mysql.connector

def load_to_mysql(df):
    # ✅ Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Himanshum7",  # ← Change if your password is different
        database="news_db"
    )
    
    cursor = conn.cursor()

    # 🧹 Optional: clear previous data
    cursor.execute("TRUNCATE TABLE headlines")

    # 🟢 Insert rows
    count = 0
    for _, row in df.iterrows():
        sql = """
        INSERT INTO headlines (title, url, date, clean_title, sentiment, sentiment_label)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            row['title'],
            row['url'],
            row['date'],
            row['clean_title'],
            float(row['sentiment']),
            row['sentiment_label']
        )
        cursor.execute(sql, values)
        count += 1

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Successfully inserted {count} rows into MySQL.")

# Optional test: Run this file directly to load data into MySQL
if __name__ == "__main__":
    import pandas as pd
    import os

    # Find the path to the CSV file
    csv_file = os.path.join("data", "headlines_transformed.csv")

    # Load the data
    df = pd.read_csv(csv_file)

    # Load it into MySQL
    load_to_mysql(df)

