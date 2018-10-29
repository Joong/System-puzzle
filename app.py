import datetime
import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def index():
    # Connect to database
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all local GET requests
    sql_local = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'local\';"""
    cur.execute(sql_local)
    local = cur.fetchone()[0]

    # Get number of all remote GET requests
    sql_remote = """SELECT COUNT(*) FROM weblogs WHERE source LIKE \'remote\';"""
    cur.execute(sql_remote)
    remote = cur.fetchone()[0]

    # Get number of all succesful local requests
    sql_local_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source LIKE \'local\';"""
    cur.execute(sql_local_success)
    local_success = cur.fetchone()[0]

    # Get number of all succesful remote requests
    sql_remote_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source LIKE \'remote\';"""
    cur.execute(sql_remote_success)
    remote_success = cur.fetchone()[0]

    # Determine rate if there was at least one request
    rate = "No entries yet!"
    if all != 0:
        local_rate = str(local_success / local)
        remote_rate = str(remote_success / remote)

    return render_template('index.html', local_rate = local_rate, remote_rate = remote_rate)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
