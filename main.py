from solcx import compile_standard, install_solc
from web3 import Web3
import json
import os

install_solc("0.8.0")

#-----------Solidity Smart Contract-----------
with open("./VehicleRegistration.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"VehicleRegistration.sol": {"content": contract_source_code}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}},
    },
    solc_version="0.8.0",
)

abi = compiled_sol["contracts"]["VehicleRegistration.sol"]["VehicleRegistration"]["abi"]
bytecode = compiled_sol["contracts"]["VehicleRegistration.sol"]["VehicleRegistration"]["evm"]["bytecode"]["object"]
with open("VehicleRegistration_abi.json", "w") as f:
    json.dump(abi, f)
    
#------------------Connect to Ganache and Deploy-----------------------
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
account = w3.eth.accounts[0]

VehicleRegistration = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = VehicleRegistration.constructor().transact({"from": account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at: {tx_receipt.contractAddress}")

vehicle_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

tx_hash = vehicle_contract.functions.registerVehicle(
    "VIN67890", "Helen", "Tesla Model 3", 2021
).transact({"from": account})
w3.eth.wait_for_transaction_receipt(tx_hash)

vin_details = vehicle_contract.functions.getVehicle("VIN67890").call()
print(f"Vehicle Details: {vin_details}")
