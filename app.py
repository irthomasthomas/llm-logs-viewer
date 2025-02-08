from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

DATABASE_PATH = '/home/thomas/.config/io.datasette.llm/logs.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

def fetch_records(conversation_ids):
    conn = get_db_connection()
    records = []
    for cid in conversation_ids:
        cursor = conn.execute("SELECT * FROM responses WHERE conversation_id = ?", (cid,))
        records.extend(cursor.fetchall())
    conn.close()
    return records

def categorize_record(record):
  if "<arbiter_prompt>" in record['prompt']:
    return "ARBITER_RESPONSE"
  else:
    return "MEMBER_RESPONSE"
    
@app.route('/')
def index():
    with open('llm-deep-search-cids.txt', 'r') as f:
        conversation_ids = [line.strip() for line in f if line.strip() and not line.startswith("---")]

    records = fetch_records(conversation_ids)

    processed_records = []
    for record in records:
        processed_record = dict(record)  # Convert to dict for modification
        processed_record['category'] = categorize_record(processed_record)
        processed_records.append(processed_record)

    return render_template('index.html', records=processed_records)
    
@app.route('/record/<record_id>')
def get_record(record_id):
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM responses WHERE id = ?", (record_id,))
    record = cursor.fetchone()
    conn.close()

    if record:
        return jsonify(dict(record))  # Return as JSON for easier handling
    else:
        return jsonify({'error': 'Record not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
