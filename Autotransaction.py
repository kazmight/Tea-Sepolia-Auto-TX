from web3 import Web3, HTTPProvider
import json
import random
import secrets
import time
import sys

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Banner dengan warna rainbow
print(f'{RED}H{YELLOW}e{GREEN}l{YELLOW}l{RED}o {CYAN}E{MAGENTA}V{GREEN}M {YELLOW}T{RED}e{CYAN}a {MAGENTA}S{GREEN}e{YELLOW}p{RED}o{CYAN}l{MAGENTA}i{YELLOW}a {GREEN}T{RED}e{YELLOW}s{CYAN}t{MAGENTA}n{GREEN}e{YELLOW}t {RED}B{CYAN}y {MAGENTA}A{YELLOW}D{GREEN}F{RED}M{YELLOW}I{CYAN}D{MAGENTA}N {GREEN}T{YELLOW}e{RED}a{CYAN}m{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Native {YELLOW}To {RED}Random {GREEN}Recipient {YELLOW}Address{RESET}')
print(f'{YELLOW}- {RED}Auto {GREEN}Deploy {YELLOW}Contract{RESET}')
print(f'{RED}- {GREEN}Auto {YELLOW}Interaction {RED}Contract{RESET}')
print(f'{GREEN}- {YELLOW}Auto {RED}Send {GREEN}Spesific {YELLOW}Token {RED}To {GREEN}Random {YELLOW}Recipient {RED}Address{RESET}')
print(f'')

print(f'- Tea Sepolia Auto Transaction By INVICTUS LABS')
print(f'- Auto Send Native To Random Recipient Address')
print(f'- Auto Deploy Contract')
print(f'- Auto Interaction Contract')
print(f'- Auto Send Spesific Token To Random Recipient Address')
print(f'')

web3 = Web3(Web3.HTTPProvider("https://tea-sepolia.g.alchemy.com/public"))
chainId = web3.eth.chain_id

# ... (bagian sebelumnya tetap sama sampai fungsi sendNative) ...

def sendNative(sender, key, amount, recipient):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (10*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        totalamount = web3.to_wei(amount, 'ether')
        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'to': recipient,
            'value': totalamount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        native_tx = {
            'chainId': chainId,
            'from': sender,
            'to': recipient,
            'value': totalamount,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        }
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(native_tx, key).rawTransaction)
        #get transaction hash
        print(f'{YELLOW}Processing Send {amount} Native From {sender} To {recipient} ...{RESET}')
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status == 1:
            print(f'{GREEN}Send {amount} Native From {sender} To {recipient} Success!{RESET}')
            print(f'{GREEN}TX-ID : {str(web3.to_hex(tx_hash))}{RESET}')
            return True
        else:
            print(f'{RED}Send {amount} Native From {sender} To {recipient} Failed!{RESET}')
            print(f'{RED}TX-ID : {str(web3.to_hex(tx_hash))}{RESET}')
            return False
            
    except Exception as e:
        print(f'{RED}Error : {e}{RESET}')
        return False

# Modifikasi serupa untuk fungsi lainnya (sendToken, writeContract, deployContract)
# Contoh untuk sendToken:

def sendToken(sender, key, ctraddr, amount, recipient):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (5*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        totalamount = web3.to_wei(amount, 'ether')
        token_contract = web3.eth.contract(address=web3.to_checksum_address(ctraddr), abi=token_abi)
        nametkn = token_contract.functions.name().call()
        gasAmount = token_contract.functions.transfer(recipient, totalamount).estimate_gas({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        token_tx = token_contract.functions.transfer(recipient, totalamount).build_transaction({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        })
        
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(token_tx, key).rawTransaction)
        print(f'{YELLOW}Processing Send {amount} {nametkn} From {sender} To {recipient} ...{RESET}')
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status == 1:
            print(f'{GREEN}Send {amount} {nametkn} From {sender} To {recipient} Success!{RESET}')
            print(f'{GREEN}TX-ID : {str(web3.to_hex(tx_hash))}{RESET}')
            return True
        else:
            print(f'{RED}Send {amount} {nametkn} From {sender} To {recipient} Failed!{RESET}')
            print(f'{RED}TX-ID : {str(web3.to_hex(tx_hash))}{RESET}')
            return False
            
    except Exception as e:
        print(f'{RED}Error : {e}{RESET}')
        return False

# Modifikasi serupa untuk writeContract dan deployContract

def sendTX():
    try:
        num_transactions = int(input('Masukkan jumlah transaksi yang ingin dijalankan: '))
        success_count = 0
        failed_count = 0
        
        with open('pvkeylist.txt', 'r') as file:
            local_data = file.read().splitlines()

            if not local_data:
                print(f"{RED}Notice: 'pvkeylist.txt' is empty. Exiting...{RESET}")
                sys.exit(1)

            for _ in range(num_transactions):
                for pvkeylist in local_data:
                    try:
                        sender = web3.eth.account.from_key(pvkeylist)
                    except ValueError:
                        print(f"{RED}Notice: Invalid private key format. Exiting...{RESET}")
                        sys.exit(1)
                    
                    sender = web3.eth.account.from_key(pvkeylist)
                    recipient = web3.to_checksum_address(get_random_address_from_block())
                    amountrandom = random.uniform(amountmin, amountmax)
                    
                    # Eksekusi transaksi dengan penanganan status
                    if sendNative(sender.address, sender.key, amountrandom, recipient):
                        success_count += 1
                    else:
                        failed_count += 1
                    print(f'')
                    
                    ctraddr = deployContract(sender.address, sender.key)
                    print(f'')
                    
                    if writeContract(sender.address, sender.key, ctraddr):
                        success_count += 1
                    else:
                        failed_count += 1
                    print(f'')
                    
                    if sendToken(sender.address, sender.key, tknaddr, amountrandom, recipient):
                        success_count += 1
                    else:
                        failed_count += 1
                    print(f'')
                    
                    time.sleep(1)
        
        # Tampilkan ringkasan
        print(f'\n{GREEN}Transaksi Sukses: {success_count}{RESET}')
        print(f'{RED}Transaksi Gagal: {failed_count}{RESET}')
        print(f'{YELLOW}Total Transaksi: {success_count + failed_count}{RESET}')
                    
    except Exception as e:
        print(f'{RED}Error : {e}{RESET}')
        pass

# Meminta input parameter
amountmin = float(input('Min Send Amount : '))
amountmax = float(input('Max Send Amount : '))
tknaddr = web3.to_checksum_address(input('Input Token Address : '))
print(f'')         

# Jalankan fungsi utama
sendTX()
