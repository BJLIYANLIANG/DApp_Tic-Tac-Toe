# DApp Game Demonstration

Simple demonstration of a decentralized game using Node.JS, Truffle, and Solidity. e.g., A classic card game where you compare numerical data of cars. https://en.wikipedia.org/wiki/Top_Trumps

## Live demo ##
* Use MetaMask connection to Ropsten 
* Open [Live Demo](https://kilkki80.000webhostapp.com/)

### This is a DApp version of the game ###
Gameplay
 1. Player registers as a player
 2. 3 cards are given for every player in registration
 3. Player can see other players and how many cards they have
 4. Player can play againts a player by choosin "play with" button after player's name
 5. Player chooses a value from his card to compete againts opponents card. By choosing "play" button.
 6. After this result of the game round is show to the player
 7. Winner gets the card of the loser

### Dependencies ###

* [Installing NodeJS](https://nodejs.org/en/download/)
* [Installing Truffle](https://github.com/trufflesuite/truffle)
* [Installing Solidity](https://solidity.readthedocs.io/en/develop/installing-solidity.html)
* [Installing Canache-cli](https://github.com/trufflesuite/ganache-cli) (unless you utilize one of the testnets')
* [Installing Yarn](https://yarnpkg.com/lang/en/docs/install/)

BONUS FOR EXPERIMENTAL FEATURES

* [Installing IPFS](https://ipfs.io/docs/install/)
* [Installing Whisper](https://github.com/ethereum/go-ethereum/wiki/Whisper)
* [Installing Vyper](https://github.com/ethereum/go-ethereum/wiki/Whisper)

### Installing DApp ###
1. Clone repo with the following command into your directory of choice, `git clone https://github.com/matthew-mcateer/decentralized_game_demo.git`
2. Install MetaMask for your browser
3. Run `npm install`
4. Start rpc or ganache. (Change the network address accordingly in truffle.js)
5. Compile and migrate contract `truffle compile && truffle migrate`
6. Run `npm run dev`
7. Open browser to localhost if previous command didn't automatically

### Completed ###
* Solidity contract created (All major logic for game creation, user turn submission, and win-conditions).

### Todo ###
* Use frontend framework like angular
* Clean up code
* Add error checks to frontend


* HTML front-end. - HTML layout complete. Needs logic to connect HTML to the solidity contract.
	* Need to link wallet address to http-session
	* Need to collect game-state from blockchain and fill-in tile variables.
	* Need to add contract function execution via html buttons.

* Add Whisper Chat based on [this](https://github.com/rodocite/decentralized-react-chat)
* Add IPFS Functionality based on [this](https://www.youtube.com/watch?v=Nv_Teb--1zg&t=3s)
* Reimplement contracts using the experimental [Vyper Programming Language](https://github.com/ethereum/go-ethereum/wiki/Whisper)

### Known Issues ###
`Unhandled rejection Error: Couldn't decode bool from ABI: 0x`
	means you forgot to deploy the contract, prob set remix to Javascript VM


#### Special Thanks ###
* https://github.com/Theschool-ai/Game-AppleEater
* https://github.com/marrer99/StopitGame

* https://github.com/san-lee-ai/simple_auction
* https://github.com/kilkki/top-trumps-dapp
* https://github.com/whvod/EthDoubleOrNothing
* https://github.com/llSourcell/simple_auction
* https://github.com/ro6/ethereum-heroes-hackathon_tic-tac-toe

(and for all the [tic tac toe variants](https://github.com/search?l=JavaScript&q=ethereum+tic+tac+toe&type=Repositories) that helped me understand the full extent of the important parts)

* https://github.com/NodeFactoryIo/ethereum-workshop & https://github.com/NodeFactoryIo/ethereum-workshop-contract
* https://github.com/DotBowder/TicTacToe-DAPP
* https://github.com/cag/eth-tictactoe
* https://github.com/lserafin/Tic-tac-toe
* https://github.com/emilianobilli/tictactoe
* https://github.com/timohe/ethTicTacToe
* https://github.com/ro6/ethereum-heroes-hackathon_tic-tac-toe

(and of course, the example of using state-channels in IPFS)
* https://github.com/AleBuser/TicTacToe-ipfs

## Original Prompt ##

The technology stack:

- Node.JS
- Truffle
- Solidity
- Canache-cli (unless you utilize one of the testnets')
- Bonus points if technology is utilized
    - IPFS
    - Whisper
        - Bonus if deployed on the public internet for the rest of the class.

- Recommend utilizing free credits from DigitalOcean or Google Cloud Compute(GCP)

- No bonus, but shout out if the Viper programming language is used.

Please post your code to GitHub. Then email (schoolofaigrading@gmail.com) a link to the GitHub repo with any additional information to run the game. Please include an overview of the game, any important rules for the game. If the game is not completely operational, please describe what was the blocker you encountered. Please also describe any issues you encountered along the development path and what steps you took to overcome the issue(s).

If you need help along the way, please reach out to the instructors via email (dapps@sirajraval.com). Please include a full description of what you are building, issues and GitHub link to your current code.

Please feel free to collaborate and work with other classmates and build an amazing game. When submitting, please include a note of everyone that worked on the project. 

Looking for classmates to team up with? Use this form https://docs.google.com/spreadsheets/d/1_WrorNrFjmb6dEFzr7tB0gkHgxTVzak_OWupeqgp7js/

Please submit your project by end of day 4/21/2018.

Thanks!

Kind Regards,

TheSchool.AI

##### GAME IDEAS
The midterm assignment is to build a Dapp game using the technologies we have learned about of the past couple of weeks.

##### Game one:
Simple single player mind math addition game where the user is presented with two randomly generated numbers. 

The user is to add these numbers together in their mind. The user's score will increase for each successful answer. 

Tech Stack

The game will use node.js and also will be using local private development blockchain for storing the score.

##### Game two:
Building upon the last game, with two adjustments, at the end of the week the overall score will reset, and the ability to spend the score points as an additional bonus challenge. This type of reset can be useful in similar old 1990’s style games where the user’s stash of virtual coins would reset at the end of the week. Before the reset, the user can purchase virtual goods such as player upgrades like a Star or Unicore emoji. 

##### Game three:
Game three is a simple web-application game, using a local private development blockchain again for the data store. In this game, we will utilize a web-game application development tool, which will perform a simple callback into our node.js server, which performs the writing to the blockchain. The game concept is to have your game character run around on the screen, controlling the user direction with your directional arrow keys, and the game character will eat apples. For each apple the character eats, the web application will perform an outbound callback to the node.js server, which will update the user score on the blockchain.
