from flask import Flask, render_template, request
import os

from core.dbdriver import get_db, init_tables

app = Flask(__name__)

init_tables()

@app.route('/')
def index():
	with get_db().cursor() as cursor :
		cursor.execute("SELECT *, (SELECT COUNT(*) FROM `cheer`WHERE ask_id = ask.id) AS cheer_cnt FROM `ask`")
		result = cursor.fetchall()

	return render_template('main.html',
		dataset=result,
	)

@app.route('/ask', methods=['POST'])
def add_ask():
	message = request.form.get('message')

	with get_db().cursor() as cursor :
		sql = "INSERT INTO `ask` (`message`) VALUES (%s)"
		r = cursor.execute(sql, (message, ))

	return render_template('redirection.html', success=r)


@app.route('/cheer', methods=['POST'])
def add_cheer():
	ask_id = request.form.get('ask_id')
	message = request.form.get('message')

	with get_db().cursor() as cursor :
		sql = "INSERT INTO `cheer` (`ask_id`, `message`) VALUES (%s, %s)"
		r = cursor.execute(sql, (ask_id, message))

	return render_template('redirection.html', success=r)




if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		debug=True,
		port=os.environ.get('APP_PORT', 8080)
	)
