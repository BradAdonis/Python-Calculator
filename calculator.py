from tkinter import *
import math

class CalculatorGUI(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        
        self.master.title("Calculator GUI")
        
        self.grid()
        self._strX = ""
        self._strY = ""
        self._Total = StringVar()
        self._Operation = ""
        self._OperationFound = False
        self._Calculate = False
        
        self._EntryLabel = Label(self, text = "Input")
        self._EntryLabel.grid(row = 0, column = 0)
        
        self._Entry = Entry(self, textvariable = self._Total)
        self._Entry.grid(row = 0, column = 1, columnspan = 2)
        
        self._7Button = Button(self, text="7", command = self._7Command, width=10)
        self._7Button.grid(row = 1, column = 0)
        
        self._8Button = Button(self, text="8", command = self._8Command, width=10)
        self._8Button.grid(row= 1, column = 1)
        
        self._9Button = Button(self, text="9", command = self._9Command, width=10)
        self._9Button.grid(row=1, column = 2)
        
        self._4Button = Button(self, text="4", command = self._4Command, width=10)
        self._4Button.grid(row=2, column = 0)
        
        self._5Button = Button(self, text="5", command = self._5Command, width=10)
        self._5Button.grid(row=2, column = 1)
        
        self._6Button = Button(self, text="6", command = self._6Command, width=10)
        self._6Button.grid(row=2, column=2)
        
        self._1Button = Button(self, text="1", command = self._1Command, width=10)
        self._1Button.grid(row=3, column=0)
        
        self._2Button = Button(self, text="2", command = self._2Command, width=10)
        self._2Button.grid(row=3, column=1)
        
        self._3Button = Button(self, text="3", command = self._3Command, width=10)
        self._3Button.grid(row=3, column=2)
        
        self._0Button = Button(self, text="0", command = self._0Command, width=10)
        self._0Button.grid(row=4, column=0)
        
        self._Plus = Button(self, text="+", command = self._PlusCommand, width=10)
        self._Plus.grid(row=1, column=3)
        
        self._Minus = Button(self, text="-", command = self._MinusCommand, width=10)
        self._Minus.grid(row=2, column=3)
        
        self._Multiply = Button(self, text="*", command = self._MultiplyCommand, width=10)
        self._Multiply.grid(row=3, column=3)
        
        self._Divide = Button(self, text="/", command = self._DivideCommand, width=10)
        self._Divide.grid(row=4, column=3)
    
        self._Cancel = Button(self, text="c", command = self._CancelCommand, width=10)
        self._Cancel.grid(row=0, column=3)
        
        self._Equals = Button(self, text="=", command = self._EqualsCommand, width=10)
        self._Equals.grid(row=4, column=2)
        
    def _CommandInput(self, Command):
        try:
            if Command == "+" or Command == "-" or Command == "*" or Command == "/":
                self._Operation = str(Command)
                self._OperationFound = True
            elif Command == "=":
                self._Calculate = True
                self._CalculateFunction()
            elif Command == "C":
                self._Total.set("")
                self._strX = ""
                self._strY = ""
                self._Operation = ""
                self._OperationFound = False
                self._Calculate = False
            else:
                if self._Calculate == False:
                    if self._OperationFound == True:
                        self._strY = self._strY + Command
                    elif self._OperationFound == False:
                        self._strX = self._strX + Command
                        
            try:
                if self._Calculate == False:
                    tempString = self._Total.get()
                    Command = tempString + Command            
                    self._Total.set(Command)
            except: 
                self._Total.set("")
            
        except ValueError:
            self._Total.set("ERR")
            self._CommandInput("C")
            
    def _CalculateFunction(self):
        calcValue = 0
        
        try:
            if self._Operation == "+":
                calcValue = int(self._strX) + int(self._strY)
            elif self._Operation == "-":
                calcValue = int(self._strX) - int(self._strY)
            elif self._Operation == "*":
                calcValue = int(self._strX) * int(self._strY)
            elif self._Operation == "/":
                calcValue = int(self._strX) / int(self._strY)
            self._Total.set(str(calcValue))    
        except ZeroDivisionError:
            self._Total.set("ERR")
        
    def _CancelCommand(self):
        self._CommandInput("C")
        
    def _EqualsCommand(self):
        self._CommandInput("=")
        
    def _7Command(self):
        self._CommandInput("7")
            
    def _8Command(self):
        self._CommandInput("8")
            
    def _9Command(self):
        self._CommandInput("9")
            
    def _4Command(self):
        self._CommandInput("4")
            
    def _5Command(self):
        self._CommandInput("5")
            
    def _6Command(self):
        self._CommandInput("6")
            
    def _1Command(self):
        self._CommandInput("1")
            
    def _2Command(self):
        self._CommandInput("2")
            
    def _3Command(self):
        self._CommandInput("3")
            
    def _0Command(self):
        self._CommandInput("0")
    
    def _PlusCommand(self):
        self._CommandInput("+")
            
    def _MinusCommand(self):
        self._CommandInput("-")
            
    def _MultiplyCommand(self):
        self._CommandInput("*")
            
    def _DivideCommand(self):
        self._CommandInput("/")
        
def main():
    CalculatorGUI().mainloop()     
    
main()
