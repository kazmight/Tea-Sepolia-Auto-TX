from web3 import Web3
import json, random, time, sys

# Colors for terminal output
GREEN, YELLOW, RED, CYAN, MAGENTA, RESET = '\033[92m', '\033[93m', '\033[91m', '\033[96m', '\033[95m', '\033[0m'

# Intro
print(f'{RED}H{YELLOW}e{GREEN}l{YELLOW}l{RED}o {CYAN}E{MAGENTA}V{GREEN}M {YELLOW}T{RED}e{CYAN}a {MAGENTA}S{GREEN}e{YELLOW}p{RED}o{CYAN}l{MAGENTA}i{YELLOW}a {GREEN}T{RED}e{YELLOW}s{CYAN}t{MAGENTA}n{GREEN}e{YELLOW}t {RED}B{CYAN}y {MAGENTA}I{YELLOW}N{GREEN}V{RED}I{YELLOW}C{CYAN}T{MAGENTA}U{YELLOW}S {GREEN}L{RED}A{YELLOW}B{CYAN}S{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Native {YELLOW}To {RED}Random {GREEN}Recipient {YELLOW}Address{RESET}')
print(f'{YELLOW}- {RED}Auto {GREEN}Deploy {YELLOW}Contract{RESET}')
print(f'{RED}- {GREEN}Auto {YELLOW}Interaction {RED}Contract{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Spesific {YELLOW}Token {RED}To {GREEN}Random {YELLOW}Recipient {RED}Address{RESET}\n')

# Setup Web3
web3 = Web3(Web3.HTTPProvider("https://tea-sepolia.g.alchemy.com/public"))
chainId = web3.eth.chain_id

# Contract data and ABI
datadeploy = "0x6080..."  # use your full deploy data here
msg_abi = json.loads('[{"inputs": [{"internalType": "string","name": "newMessage","type": "string"}],"name": "writeMessage","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
token_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},...]')  # your full ABI

def get_base_gas_price():
    block = web3.eth.get_block('latest')
    return block.get('baseFeePerGas', web3.to_wei('5', 'gwei'))

def sign_and_send(tx, key):
    signed_tx = web3.eth.account.sign_transaction(tx, key)
    return web3.eth.send_raw_transaction(signed_tx.raw_transaction)

def send_native(sender, key, amount, recipient):
    try:
        gas_price = int(get_base_gas_price() * 1.1)
        tx = {
            'chainId': chainId,
            'from': sender,
            'to': recipient,
            'value': web3.to_wei(amount, 'ether'),
            'nonce': web3.eth.get_transaction_count(sender),
            'gasPrice': gas_price,
        }
        tx['gas'] = web3.eth.estimate_gas({k: tx[k] for k in ['from', 'to', 'value']})
        tx_hash = sign_and_send(tx, key)
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"{GREEN}Sent {amount} ETH to {recipient} — TX: {web3.to_hex(tx_hash)}{RESET}")
    except Exception as e:
        print(f"{RED}Native TX error: {e}{RESET}")

def deploy_contract(sender, key):
    try:
        gas_price = int(get_base_gas_price() * 1.1)
        tx = {
            'chainId': chainId,
            'from': sender,
            'data': datadeploy,
            'nonce': web3.eth.get_transaction_count(sender),
            'gasPrice': gas_price,
        }
        tx['gas'] = web3.eth.estimate_gas({'from': sender, 'data': datadeploy})
        tx_hash = sign_and_send(tx, key)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"{CYAN}Contract deployed: {receipt.contractAddress} — TX: {web3.to_hex(tx_hash)}{RESET}")
        return receipt.contractAddress
    except Exception as e:
        print(f"{RED}Contract Deploy Error: {e}{RESET}")
        return None

def write_contract(sender, key, ctraddr):
    try:
        gas_price = int(get_base_gas_price() * 1.1)
        contract = web3.eth.contract(address=ctraddr, abi=msg_abi)
        tx = contract.functions.writeMessage("test").build_transaction({
            'chainId': chainId,
            'from': sender,
            'nonce': web3.eth.get_transaction_count(sender),
            'gasPrice': gas_price
        })
        tx['gas'] = contract.functions.writeMessage("test").estimate_gas({'from': sender})
        tx_hash = sign_and_send(tx, key)
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"{CYAN}Interaction with contract {ctraddr} successful — TX: {web3.to_hex(tx_hash)}{RESET}")
    except Exception as e:
        print(f"{RED}Contract Interaction Error: {e}{RESET}")

def send_token(sender, key, ctraddr, amount, recipient):
    try:
        contract = web3.eth.contract(address=ctraddr, abi=token_abi)
        gas_price = int(get_base_gas_price() * 1.05)
        decimals = contract.functions.decimals().call()
        amt = int(amount * (10 ** decimals))
        tx = contract.functions.transfer(recipient, amt).build_transaction({
            'chainId': chainId,
            'from': sender,
            'nonce': web3.eth.get_transaction_count(sender),
            'gasPrice': gas_price
        })
        tx['gas'] = contract.functions.transfer(recipient, amt).estimate_gas({'from': sender})
        tx_hash = sign_and_send(tx, key)
        web3.eth.wait_for_transaction_receipt(tx_hash)
        name = contract.functions.name().call()
        print(f"{GREEN}Sent {amount} {name} to {recipient} — TX: {web3.to_hex(tx_hash)}{RESET}")
    except Exception as e:
        print(f"{RED}Token Send Error: {e}{RESET}")

def get_random_address():
    try:
        block = web3.eth.get_block('latest', full_transactions=True)
        addrs = {tx['from'] for tx in block.transactions}
        addrs |= {tx['to'] for tx in block.transactions if tx['to']}
        return random.choice(list(addrs))
    except:
        return web3.to_checksum_address("0x000000000000000000000000000000000000dead")

# === Input Configuration ===
amountmin = float(input('Min Send Amount : '))
amountmax = float(input('Max Send Amount : '))
token_address = web3.to_checksum_address(input('Input Token Address : '))
print()

# === Main Loop ===
def sendTX():
    try:
        with open('pvkeylist.txt', 'r') as f:
            keys = [k.strip() for k in f.readlines() if k.strip()]
        if not keys:
            print("No keys in pvkeylist.txt")
            return
        for key in keys:
            acct = web3.eth.account.from_key(key)
            sender = acct.address
            recipient = get_random_address()
            amt = random.uniform(amountmin, amountmax)
            send_native(sender, key, amt, recipient)
            ctr = deploy_contract(sender, key)
            if ctr:
                write_contract(sender, key, ctr)
                send_token(sender, key, token_address, amt, recipient)
            print()
            time.sleep(5)
    except Exception as e:
        print(f"{RED}Main Loop Error: {e}{RESET}")

sendTX()
