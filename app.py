import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == '__main__':
	app.debug = True
	app.run()


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
	if request.method == 'GET':
		pass  # Handle GET all Request
	elif request.method == 'POST':
		data = request.form
		result = add_song(data['artist'], data['title'], data['rating'])
		return jsonify(result)


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(song_id):
	if request.method == 'GET':
		pass  # Handle GET single request
	elif request.method == 'PUT':
		pass  # Handle UPDATE request
	elif request.method == 'DELETE':
		pass  # Handle DELETE request


def add_song(artist, title, rating):
	try:
		with sqlite3.connect('songs.db') as connection:
			cursor = connection.cursor()
			cursor.execute("""
                INSERT INTO songs (artist, title, rating) VALUES (?, ?, ?);
                """, (artist, title, rating,))
			result = {'status': 1, 'message': 'Song Added'}
	except:
		result = {'status': 0, 'message': 'error'}
	return result