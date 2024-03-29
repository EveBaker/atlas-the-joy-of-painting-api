import pandas as pd
from sqlalchemy import create_engine

# load csv
episode_data = pd.read_csv ('The Joy Of Painting - Episode Dates.csv')
color_data = pd.read_csv('The Joy Of Painiting - Colors Used.csv')

#load data
engine = create_engine('sqlite:///joy_of_painting.db')
episode_data.to_sql('episodes', engine, if_exists='replace', index=False)
color_data.to_sql('colors', engine, if_exists='replace', index=False)