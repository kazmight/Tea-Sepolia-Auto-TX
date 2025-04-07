Tea Sepolia Testnet

![Banner](https://img.shields.io/badge/Helper-EVM_Tea_Sepolia_Testnet-brightgreen)
![Version](https://img.shields.io/badge/Version-2.0-blue)
![License](https://img.shields.io/badge/License-MIT-orange)

Script otomatis untuk berinteraksi dengan jaringan EVM Tea Sepolia Testnet. Dibuat oleh **INVICTUS LABS**.

## 🌟 Fitur Utama

- 🚀 **Auto Send Native** - Mengirim aset native ke alamat acak
- 📜 **Auto Deploy Contract** - Melakukan deploy kontrak cerdas
- 🤖 **Auto Interaction Contract** - Berinteraksi dengan kontrak yang sudah terdeploy
- 💰 **Auto Send Token** - Mengirim token spesifik ke alamat acak
- 🎨 **Colorful Output** - Status transaksi dengan warna (hijau/kuning/merah)

## 🛠️ Persyaratan

- Python 3.8+
- Library Web3.py
- Koneksi internet
- File `privatekey.txt` berisi private key (satu key per baris)

## ⚙️ Instalasi

1. Clone the Repository :
   ```bash
   git clone https://github.com/kazmight/Tea-Sepolia-Auto-TX.git
   cd Tea-Sepolia-Auto-TX

2. Install Python 3.10 :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install software-properties-common -y
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   sudo apt install python3.10 python3.10-venv python3.10-dev -y


3. Membuat Virtual Environment :
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate

4. Dependency Installation :
   ```bash
   pip install web3 python-dotenv
   pip install -r requirements.txt
 
5. Execution Script :
   ```bash
   Python3 Autotransaction.py
   or 
   Python Autotransaction.py

**Input Prompts:**

**Min Send Amount (e.g., 0.001)**

**Max Send Amount (e.g., 0.01)**

**Token Address (Paste Contract Addrres token yang udah kalian deploy)**

**Number of Transactions (e.g., 5)**
