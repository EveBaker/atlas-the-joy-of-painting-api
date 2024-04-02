from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='JoyOfPaintingDB',
            user='root',
            password='root'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MYSQL: {e}")
        return None
    
@app.route('/episodes', methods=['GET'])
def get_episodes():
    """fetches episodes"""
    month = request.args.get('month')
    query = "SELECT * FRON Episodes"
    if month:
        query += " WHERE MONTH(air_date) = %s"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if month:
        cursor.execute(query, (month,))
    else:
        cursor.execute(query)
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(episodes)

