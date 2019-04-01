"""
Program: magic8ball.py
Author: James Jutt
Date: 4/1/19

Magic 8-Ball program that will output the users question and a random response
"""

from breezypythongui import EasyFrame
from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
import random
import sys

class Magic8Ball(EasyFrame):
    """Displays output after user inputs a question and clicks the button"""
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Lottery Number Generator", background = "black", resizable = False)
        myFont = Font(family = "fixedsys", size = 23, slant = "italic")

        # Label to push photo image into "image" argument
        self.myImage = self.addLabel(text = "", row = 3, column = 1, columnspan = 10, background = "black", sticky = "NSEW")
        
        # Stores the images in variables for later use
        self.imageInitial = ImageTk.PhotoImage(Image.open("images/magic8ball.jpg"))
        self.imageAfter = ImageTk.PhotoImage(Image.open("images/qmark.jpg"))

        # Sets the image to myImage
        self.myImage["image"] = self.imageInitial

        # Main questionLabel and questionInput to take in the users question
        self.questionLabel = self.addLabel(text = "What do you want to ask this magic 8-ball?", row = 4, column = 1, columnspan = 6, background = "black", font = myFont, foreground = "darkviolet", sticky = "NSEW")
        self.questionInput = self.addTextField(text = "", row = 5, column = 1, columnspan = 6, sticky = "NSEW")

        # Command buttons, one to ask submit the question (askBtn) and one to quit the program (quitBtn)
        self.askBtn = self.addButton(text = "        Ask the Magic 8 Ball         ", row = 6, column = 0, columnspan = 3, command = self.answer)
        self.quitBtn = self.addButton(text = "                      Quit                    ", row = 6, column = 3, columnspan = 6, command = self.quit)
    
    # Event handler to output users question and response
    def answer(self):
        # Second Font object needed because of "scope"
        myFont = Font(family = "fixedsys", size = 20, slant = "italic")

        # Label to output the users question
        self.userQuestion = self.addLabel(text = "", row = 0, column = 1, columnspan = 6, background = "black", foreground = "darkviolet", font = myFont, sticky = "NSEW")

        # Line break to seperate output
        self.outputLine = self.addLabel(text = "---------------------------------------------------------", row = 1, column = 1, columnspan = 6, background = "black", foreground = "darkviolet", font = myFont, sticky = "NSEW")

        # Label to output the random response from outputArray
        self.questionOutput = self.addLabel(text = "", row = 2, column = 1, columnspan = 6, background = "black", foreground = "darkviolet", font = myFont, sticky = "NSEW")

        # Stores the input from self.questionInput for conditionals
        getInput = self.questionInput.getText()

        # Some validation to check if users response is an empty string or starts with a number
        if getInput == "" or getInput.startswith("0") == True or getInput.startswith("1") == True or getInput.startswith("2") == True or getInput.startswith("3") == True or getInput.startswith("4") == True or getInput.startswith("5") == True or getInput.startswith("6") == True or getInput.startswith("7") == True or getInput.startswith("8") == True or getInput.startswith("9") == True:
            # Update questionOutput "text" when user enters an invalid question
            self.userQuestion["text"] = f"You asked the Magic 8-ball an invalid question"
            self.questionOutput["text"] = f"The Magic 8-ball replies:  How dare you try to trick me "

            # Prompts user to enter a valid question
            self.questionLabel["text"] = "        Ask me real question!         "

            # Changes foregrounds to red if user enters an invalid response
            self.userQuestion["foreground"] = "red"
            self.questionOutput["foreground"] = "red"
            self.outputLine["foreground"] = "red"
            self.questionLabel["foreground"] = "red"

            # Change image when if condition is True
            self.myImage["image"] = self.imageAfter

        else:
            # Sets the button "text" back to its normal state
            self.askBtn["text"] = "        Ask the Magic 8 Ball         "

            # Sets the image back if user enters an valid input
            self.myImage["image"] = self.imageInitial

            # Array of all the possible outputs
            outputArray = ["My sources say no.", "Cannot predict now.", "Most likely.", "Outlook not so good.", "As I see it, yes.", "Ask again later.", "Concentrate and ask again.",
                            "It is certain.", "Signs point to yes.", "Better not tell you now.", "You may rely on it."]

            # Stores a random number between 0 and length of outputArray
            myNum = random.randint(0, len(outputArray) - 1)

            # Initialize ranResponse with a random index number from myNum variable
            ranResponse = outputArray[myNum]

            # Push output if all conditions are True
            self.questionLabel["text"] = "Ask the Magic 8-ball another question \nor press quit to exit the program"
            self.userQuestion["text"] = f"You asked the Magic 8-ball: \n{getInput}"
            self.questionOutput["text"] = f"The Magic 8-ball replies:  \n{ranResponse}"

            # Change foregrounds to "green" if user enters an valid question
            self.userQuestion["foreground"] = "green"
            self.questionOutput["foreground"] = "green"
            self.outputLine["foreground"] = "green"
            self.questionLabel["foreground"] = "green"

    # Event handler if user clicks the "quit" button
    def quit(self):
        sys.exit(0)

def main():
    Magic8Ball().mainloop()

if __name__ == "__main__":
    main()