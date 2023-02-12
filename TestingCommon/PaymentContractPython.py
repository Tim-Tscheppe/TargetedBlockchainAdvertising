# This program is a python implementation of the smart contract  we will be using to execute payments on the Ethereum blockchain.
# @ Tim Tscheppe, Marquette University, 02-12-2023

def ExecutePayment(amount, walletAddress):
    # let the values be called from outside function (Important in Solidity)
    publicAmount = int(amount)
    publicwalletAddress = str(walletAddress)

    # A constructor will go here in solidity, but not necessary for the black box approach
    print(publicAmount , " has been send to " , publicwalletAddress)

# Just a simple main for debug purposes
testAmount = input("Enter how much you'd like to send \n")
testAddress = input("Enter who you want to send it to \n")
ExecutePayment(testAmount, testAddress)