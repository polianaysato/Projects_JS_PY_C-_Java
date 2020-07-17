let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

/*
Parameters: parameterless function 
Description: It is used by a callback function in the Event Listener at game.js script.
Return: integer 
*/
const generateTarget = () => {
  return Math.floor(Math.random() * 10);
}

/*
Parameters: integer humanGuess, integer computerGuess and integer secretNumber
Description: This method is used in the game.js script to define a winner.
Return: boolean
*/
const compareGuesses = (humanGuess, computerGuess, secretNumber) => {
  let a = Math.abs(humanGuess - secretNumber);
  let b = Math.abs(computerGuess - secretNumber);
  let c = a <= b? true : false;
  return c;
}

/*
Parameters: string winner
Description: It is used to set the variables humanScore and computerScore, based on the round's winner
Return: None
*/
const updateScore =(winner) => {

  switch(winner){
    case 'human': humanScore++;
    break;

    case 'computer': computerScore++;
    break;
  }
}

/*
Parameters: None
Description: It updates the current round number of the game
Return: integer
*/
const advanceRound = () => {
  return currentRoundNumber++;

}