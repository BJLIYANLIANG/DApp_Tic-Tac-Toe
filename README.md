# DApp Tic-Tac-Toe

Simple demonstration of a decentralized game using Node.JS, Truffle, and Solidity. This is the classic strategy game that's easy to learn, but tough to win (https://en.wikipedia.org/wiki/Tic-tac-toe, hopefully you shouldn't need to look at the Wikipedia article for this one). This demo also includes options for bidding on games and placing aribitrary amounts of ETH.

## Live demo ##
* Use MetaMask connection to either the Ropsten testnet,  
* Open the Live Demo (http://34.197.89.246:2200/). In the event that the link does not work, you can follow the instructions below and run your own version of the demo locally.

### This is a DApp version of the game ###
Gameplay
 1. Once the User
 2. Player 1 marks cells with crosses, player 2 marks with circles
 3. Players move one at a time and cannot place their marks in the same cells at the same time
 4. If one Player places 3 marks of theirs in a row, either vertically, horizontally, or diagonally, they are declared the Winner
 5. Winner gets bid placed by the loser
 6. Players then have option to create another new game or join an existing one

### Pre-installation Dependencies ###

* [Installing NodeJS](https://nodejs.org/en/download/)
* [Installing Truffle](https://github.com/trufflesuite/truffle)
* [Installing Solidity](https://solidity.readthedocs.io/en/develop/installing-solidity.html)
* [Installing Canache-cli](https://github.com/trufflesuite/ganache-cli) (unless you utilize one of the testnets')
* [Installing Yarn](https://yarnpkg.com/lang/en/docs/install/)

BONUS FOR EXPERIMENTAL FEATURES

* [Installing IPFS](https://ipfs.io/docs/install/)
* [Installing Whisper](https://github.com/ethereum/go-ethereum/wiki/Whisper)
* [Installing Vyper](https://vyper.readthedocs.io/en/latest/installing-vyper.html)

### Installing the DApp ###
1. Clone repo with the following command into your directory of choice, `git clone https://github.com/matthew-mcateer/decentralized_game_demo.git`
2. Install MetaMask for your browser, and set up your user account
3. Run `npm install `
4. Start rpc or ganache. (Change the network address accordingly in truffle.js)
5. Compile and migrate contract `truffle compile && truffle migrate`
6. Run `npm run dev`
7. Open browser to `localhost:8545` if previous command didn't automatically work

### Completed ###
* Stylish Front-end design for game created
* Main responsive javascript app, app.js, created for running the game
* Solidity contract created containing logic and rules of the game
* Added contract execution capabilities within HTML for page
* Game successfully tested on local testnet
* Dependency Tracking set up with yarn

### Next Steps ###
* Refine Front-end additionally using Angular and/or React
* Either Creating more permenant web app or further decentralization of back-end
* Add Whisper Chat functionality based on [this](https://github.com/rodocite/decentralized-react-chat).
* Add IPFS Functionality based on [this](https://www.youtube.com/watch?v=Nv_Teb--1zg&t=3s). Some local files for the game were uploaded to the IPFS successfully, but a dedicated IPFS daemon needs to be created and maintain, or the hashed become invalid within 24-hours.
* Reimplement contracts using the experimental [Vyper Programming Language](https://github.com/ethereum/go-ethereum/wiki/Whisper). This has been partially successful, but further testing and debugging is required
* Increasing room for additional game rooms
* Containerization using Docker

### Known Issues ###
`errr` error in MetaMask
	Unknown, Ethereum test network is possibly overloaded

`Unhandled rejection Error: Couldn't decode bool from ABI: 0x`
	Contract likely wasn't deployed correctly

##### Submitting additional Issues
Additional new issued can be submitted to the [issues page for this repo](https://github.com/matthew-mcateer/DApp_Tic-Tac-Toe/issues).

#### 3rd-Party Resources & Special Thanks ####
This project was made possible by the existence of multiple resources for Ethereum Game Development, which served as eithr direct tutorials or indirect guides. Some of the resources that were looked at over the course of this project include but were not limited to.

The Resources of The School of AI and Siraj Raval
* https://github.com/llSourcell/Decentralized_Games
* 
* https://github.com/Theschool-ai/Game-AppleEater
* https://github.com/marrer99/StopitGame
* https://github.com/llSourcell/simple_auction

Useful Documentation and Articles
* https://hackernoon.com/getting-started-as-an-ethereum-web-developer-9a2a4ab47baf
* https://blog.zeppelin.solutions/a-gentle-introduction-to-ethereum-programming-part-1-783cc7796094
* https://medium.com/@merunasgrincalaitis/ultimate-guide-to-convert-a-web-app-to-a-decentralized-app-dapp-f6112a079509
* https://hackernoon.com/ethereum-development-walkthrough-part-2-truffle-ganache-geth-and-mist-8d6320e1226
* https://medium.com/@mvmurthy/full-stack-hello-world-voting-ethereum-dapp-tutorial-part-1-40d2d0d807c2
* https://nodejs.org/en/download/
* https://github.com/trufflesuite/truffle
* https://solidity.readthedocs.io/en/develop/installing-solidity.html
* https://github.com/trufflesuite/ganache-cli
* https://yarnpkg.com/lang/en/docs/install/
* https://ipfs.io/docs/install/
* https://github.com/ethereum/go-ethereum/wiki/Whisper
* https://vyper.readthedocs.io/en/latest/installing-vyper.html
* https://github.com/TechBookHunter/Free-Blockchain-Books/blob/master/book/Introducing%20Ethereum%20and%20Solidity%20-%20Foundations%20of%20Cryptocurrency%20and%20Blockchain%20Programming%20for%20Beginners.pdf 
* https://media.readthedocs.org/pdf/solidity/develop/solidity.pdf
* https://ethereumbuilders.gitbooks.io/guide/content/en/solidity_tutorials.html
* https://consensys.github.io/smart-contract-best-practices/known_attacks/
* https://ethereumbuilders.gitbooks.io/guide/content/en/solidity_tutorials.html

3rd Party JavaScript Tic Tac Toe Games

https://github.com/richleland/Tic-Tac-Toe
https://github.com/rolling-scopes-school/tic-tac-toe
https://github.com/jwngr/tic-tac-tic-tac-toe
https://github.com/sf-wdi-gaia/tic-tac-toe

3rd Party Solidity Ethereum DApps & Smart Contracts

* https://medium.com/cryptolinks/ethereum-smart-contract-development-610718d0629
* https://github.com/kilkki/top-trumps-dapp
* https://github.com/whvod/EthDoubleOrNothing
* https://github.com/ro6/ethereum-heroes-hackathon_tic-tac-toe
* https://github.com/NodeFactoryIo/ethereum-workshop & https://github.com/NodeFactoryIo/ethereum-workshop-contract
* https://github.com/lserafin/Tic-tac-toe
* https://github.com/ro6/ethereum-heroes-hackathon_tic-tac-toe

3rd Party IPFS Game Examples
* https://github.com/AleBuser/TicTacToe-ipfs
