// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VehicleRegistration {
    struct Vehicle {
        string vin;
        string owner;
        string model;
        uint256 year;
    }

    mapping(string => Vehicle) public vehicles;

    event VehicleRegistered(string vin, string owner, string model, uint256 year);

    function registerVehicle(string memory _vin, string memory _owner, string memory _model, uint256 _year) public {
        require(bytes(vehicles[_vin].vin).length == 0, "Vehicle already registered.");
        vehicles[_vin] = Vehicle(_vin, _owner, _model, _year);
        emit VehicleRegistered(_vin, _owner, _model, _year);
    }

    function getVehicle(string memory _vin) public view returns (string memory, string memory, string memory, uint256) {
        Vehicle memory v = vehicles[_vin];
        require(bytes(v.vin).length != 0, "Vehicle not found.");
        return (v.vin, v.owner, v.model, v.year);
    }
}
