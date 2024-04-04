import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_config = {
    'host': 'localhost',
    'database': 'JoyOfPaintingDB',
    'user': 'root',
    'password': 'root'
}

def load_data_to_db(df, table_name):
    """
    Load a DataFrame to the specified database table.
    """
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            for i, row in df.iterrows():
                placeholders = ', '.join(['%s'] * len(row))
                columns = ', '.join(row.index)
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, tuple(row))
            
            connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def transform_data():
    dataset_paths = {
        'episodes': 'The Joy Of Painting - Episode Dates.csv',
        'subjects': 'The Joy Of Painiting - Subject Matter.csv',
        'colors': 'The Joy Of Painiting - Colors Used.csv'
    }

    # Extract
    episodes_df = pd.read_csv(dataset_paths['episodes'])
    subjects_df = pd.read_csv(dataset_paths['subjects'])
    colors_df = pd.read_csv(dataset_paths['colors'])

    # Transform

    # 1. Standardizing Date Formats
    episodes_df['air_date'] = pd.to_datetime(episodes_df['air_date']).dt.date

    # 2. Deduplicating Subjects and Colors
    subjects_df = subjects_df.drop_duplicates(subset=['subject_name'])
    subjects_df['subject_name'] = subjects_df['subject_name'].str.title()

    colors_df = colors_df.drop_duplicates(subset=['color_name'])
    colors_df['color_name'] = colors_df['color_name'].str.lower() 

    # 3. Handling Missing Values (example for episodes)
    episodes_df = episodes_df.dropna(subset=['title', 'air_date'])

    # Load
    load_data_to_db(episodes_df, 'Episodes')
    load_data_to_db(subjects_df, 'Subjects')
    load_data_to_db(colors_df, 'Colors')

if __name__ == "__main__":
    transform_data()
