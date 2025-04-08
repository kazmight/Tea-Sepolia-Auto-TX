from web3 import Web3, HTTPProvider
import json
import random
import time
import sys
from web3.exceptions import ContractLogicError

# Colors for terminal output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Transaction types mapping
TRANSACTION_TYPES = {
    'native': 'Native Transfer',
    'deploy': 'Contract Deployment',
    'interact': 'Contract Interaction',
    'token': 'Token Transfer'
}

# [Rest of your existing imports and setup code...]

# Intro
print(f'{YELLOW}T{RED}e{CYAN}a {MAGENTA}S{GREEN}e{YELLOW}p{RED}o{CYAN}l{MAGENTA}i{YELLOW}a {GREEN}T{RED}e{YELLOW}s{CYAN}t{MAGENTA}n{GREEN}e{YELLOW}t {RED}B{CYAN}y {MAGENTA}I{YELLOW}N{GREEN}V{RED}I{YELLOW}C{CYAN}T{MAGENTA}U{YELLOW}S {GREEN}L{RED}A{YELLOW}B{CYAN}S{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Native {YELLOW}To {RED}Random {GREEN}Recipient {YELLOW}Address{RESET}')
print(f'{YELLOW}- {RED}Auto {GREEN}Deploy {YELLOW}Contract{RESET}')
print(f'{RED}- {GREEN}Auto {YELLOW}Interaction {RED}Contract{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Spesific {YELLOW}Token {RED}To {GREEN}Random {YELLOW}Recipient {RED}Address{RESET}\n')

# Setup Web3
web3 = Web3(Web3.HTTPProvider("https://tea-sepolia.g.alchemy.com/public"))
chainId = web3.eth.chain_id

# Contract data and ABI
datadeploy = "0x6080604052348015600f57600080fd5b5061036a8061001f6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063031d5d011461003b578063b588bfad14610059575b600080fd5b61004361006e565b6040516100509190610112565b60405180910390f35b61006c610067366004610161565b610100565b005b60606000805461007d906101d3565b80601f01602080910402602001604051908101604052809291908181526020018280546100a9906101d3565b80156100f65780601f106100cb576101008083540402835291602001916100f6565b820191906000526020600020905b8154815290600101906020018083116100d957829003601f168201915b5050505050905090565b600061010d828483610273565b505050565b60006020808352835180602085015260005b8181101561014057858101830151858201604001528201610124565b506000604082860101526040601f19601f8301168501019250505092915050565b6000806020838503121561017457600080fd5b823567ffffffffffffffff8082111561018c57600080fd5b818501915085601f8301126101a057600080fd5b8135818111156101af57600080fd5b8660208285010111156101c157600080fd5b60209290920196919550909350505050565b600181811c908216806101e757607f821691505b60208210810361020757634e487b7160e01b600052602260045260246000fd5b50919050565b634e487b7160e01b600052604160045260246000fd5b601f82111561010d576000816000526020600020601f850160051c8101602086101561024c5750805b601f850160051c820191505b8181101561026b57828155600101610258565b505050505050565b67ffffffffffffffff83111561028b5761028b61020d565b61029f8361029983546101d3565b83610223565b6000601f8411600181146102d357600085156102bb5750838201355b600019600387901b1c1916600186901b17835561032d565b600083815260209020601f19861690835b8281101561030457868501358255602094850194600190920191016102e4565b50868210156103215760001960f88860031b161c19848701351681555b505060018560011b0183555b505050505056fea264697066735822122055624fd2cb38f0bfa640ac81ca40f9a0bc410d13e12db84e10a0e36edf4217c664736f6c63430008190033"

msg_abi = json.loads('[{"inputs": [{"internalType": "string","name": "newMessage","type": "string"}],"name": "writeMessage","outputs": [],"stateMutability": "nonpayable","type": "function"}]')

token_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')

def get_base_gas_price():
    """Retrieve the base gas price from the latest block."""
    try:
        latest_block = web3.eth.get_block('latest')
        return latest_block['baseFeePerGas']
    except Exception as e:
        print(f"{YELLOW}Error getting base fee: {e}{RESET}")
        return web3.to_wei(30, 'gwei')  # Fallback base fee

def get_gas_parameters():
    """Get safe gas parameters with proper validation"""
    try:
        base_fee = get_base_gas_price()
        max_priority = int(base_fee * 0.1)  # 10% of base fee
        max_fee = base_fee + max_priority
        return {
            'maxFeePerGas': min(max_fee, web3.to_wei(150, 'gwei')),  # Cap at 150 gwei
            'maxPriorityFeePerGas': min(max_priority, web3.to_wei(2, 'gwei')),  # Cap at 2 gwei
            'gas': 21000  # Default gas for simple transfers
        }
    except Exception as e:
        print(f"{YELLOW}Using fallback gas parameters: {e}{RESET}")
        return {
            'maxFeePerGas': web3.to_wei(50, 'gwei'),
            'maxPriorityFeePerGas': web3.to_wei(1, 'gwei'),
            'gas': 21000
        }

def sendNative(sender, key, amount, recipient):
    try:
        # Validate inputs
        if not web3.is_address(recipient):
            print(f"{RED}Invalid recipient address{RESET}")
            return False

        # Get gas parameters
        gas_params = get_gas_parameters()
        
        # Convert amount
        amount_wei = web3.to_wei(amount, 'ether')
        
        # Build transaction
        tx = {
            'chainId': chainId,
            'to': recipient,
            'value': amount_wei,
            'nonce': web3.eth.get_transaction_count(sender),
            **gas_params
        }

        # Check balance
        balance = web3.eth.get_balance(sender)
        required = amount_wei + (tx['gas'] * tx['maxFeePerGas'])
        if balance < required:
            print(f"{RED}Insufficient balance: Need {web3.from_wei(required, 'ether'):.6f} ETH, has {web3.from_wei(balance, 'ether'):.6f} ETH{RESET}")
            return False

        # Sign and send
        signed = web3.eth.account.sign_transaction(tx, key)
        raw_tx = signed.rawTransaction if hasattr(signed, 'rawTransaction') else signed.raw_transaction
        tx_hash = web3.eth.send_raw_transaction(raw_tx)
        
        print(f"{CYAN}Sending {amount:.6f} ETH...{RESET}")
        
        # Wait for receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        
        if receipt.status == 1:
            print(f"{GREEN}Success! TX: {web3.to_hex(tx_hash)}{RESET}")
            return True
        else:
            print(f"{RED}Transaction failed (status 0){RESET}")
            return False
            
    except Exception as e:
        print(f"{RED}Error: {type(e).__name__}: {e}{RESET}")
        return False
        
def writeContract(sender, key, ctraddr):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (5*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        msg_contract = web3.eth.contract(address=web3.to_checksum_address(ctraddr), abi=msg_abi)
        gasAmount = msg_contract.functions.writeMessage("test").estimate_gas({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        msg_tx = msg_contract.functions.writeMessage("test").build_transaction({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        })
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(msg_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Interaction On Contract {ctraddr} From {sender} ...')
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'{GREEN}Interaction On Contract {ctraddr} From {sender} Success!{RESET}')
        print(f'{GREEN}TX-ID : {str(web3.to_hex(tx_hash))}{RESET}')
        return True
    except Exception as e:
        print(f'{RED}Error interacting with contract: {e}{RESET}')
        return False

def deployContract(sender, key):
    try:
        # Get gas parameters with higher gas limit for deployment
        gas_params = get_gas_parameters()
        gas_params['gas'] = 2000000  # Higher gas limit for deployments
        
        # Build transaction
        tx = {
            'chainId': chainId,
            'from': sender,
            'data': datadeploy,
            'nonce': web3.eth.get_transaction_count(sender),
            **gas_params
        }

        # Check balance
        balance = web3.eth.get_balance(sender)
        required = tx['gas'] * tx['maxFeePerGas']
        if balance < required:
            print(f"{RED}Insufficient balance for deployment: Need {web3.from_wei(required, 'ether'):.6f} ETH{RESET}")
            return None, False

        # Sign and send
        signed = web3.eth.account.sign_transaction(tx, key)
        raw_tx = signed.rawTransaction if hasattr(signed, 'rawTransaction') else signed.raw_transaction
        tx_hash = web3.eth.send_raw_transaction(raw_tx)
        
        print(f"{CYAN}Deploying contract...{RESET}")
        
        # Wait for receipt with longer timeout
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)
        
        if receipt.status == 1:
            contract_address = receipt.contractAddress
            print(f"{GREEN}Deployment successful! Contract: {contract_address}{RESET}")
            print(f"{GREEN}TX: {web3.to_hex(tx_hash)}{RESET}")
            return contract_address, True
        else:
            print(f"{RED}Contract deployment failed (status 0){RESET}")
            return None, False
            
    except Exception as e:
        print(f"{RED}Deployment error: {type(e).__name__}: {e}{RESET}")
        return None, False


def sendNative(sender, key, amount, recipient):
    try:
        # Validate inputs
        if not web3.is_address(recipient):
            print(f"{RED}Invalid recipient address{RESET}")
            return False

        # Get gas parameters
        gas_params = get_gas_parameters()
        
        # Convert amount
        amount_wei = web3.to_wei(amount, 'ether')
        
        # Build transaction
        tx = {
            'chainId': chainId,
            'to': recipient,
            'value': amount_wei,
            'nonce': web3.eth.get_transaction_count(sender),
            **gas_params
        }

        # Check balance
        balance = web3.eth.get_balance(sender)
        required = amount_wei + (tx['gas'] * tx['maxFeePerGas'])
        if balance < required:
            print(f"{RED}Insufficient balance: Need {web3.from_wei(required, 'ether'):.6f} ETH, has {web3.from_wei(balance, 'ether'):.6f} ETH{RESET}")
            return False

        # Sign and send
        signed = web3.eth.account.sign_transaction(tx, key)
        raw_tx = signed.rawTransaction if hasattr(signed, 'rawTransaction') else signed.raw_transaction
        tx_hash = web3.eth.send_raw_transaction(raw_tx)
        
        print(f"{CYAN}Sending {amount:.6f} ETH...{RESET}")
        
        # Wait for receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        
        if receipt.status == 1:
            print(f"{GREEN}Success! TX: {web3.to_hex(tx_hash)}{RESET}")
            return True
        else:
            print(f"{RED}Transaction failed (status 0){RESET}")
            return False
            
    except Exception as e:
        print(f"{RED}Error: {type(e).__name__}: {e}{RESET}")
        return False
        
def get_random_address_from_block(block_number=None):
    try:
        # If no block number is provided, get the latest block
        if block_number is None:
            block = web3.eth.get_block('latest', full_transactions=True)
        else:
            block = web3.eth.get_block(block_number, full_transactions=True)

        # Collect addresses involved in transactions (both from and to addresses)
        addresses = set()  # Use a set to avoid duplicates
        
        for tx in block['transactions']:
            sender = tx['from']
            recipient = tx['to']
            
            addresses.add(sender)
            if recipient:
                addresses.add(recipient)
        
        if not addresses:
            print(f"{YELLOW}No addresses found in this block.{RESET}")
            return None

        # Randomly select an address from the set of addresses
        random_address = random.choice(list(addresses))
        return random_address
    
    except Exception as e:
        print(f"{RED}Error while fetching block data: {e}{RESET}")
        return None

# Get user inputs
amountmin = float(input('Min Send Amount : '))
amountmax = float(input('Max Send Amount : '))
tknaddr = web3.to_checksum_address(input('Input Token Address : '))
total_runs = int(input('How many transactions to run? (e.g., 100) : '))
print(f'')


def sendTX():
    try:
        with open('pvkeylist.txt', 'r') as file:
            local_data = file.read().splitlines()

            if not local_data:
                print(f"{RED}Notice: 'pvkeylist.txt' is empty. Exiting...{RESET}")
                sys.exit(1)

            for pvkeylist in local_data:
                try:
                    sender = web3.eth.account.from_key(pvkeylist)
                except ValueError:
                    print(f"{RED}Invalid private key format. Skipping...{RESET}")
                    continue
                
                successful_txs = 0
                failed_txs = 0
                
                for run in range(1, total_runs + 1):
                    print(f'\n{MAGENTA}=== Transaction {run} of {total_runs} ==={RESET}')
                    
                    try:
                        # Check native balance first
                        balance = web3.eth.get_balance(sender.address)
                        if balance < web3.to_wei(0.01, 'ether'):
                            print(f'{YELLOW}Low balance: {web3.from_wei(balance, "ether")} ETH. Skipping...{RESET}')
                            failed_txs += 1
                            time.sleep(2)
                            continue
                            
                        recipient = web3.to_checksum_address(get_random_address_from_block())
                        amountrandom = random.uniform(amountmin, amountmax)
                        
                        # Add increasing delay between transactions
                        time.sleep(1 + (run * 0.1))
                        
                        # Transaction sequence with logging
                        tx_results = {}
                        
                        # 1. Native Transfer
                        print(f'\n{CYAN}1. {TRANSACTION_TYPES["native"]}{RESET}')
                        tx_results['native'] = sendNative(sender.address, sender.key, amountrandom, recipient)
                        
                        # 2. Contract Deployment
                        print(f'\n{CYAN}2. {TRANSACTION_TYPES["deploy"]}{RESET}')
                        ctraddr, tx_results['deploy'] = deployContract(sender.address, sender.key)
                        
                        # 3. Contract Interaction
                        print(f'\n{CYAN}3. {TRANSACTION_TYPES["interact"]}{RESET}')
                        if tx_results['deploy'] and ctraddr:
                            tx_results['interact'] = writeContract(sender.address, sender.key, ctraddr)
                        else:
                            print(f"{YELLOW}Skipping interaction - deployment failed{RESET}")
                            tx_results['interact'] = False
                        
                        # 4. Token Transfer
                        print(f'\n{CYAN}4. {TRANSACTION_TYPES["token"]}{RESET}')
                        tx_results['token'] = sendToken(sender.address, sender.key, tknaddr, amountrandom, recipient)
                        
                        # Transaction summary
                        print(f'\n{YELLOW}=== Transaction {run} Summary ==={RESET}')
                        for tx_type, success in tx_results.items():
                            status = f"{GREEN}✓ Success{RESET}" if success else f"{RED}✗ Failed{RESET}"
                            print(f"{TRANSACTION_TYPES[tx_type]}: {status}")
                        
                        # Update counters
                        if all(tx_results.values()):
                            successful_txs += 1
                        else:
                            failed_txs += 1
                            
                    except Exception as e:
                        print(f'{RED}Transaction sequence failed: {e}{RESET}')
                        failed_txs += 1
                        time.sleep(5)
                        continue
                
                print(f'\n{CYAN}=== Account Summary ==={RESET}')
                print(f'{GREEN}Successful: {successful_txs}{RESET}')
                print(f'{RED}Failed: {failed_txs}{RESET}')
                print(f'{YELLOW}Success rate: {successful_txs/total_runs*100:.2f}%{RESET}\n')
                
    except Exception as e:
        print(f'{RED}Fatal error: {e}{RESET}')
sendTX()
