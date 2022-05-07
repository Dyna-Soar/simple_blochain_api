from flask import Flask
import json

from blockchain_first import Blockchain, Block

app = Flask(__name__)

chain_test = Blockchain()


@app.route("/")
def show_blockchain():
    blockchain_chain = chain_test.get_blockchain()
    return "<p>" + str(blockchain_chain) + "</p>"


@app.route("/mine_block")
def mine_block():
    chain_test.add_block()
    blockchain_chain = chain_test.get_blockchain()
    print(blockchain_chain)
    return "<p>" + str(blockchain_chain) + "</p>"