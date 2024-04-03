import pandas as pd
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(host='localhost', database='JoyOfPaintingDB', user='localhost', password='root')

def load_data(csv_path):
    return pd.read_csv(csv_path)

def process_episodes(df):
    connection = connect_to_db()
    cursor = connection.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("INSERT INTO Episodes (title, season, episode, air_date) VALUES (%s, %s, %s, %s)", 
                           (row['Title'], int(row['Season']), int(row['Episode']), row['AirDate']))
        except mysql.connector.Error as err:
            print("Error: ", err)
            connection.rollback()
        else:
            connection.commit()

    cursor.close()
    connection.close()

def main():
    episodes_csv = 'The Joy Of Painting - Episode Dates.csv'
    df_episodes = load_data(episodes_csv)
    process_episodes(df_episodes)
    print("ETL Process Completed")

if __name__ == "__main__":
    main()
