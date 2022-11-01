from web3 import Web3 
ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

account1 = '0x3c31b9f2aD8e82283d2630a697e46D23a0433a79'
account2 = '0x1d2E16F126640A762F8b19E3D4DEB2E0a79E7DED'

private_key = '87a24e14deceee9801968b274e197737a2ef489b847f41dfafbd48c76882923c'


nonce = web3.eth.getTransactionCount(account1)
tx = {    
    'nonce' : nonce,
    'to': account2,
    'value': web3.toWei(12, 'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei(50, 'gwei'),

}

signed_tx = web3.eth.account.signTransaction(tx, private_key) # here a transaction is signed
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction) # here a transaction is sent to the network

print(tx_hash)








