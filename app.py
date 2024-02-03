import os
import json
from dotenv import load_dotenv
from web3 import Web3, Account, HTTPProvider
from flask import Flask, render_template, request

# load environment variables from .env file
load_dotenv('.env')

# web3.py instance
w3 = Web3(HTTPProvider(os.environ.get('RPC_URL'))) 
print('Web3 Connected:',w3.isConnected())

# account setup
private_key= os.environ.get('PRIVATE_KEY') #private key of the account
public_key = Account.from_key(private_key)
account_address = public_key.address

# Contract instance
contract_artifacts_file = json.load(open('./contracts/ProductRegistry.json'))
abi = contract_artifacts_file['abi']
contract_address = os.environ.get('CONTRACT_ADDRESS')
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

app = Flask(__name__)

@app.route("/")
def index():
    product_count = contract_instance.functions.showAll().call()
    return render_template("index.html", product_count=product_count)

@app.route("/registerProduct", methods=['POST'])
def register_product():
    # Convert ID to integer as Solidity expects uint256
    ID = int(request.form.get("ID"))
    holderName = request.form.get("holderName")
    location = request.form.get("location")
    city = request.form.get("city")
    vehical = request.form.get("vehical")

    # Build the transaction
    tx = contract_instance.functions.register(ID, holderName, location, city, vehical).buildTransaction({
        'from': account_address,  # Set the sender address
        'nonce': w3.eth.getTransactionCount(account_address),  # Get the nonce for the account
        'gas': 2000000,  # Set the gas limit for the transaction
        'gasPrice': w3.eth.gasPrice  # Set the gas price for the transaction
    })

    # Sign the transaction with the private key
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Wait for the transaction to be mined
    w3.eth.waitForTransactionReceipt(tx_hash)

    # Assuming productCount is a function that returns the number of products
    # If it's not available, you'll need to adjust the following line accordingly
    product_count = len(contract_instance.functions.showAll().call())

    # Render the template with the updated product count
    return render_template("index.html", product_count=product_count)

@app.route("/showAllProducts")
def show_all_products():
    all_products = contract_instance.functions.showAll().call()
    return {'products': all_products}

@app.route("/changeHolder", methods=['POST'])
def change_holder():
    ID = int(request.form.get("ID"))
    newHolderName = request.form.get("newHolderName")
    tx = contract_instance.functions.changeHolder(ID, newHolderName).buildTransaction({
        'from': account_address,
        'nonce': w3.eth.getTransactionCount(account_address),
        'gas': 2000000,
        'gasPrice': w3.eth.gasPrice
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return index()



if __name__ == '__main__':
    app.run(port=8444, host='localhost')
