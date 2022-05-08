import flask
from flask import Flask
import json

from blockchain_first import Blockchain, Block

app = Flask(__name__)

chain_test = Blockchain()


@app.route("/")
def show_blockchain():
    response = chain_test.get_json_blockchain()
    return response, 200


@app.route("/mine_block")
def mine_block():
    chain_test.add_block()
    response = chain_test.get_json_blockchain()
    return response, 200
