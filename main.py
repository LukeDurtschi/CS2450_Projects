"""
CS 2450 - Project
"""

__author__ = "Kevin Bacon, Luke Durtschi, Matt Scott, Damian Sacks"
__version__ = "0.1.0"
__license__ = "MIT"


class Register:
    def __init__(self):
        self.value = 0

class Memory:
    def __init__(self, size = 100):
        self.size = size
        self.data = [None] * size
    
    def getMemoryLoc(self, loc):
       return self.data[loc]
    
    def updateMemory(self, loc, word):
       self.data[loc] = word

    def clearMemory(self):
       self.data = [0] * 100
    

class CPU:
    def __init__(self):
        #A register
        self.accumulator = Register()
        #A list where instructions are held
        self.memory = Memory()
        #Used to point where we are in the program
        self.pointer = 0
        #List of valid commands
        self.valid_commands = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        #Keeps the users instructions
        self.instructions = []

    def execute_READ(self, memory_location):
    # Read a word from the keyboard into a specific memory_location in memory
      return self.memory.getMemoryLoc(memory_location)

    def execute_WRITE(self, memory_location, word):
    # Write a word from a specific memory_location in memory to the screen changes
      return self.memory.updateMemory(memory_location, word)
        
    def load(self, memory_location):
        print('load')
    
    def store(self, memory_location):
        print('store')
    
    def add(self, memory_location):
        print('add')

    def subtract(self, memory_location):
        print('subtract')

    def divide(self, memory_location):
        print('divide')

    def multiply(self, memory_location):
       print('multiply')

    def get_code(self):
      '''Gets the user's code from the consol and stores it in the list instructions'''
      #Welcome message
      print("Welcome to UVSim! After each instruction, press enter.")
      print("Type Compile, when your program is complete: \n")

      #User input, BasicML code
      ui = ""

      #Loops to get the code from the user
      while ui != "compile".upper():
          ui = str(input()).upper()

          if ui.upper() != "COMPILE":
            self.instructions.append(ui)
    
    def compile(self):
      '''Processes the user's code and catches an error before running it
      Splits each line of the user's code into two, the command and memory location (command, location)
      Does input validation and turns the command and location into ints
      If the user's input is not valid, it will print an error message and the line the error is on (self.pointer)
      '''
      #Will be used to store instructions at a certain area in memory starting from 0
      memory_location = 0

      no_halt = True

      #Loops through the user's code and checks for errors
      for code in self.instructions:

          #Keeps track of the line number for error handling
          self.pointer += 1
          #Chooses which operation is performed
          command = code[:2]
          #Ensures that there is a valid int for choosing location in memory
          if code[2] != '0':
            location = code[2:]
          else:
            if len(code[2:]) == 2:
              location = code[3]

            else:
              print(f'Error on line {self.pointer}.')
              print('Memory location out of bounds.')
              exit()

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              print(f"Error on line {self.pointer}.")
              print('Expected a four digit int.')
              exit()

          if command not in self.valid_commands:
              print(f'Error on line {self.pointer}.')
              print('Invalid command.')
              exit()

          elif location <= 0 or location > 99:
              print(f'Error on line {self.pointer}.')
              print('Memory location out of bounds.')
              exit()

          else:
             #Code was valid and is added to a location in memory
             self.memory.data[memory_location] = code
             memory_location += 1

             #If a halt instruction is found, this part marks it as found 
             if command == 43:
                no_halt = False

      #Ensures that there is a halt instruction so the program doesn't run indefinitley 
      if no_halt == True:
         print('Error no halt instruction')
         exit()

    def process_code(self):

      '''
      Executes the program
      Still checks to make sure the instruction is valid in case the user 
      stores data at a location that previously held an instruction
      If code is valid, it will execute the appropriate function
      '''

      self.pointer = 0

      #Processes the code until a halt instruction is reached or a valid instruction is overwritten
      while True:
          
          code = self.memory.getMemoryLoc(self.pointer)
          
          if code == None:
             print('Error, branched to a location with no defined instruction.')
             exit()

          #Chooses which operation is performed
          command = code[:2]
          #Ensures that there is a valid int for choosing location in memory
          if code[2] != '0':
            location = code[2:]
          else:
            if len(code[2:]) == 2:
              location = code[3]

            else:
              print(f'Error on line {self.pointer}.')
              print('Data Overwriting')
              exit()

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              print(f"Error on line {self.pointer}.")
              print('Data Overwriting')
              exit()

          if command not in self.valid_commands:
              print(f'Error on line {self.pointer}.')
              print('Data Overwriting')
              exit()

          elif location <= 0 or location > 99:
              print(f'Error on line {self.pointer}.')
              print('Data Overwriting')
              exit()

          #Instruction at the location is valid and can be processed
          if command == 10:
            self.execute_READ(location)
            self.pointer += 1
        
          elif command == 11:
            self.execute_WRITE(location)
            self.pointer += 1
          
          elif command == 20:
            self.load(location)
            self.pointer += 1

          elif command == 21:
            self.store(location)
            self.pointer += 1

          elif command == 30:
            self.add(location)
            self.pointer += 1

          elif command == 31:
            self.subtract(location)
            self.pointer += 1

          elif command == 32:
            self.divide(location)
            self.pointer += 1

          elif command == 33:
            self.multiply(location)
            self.pointer += 1

          elif command == 40:
            #BRANCH
            self.pointer = location

          elif command == 41:
            #BRANCHNEG
            print('Branch Neg')

          elif command == 42:
            #BRANCHZERO
            print('Branch Zero')

          elif command == 43:
            #HALT
            exit()
def main():
    """ Main entry point of the app """
    
    #Creates the cpu object
    cpu = CPU()
    cpu.get_code()
    cpu.compile()
    cpu.process_code()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()