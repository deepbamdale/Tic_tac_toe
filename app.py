from flask import Flask, jsonify, request


playerinfo = [{
    'name': 'dipali',
    'symbol': 'X'
},
 {
    'name': 'minal',
    'symbol': 'O'
}]

app = Flask(__name__)


# retrieve all playerinfo
@app.route('/players')
def get_allplayer():
    return jsonify({'players': playerinfo})


# retrieve all one playerinfo.
@app.route('/player/<string:name>')
def get_oneplayerinfo(name):
    for player in playerinfo:
        if player['name'] == name:
            return jsonify(player)

    return jsonify({'message': 'player not found'})


# create a new player .
@app.route('/player', methods=["POST"])
def player_input():
    request_data = request.get_json()
    playerinfo.append(request_data)
    return jsonify({"message": "Player has been added"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
