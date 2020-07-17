import java.lang.Math;



public class Magic8 {
  public static void main(String[] args) {
    /*
    Parameters: String
    Description: Main method that prints a string to the user and uses the generateNumber() meethod.
                 Based on the number generated, it'll prints a response to the user.
    Return: None
    */
    System.out.print("Ask a question to the Magic 8-Ball: \n");



    int answer = generateNumber();
    String eightBall = "";
    switch (answer){
      case 0: eightBall = "It is certain";
      break;
      case 1: eightBall ="It is decidedly so";
      break;
      case 2: eightBall ="Reply hazy try again";
      break;
      case 3: eightBall ="Cannot predict now";
      break;
      case 4: eightBall ="Do not count on it";
      break;
      case 5: eightBall ="My sources say no";
      break;
      case 6: eightBall ="Outlook not so good";
      break;
      case 7: eightBall ="Signs point to yes";
      break;
    }
    System.out.println(eightBall);
  }

  public static int generateNumber(){
    /*
    Parameters: None
    Description: generates a random number between 0 and 8, exclusive
    Return: integer
    */
    int randomNumber = (int) (Math.random() * 8);
    return randomNumber;
  }
}

