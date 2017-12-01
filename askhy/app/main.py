from flask import Flask
import os

from core.dbdriver import get_db, init_tables

app = Flask(__name__)

init_tables()

@app.route('/')
def index():
	html = "<h1>부탁하냥</h1><ul>"

	with get_db().cursor() as cursor :
		sql = "SELECT *, (SELECT COUNT(*) FROM `cheer` WHERE ask_id = ask.id) AS cheer_cnt FROM `ask`"

		cursor.execute(sql)
		result = cursor.fetchall()

		for id, message, created_time, cheer_cnt in result :
			html += "<li>%d: %s (%d)</li>" % (id, message, cheer_cnt)

	return html

if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		debug=True,
		port=os.environ.get('APP_PORT', 8080)
	)
