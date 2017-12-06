from flask import Flask, render_template, request, redirect
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


@app.route('/ask/<int:ask_id>', methods=['GET'])
def view_ask(ask_id):
	conn = get_db()

	with conn.cursor() as cursor :
		cursor.execute("SELECT * FROM `ask` WHERE id = %s", (ask_id, ))
		row = cursor.fetchone()

		cursor.execute("SELECT * FROM `cheer` WHERE ask_id = %s", (ask_id, ))
		rows2 = cursor.fetchall()

		print(rows2)

	return render_template('detail.html',
		message=row[1],
		register_time=row[2],
		cheers=rows2,
	)


@app.route('/ask', methods=['POST'])
def add_ask():
	conn = get_db()
	message = request.form.get('message')

	with conn.cursor() as cursor :
		sql = "INSERT INTO `ask` (`message`) VALUES (%s)"
		r = cursor.execute(sql, (message, ))

	id = conn.insert_id()
	conn.commit()

	return redirect("/#a" + str(id))


@app.route('/cheer', methods=['POST'])
def add_cheer():
	conn = get_db()
	ask_id = request.form.get('ask_id')
	message = request.form.get('message')

	with conn.cursor() as cursor :
		sql = "INSERT INTO `cheer` (`ask_id`, `message`) VALUES (%s, %s)"
		r = cursor.execute(sql, (ask_id, message))

	conn.commit()

	return redirect("/#c" + ask_id)




if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		debug=True,
		port=os.environ.get('APP_PORT', 8080)
	)
