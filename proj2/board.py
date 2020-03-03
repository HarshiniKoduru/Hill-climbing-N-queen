# -*- coding: utf-8 -*-
import random
import nqueen
iterations = 0
is_it_possible = True
randomRestarts = 0
restart_Strategy_steps = 0
passedboard = None

#Class for the Board
class board:
  #Intialize Method which will generate a random initial state
  def __init__(self, psize ,list=None ):
    if list == None:
      self.psize=psize
      self.board = [["." for i in range(0,psize)] for j in range(0,psize)]
      #initialize queens at random places
      for j in range(0,psize):
        rand_row = random.randint(0,psize-1)
        if self.board[rand_row][j] == ".":
          self.board[rand_row][j] = "Q"
      print("\nInitial State:")
      nqueen.nqueen.print_configuration(self,self.board, self.psize)
    

#Main Method which will call a proper hill climbing variant based on users input
if __name__ == "__main__":
  print ("\n**********Welcome to N Queen Solver*********\n")
  print ("Please select the size of the Puzzle to be solved: \nChoose \n\"1\" if you wish to solve default 8-queens puzzle, or \n\"2\" to assign your desired puzzle.")
  choice = int(input())
  if (choice == 1):
      psize = 8      
  elif (choice ==2):
      print ("\nPlease Enter the desired N size you wish to solve: ")
      psize = int(input())
  else:
      psize = 8
      print ("\nInvalid Choice")
      print ("\nTaking the default 8-queens puzzle\n")
  print ("\nPlease select number of Iterations to be made: \nChoose \n\"1\" Select if you want to solve the puzzle for 300 runs, or \n\"2\" Select if you want to assign your desired number of run interations. ")
  iterationChoice = int(input())
  if (iterationChoice == 1):
      iterations = 300
      
  elif (iterationChoice == 2):
      print ("\nPlease Enter the desired number of runs: ")
      iterations = int(input())
  else:
      iterations = 300 
      print ("\nInvalid Choice")
      print ("\nTaking the default value of 300 iterations \n")
  print ("\nSelect any one of the Search Strategy: \nChoose \n\"1\" Steepest Ascent Hill Climbing, or \n\"2\" Hill Climbing with Sideways Move, or \n\"3\" Random-Restart Hill Climbing without Sidemove,or \n\"4\" Random-Restart Hill Climbing with Sidemove")
  searchStrategy = int(input())
  if (searchStrategy == 1):
      search_type = 1      
  elif (searchStrategy == 2):      
      search_type = 2
  elif (searchStrategy == 3):      
      search_type = 3   
  elif (searchStrategy == 4):
      search_type = 4
  else:
      search_type = 1
      print ("\nInvalid Choice")
      print ("\nRunning the default approach - Steepest Ascent Hill Climbing\n")
 
  queen_board = nqueen.nqueen(search_type, psize, iterations, is_it_possible)
  queen_board.print_results(search_type)