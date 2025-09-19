# Vehicle Registration on Blockchain

Developed a decentralised vehicle registration system using Solidity smart contracts to store vehicle data on the Ethereum blockchain. Integrated web3.py for Python-based interaction, enabling contract deployment, vehicle registration, and data retrieval. The system ensures tamper-proof records and transparent management of vehicle information.

**Key Features:**
* Register vehicles using VIN (Vehicle Identification Number).
* Store and retrieve vehicle details (owner, model, year) on the blockchain.
* Event logging when a vehicle is registered.
* Python script to compile, deploy, and interact with the contract.
* Works with Ganache (local blockchain) or can be extended to Ethereum testnets (Sepolia/Goerli).

**Installation:**

1. Clone the repository:
```
gh repo clone Prinaka/Vehicle-Registration-on-Blockchain
cd Vehicle-Registration-on-Blockchain
```

2. Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Start Ganache:
* Open Ganache and start a workspace.
* Check RPC server (usually http://127.0.0.1:7545 or 8545).

**Usage:**

Run the script:
```
python main.py
```

**Customization & Extending:**

* Ownership Transfer – Add a function to transfer ownership of a registered vehicle from one person to another.
* Vehicle History Tracking – Keep a log of past owners and modifications, making the system auditable.
* Document Hash Verification – Store document hashes (RC, insurance, pollution certificates) on-chain for authenticity.
* Frontend Integration – Build a simple React or Streamlit UI to register and look up vehicles.
* Public Testnet Deployment – Deploy the contract on Ethereum testnets (Sepolia/Goerli) instead of just Ganache for a real blockchain experience.
* Role-Based Access – Add roles (e.g., RTO/Government authority) to restrict who can register vehicles.
* Search & Filtering – Extend the contract with helper functions (e.g., get all vehicles owned by a person).
* Integration with IPFS – Store large vehicle-related documents (e.g., insurance scans) off-chain in IPFS, while keeping only hashes on-chain.
  
**License:**

This project is licensed under the MIT License – see the LICENSE file for details.
