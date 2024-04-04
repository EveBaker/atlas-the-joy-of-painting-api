from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Function to establish database connection
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
        raise Exception(f"Error connecting to MYSQL: {e}")
    
# Route to fetch episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    month = request.args.get('month')
    query = "SELECT * FROM Episodes"
    params = ()
    if month:
        query += " WHERE MONTH(air_date) = %s"
        params = (month,)
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        episodes = cursor.fetchall()
        return jsonify(episodes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# Route to fetch episodes by subject
@app.route('/episodes/subject', methods=['GET'])
def get_episodes_by_subject():
    subject = request.args.get('subject')
    query = """
    SELECT e.* FROM Episodes e
    JOIN Episode_Subjects es ON e.episode_id = es.episode_id
    JOIN Subjects s ON es.subject_id = s.subject_id
    WHERE s.subject_name = %s
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (subject,))
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(episodes)

# Route to fetch episodes by color
@app.route('/episodes/color', methods=['GET'])
def get_episodes_by_color():
    color = request.args.get('color')
    query = """
    SELECT e.* FROM Episodes e
    JOIN Episode_Colors ec ON e.episode_id = ec.episode_id
    JOIN Colors c ON ec.color_id = c.color_id
    WHERE c.color_name = %s
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (color,))
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(episodes)

if __name__ == '__main__':
    app.run(debug=True)
