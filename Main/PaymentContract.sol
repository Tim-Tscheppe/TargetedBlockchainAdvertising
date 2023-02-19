// Solidity Implementation of Payment Execution Function
// @ Tim Tscheppe, Marquette University, 02-19-2023
// SPDX-License-Identifier: MIT

pragma solidity 0.6.9;

contract PaymentContract {

    address payable public sender;
    address payable public receiver;
    uint public amount;
    uint public funding;

    // Here is a couple random ETH addresses we can use tests:
    // 0x71C7656EC7ab88b098defB751B7401B5f6d8976F
    // 0x999999cf1046e68e36E1aA2E0E07105eDDD1f08E
    // 0xc0ffee254729296a45a3885639AC7E10F9d54979
    
    constructor(address payable _receiver,uint _amount) public payable {
        sender = msg.sender;
        receiver = _receiver;
        amount = _amount;
        funding = msg.value;
    }

    receive() external payable {
        funding += msg.value; 
    }

    function NewTransaction(address payable _receiver, uint _amount) public payable {
        funding = msg.value;
        receiver = _receiver;
        amount = _amount;
    }

    function GetBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function ExecutePayment() public payable {
        receiver.transfer(amount);
    }

}