from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from datetime import datetime

application = Flask(__name__)

application.config['MYSQL_USER'] = "user1"
application.config['MYSQL_PASSWORD'] = "D$S3hiEZ4cS4f$P"
application.config['MYSQL_HOST'] = "aa8y52f0k8vyz0.cvczn6f9jk06.us-east-2.rds.amazonaws.com"
application.config['MYSQL_DB']= 'ebdb'
application.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(application)


@application.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM sensor_readings''')
    results = cur.fetchall()
    print(results)
    results_dict = {}
    #for item in results:
    #    results_dict[item['id']] = item['name']
    return results_dict
    #return "Your Flask App Works!"

@application.route("/hello")
def hello():
    return "Hello World!"

@application.route('/postjson', methods = ['POST'])
def postJsonHandler():
    cur = mysql.connection.cursor()
    content = request.get_json(force=True)
    sql = 'INSERT INTO sensor_readings (sound_low, sound_high, temp, humidity, motion_count, reading_time) VALUES (%s, %s, %s, %s, %s, %s)'
    cur.execute(sql, (content['sound_low'], content['sound_high'], content['temp'], content['humidity'], content['motion_count'], datetime.now().time()))
    mysql.connection.commit()
    print (content)
    return 'JSON posted'
    #content = request.get_json()
    #print (content)
    #return 'JSON posted'



if __name__ == "__main__":
    application.run(debug=True)
