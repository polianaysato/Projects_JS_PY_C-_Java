using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string pressed_key, out int x_change, out int y_change){
      //Parameters: string pressed_key, out integer x_change and out integer y_change
      //Description: This method is used in the Program.cs script for updating the x and y coordinates of the carachter's position
      //Return: None
      x_change = 0;
      y_change = 0;
      switch(pressed_key){
        case "LeftArrow":
          x_change -= 1;
          break;
        case "RightArrow":
          x_change += 1;
          break;
        case "UpArrow":
          y_change -= 1;
          break;
        case "DownArrow":
          y_change += 1;
          break;
      }
    }

    public new static char UpdateCursor(string pressed_key){
      //Parameters: string pressed_key
      //Description: This method is used in the Program.cs script for updating the character's symbol
      //Return: char character
      switch(pressed_key){
        case "LeftArrow":
          return '<';
          break;
        case "RightArrow":
          return '>';
          break;
        case "UpArrow":
          return '^';
          break;
        case "DownArrow":
          return 'v';
          break;
        default:
          return '<';
      }
    }

    public new static int KeepInBounds(int coordinate, int max_value){
      //Parameters: integer coordinate and out integer max_value
      //Description: This method is used in the Program.cs script for keeping the character between the screen bounds.
      //Return: integer coordinate
      if (coordinate < 0){
        return 0;
      }
      else if (coordinate >= max_value){
        return max_value - 1;
      }
      else
      {
        return coordinate;
      }
    }

    public new static bool DidScore(int x_character, int y_character, int x_fruit, int y_fruit){
      //Parameters: integer x_character, integer y_character, integer x_fruit and integer y_fruit
      //Description: This method is used in the Program.cs script for updating the user's score
      //Return: boolean
      if (x_character == x_fruit && y_character == y_fruit){
        return true;
      }
      else
      {
        return false;
      }

    }
}
}