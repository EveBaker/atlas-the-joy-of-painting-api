import pandas as pd
import mysql.connector

def connect_to_db():
    """Establishes connection"""
    return mysql.connector.connect('localhost', database='JoyOfPaintingDB', user='root', password='root')

def load_data(csv_path):
    """loads data from pandas to pandas"""
    return pd.read_csv(csv_path)

def process_episodes(df):
    """Inserts episodes"""
    connection = connect_to_db()
    cursor = connection,cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("INSERT INTO Episodes (title, season, episode, air_date) VALUES(%s, %s, %s, %s)"), 
            (row['Title', int(row['season']), int(row['Episode']), row['AirDate']])

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