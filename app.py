from flask import Flask, jsonify
from rocket import Player, Rocket, Game
from bullet.bullets import Bullet
from explosion.explosions import Explosion
from mob.mobs import Mob
from pow.pows import Pow


app = Flask(__name__)


@app.route("/")
def rocket():
    """This function will return an html page with a table of rocket game
    Returns:
        HTML Template: The HTML page with the table
    """
    game = Game()
    return game.run()


@app.route("/player", methods=["GET"])
def get_player():
    """This function returns JSON objects for player

    Returns:
        JSON: Objects representing the player
    """
    player = Player()
    return jsonify(player.to_dict()), 200


@app.route("/rocket", methods=["GET"])
def get_rocket():
    """This function returns JSON objects for rocket
    Returns:
        JSON: Objects representing rocket
    """
    rocket = Rocket()
    return jsonify(rocket.to_dict()), 200


@app.route("/bullet", methods=["GET"])
def get_bullet():
    """This function returns JSON objects for the bullets

    Returns:
        JSON: Objects representing bullets
    """
    bullet = Bullet()
    return jsonify(bullet.to_dict()), 200


@app.route("/explosion", methods=["GET"])
def get_explosion():
    """This function returns JSON objects for explosion

    Returns:
        JSON: Objects representing explosion
    """
    explosion = Explosion()
    return jsonify(explosion.to_dict()), 200


@app.route("/mob", methods=["GET"])
def get_mob():
    """This function returns JSON objects for mob

    Returns:
        JSON: Objects representing mob
    """
    mob = Mob()
    return jsonify(mob.to_dict()), 200


@app.route("/pow", methods=["GET"])
def get_pow():
    """This function returns JSON objects for power up

    Returns:
        JSON: Objects representing power up
    """
    pow = Pow()
    return jsonify(pow.to_dict()), 200


if __name__ == "__main__":
    app.run(debug=True)
