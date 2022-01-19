from main import BlockChain
from flask import Flask, jsonify

app = Flask(__name__)

blockchain = BlockChain()

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'congartulations you just mined a block!!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],

                }

    return jsonify(response), 200

@app.route('/get_chain', methods= ['GET'])
def get_chain():
    response = {'blockchain': blockchain.chain,
                'blockchain_length':len(blockchain.chain)
                }
    return jsonify(response), 200

@app.route('/is_valid', methods= ['GET'])
def is_valid():
    response = blockchain.is_chain_valid(blockchain.chain)
    if response == False:
        return "not valid"
    else:
        return "valid"



