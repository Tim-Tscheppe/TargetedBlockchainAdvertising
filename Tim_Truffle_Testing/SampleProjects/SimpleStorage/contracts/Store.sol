pragma solidity ^0.8.10;

// The contract is kind of like a class
contract SimpleStorage {
  uint myVariable;

  function set(uint x) public {
    // This is the variable that gets stored
    myVariable = x;
  }

  function get() view public returns (uint) {
    // This is how we can call the variable, note we have to use "view" rather than "constant"
    return myVariable;
  }
}