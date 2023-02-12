/* This is how we will interface and deploy the "Simple Contract" file to the  blockchain */

var SimpleStorage = artifacts.require("SimpleStorage");

module.exports = function (deployer) {
  deployer.deploy(SimpleStorage);
};