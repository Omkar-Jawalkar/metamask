from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/c55dbd23679842e78af0e673cff4b110"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)


print(web3.eth.get_balance('0x955E55C04Fcc4dc68F7C7794e2CBC5c34BF50166'))

print(web3.eth.get_block(1))


