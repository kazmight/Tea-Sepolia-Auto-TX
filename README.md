Tea Sepolia Testnet

![Banner](https://img.shields.io/badge/Helper-EVM_Tea_Sepolia_Testnet-brightgreen)
![Version](https://img.shields.io/badge/Version-2.0-blue)
![License](https://img.shields.io/badge/License-MIT-orange)

Script otomatis untuk berinteraksi dengan jaringan EVM Tea Sepolia Testnet. Dibuat oleh **INVICTUS LABS**.

## 🌟 Fitur Utama

- 🚀 **Auto Send Native** - Mengirim aset native ke alamat acak di block explorer terakhir 
- 📜 **Auto Deploy Contract** - Melakukan deploy kontrak cerdas
- 🤖 **Auto Interaction Contract** - Berinteraksi dengan kontrak yang sudah terdeploy
- 💰 **Auto Send Token** - Mengirim token spesifik ke alamat acak block explorer terakhir
- 🎨 **Colorful Output** - Status transaksi dengan warna (hijau/kuning/merah)

## 🛠️ Persyaratan

- Python 3.8+
- Library Web3.py
- Koneksi internet
- File `privatekey.txt` berisi private key (satu key per baris)

## ⚙️ Instalasi


1. Install Python 3.10 :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install software-properties-common -y
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   sudo apt install python3.10 python3.10-venv python3.10-dev -y

2. Install Requirements :
   ```bash
   pip install requests
   pip install web3==6.20.1

3. Execution Script :
   ```bash
   python3 Autotransaction.py
   or 
   python Autotransaction.py

**Input Prompts:**

**Min Send Amount (e.g., 0.001)**

**Max Send Amount (e.g., 0.01)**

**Token Address (Paste Contract Addrres token yang udah kalian deploy)**

**privatekey.txt (isi dengan privatekey kalian)**

**How Many Run Transaction (Isi berapa jumlah tx yang ingin di jalankan)**

