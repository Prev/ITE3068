from flask import Flask, render_template
import os

from core.dbdriver import get_db, init_tables

app = Flask(__name__)

init_tables()

@app.route('/')
def index():
	with get_db().cursor() as cursor :
		sql = "SELECT *, (SELECT COUNT(*) FROM `cheer` WHERE ask_id = ask.id) AS cheer_cnt FROM `ask`"

		cursor.execute(sql)
		result = cursor.fetchall()
	print(result)

	return render_template('main.html',
		dataset=result,
	)

if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		debug=True,
		port=os.environ.get('APP_PORT', 8080)
	)
