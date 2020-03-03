import random,copy
from board import board
iterations = 0
passedboard = None
randomRestarts = 0
restart_Strategy_steps = 0

#Class for the NQueen
class nqueen:   
  #Intialize Method
  def __init__(self, search_type, psize, iterations, is_it_possible):
    #Initializing the required variables and counters
    self.totalruns = iterations
    self.totalsucc = 0
    self.totalfail = 0
    self.stepforsucc = 0
    self.stepforfail = 0
    self.sidemove = 0
    self.psize = psize    
    self.is_it_possible = is_it_possible
    for i in range(0,iterations):
      if self.is_it_possible == True:
        print ("\n============================")
        print ("OUTPUT FOR RUN:",i+1)
        print ("============================")
      self.queen_board = board(psize,passedboard)
      self.cost = self.calculate_attack_pairs(self.queen_board,self.psize)
      #Call for each type of search climbing algorithm
      if (search_type == 1):
          self.hill_Climbing()
      elif (search_type == 2):
          self.sideways_Move()
      elif (search_type == 3):
          self.random_Restart_without_sidemove()
      elif (search_type == 4):
          self.random_Restart_with_sidemove()
 
  #Printing the configuration of the N-Queen Puzzle 
  def print_configuration(self,state,psize):
      for l in range(0,psize):
          for m in range(0,psize):
              if m < psize-1:
                  print(state[l][m], end=" ")
              elif(m == psize-1):
                  print(state[l][m], end="\n")    
 


  #Definition for the Steepest hill climbing Algorithm
  def hill_Climbing(self):
    totalnumsteps = 0
    while 1:
      current_attacks = self.cost
      #Breaking if the random initial state itself is a sucess state
      if self.cost == 0:
          break
      #Call to generare the lower cost sucessesor
      self.calc_leastcost(self.psize)
      if (current_attacks == self.cost):
        self.totalfail += 1
        self.stepforfail += totalnumsteps
        if totalnumsteps == 0:
            self.stepforfail += 1
        break
      totalnumsteps += 1
      if self.is_it_possible == True:
        print ("\nTotal number of attack pairs:", (int)(self.calculate_attack_pairs(self.queen_board,self.psize)))
        self.print_configuration(self.queen_board.board,self.psize)
      if (self.cost == 0):
          break
    # If Failure is encountered
    if self.cost != 0:
      if self.is_it_possible == True:
        print ("\n*****NO SOLUTION FOUND*****")
    # If Sucess is encountered
    else:
      if self.is_it_possible == True:
        print ("\n*****SOLUTION FOUND*****")
      self.totalsucc += 1
      self.stepforsucc += totalnumsteps
    return self.cost

  #Definition for the Sideways hill climbing Algorithm
  def sideways_Move(self):
    totalnumsteps = 0
    sidemove = 0
    while 1:
      current_attacks = self.cost
      current_board = self.queen_board
      #Breaking if the random initial state itself is a sucess state
      if self.cost == 0:
          break
      #Call to generare the sucessesor board
      #This can return both equal heuristic board or lower heuristic board
      self.calc_hueristic(self.psize)
      if current_board == self.queen_board:
          self.stepforfail += totalnumsteps
          self.totalfail += 1
          if totalnumsteps == 0:
            self.stepforfail += 1
          break
      if current_attacks == self.cost:
        sidemove += 1
        if sidemove == 100:
            self.stepforfail += totalnumsteps
            self.totalfail += 1
            break
      elif(current_attacks > self.cost):
          sidemove = 0
      totalnumsteps += 1
      if self.is_it_possible == True:
        print ("\nTotal number of attack pairs:", (int)(self.calculate_attack_pairs(self.queen_board,self.psize)))
        self.print_configuration(self.queen_board.board,self.psize)
      if self.cost == 0:
        break
    if self.cost != 0:
      if self.is_it_possible == True:
        print ("\n*****NO SOLUTION FOUND*****")
    else:
      if self.is_it_possible == True:
        print ("\n*****SOLUTION FOUND*****")
      #Incrementing the count for number of success incurred and total steps taken for each successful iteration
      self.totalsucc += 1
      self.stepforsucc += totalnumsteps
    return self.cost

  #Definition for the Random Restart without sideways allowing  hill climbing Algorithm  
  def random_Restart_without_sidemove(self): 
      while 1:        
        current_attacks = self.cost
        current_board = self.queen_board
        #Breaking if the random initial state itself is a sucess state
        if self.cost == 0:
            break
        #Call to generare the sucessesor board
        self.calc_leastcost(self.psize)
        #Check and logic for random Restart
        if (current_board == self.queen_board) or ((current_attacks == self.cost) & (self.cost != 0)):
          self.queen_board = board(self.psize,passedboard)
          global randomRestarts
          #Increment the Random Restarts counter
          randomRestarts += 1 
          self.cost = self.calculate_attack_pairs(self.queen_board,self.psize)               
        elif (self.cost < current_attacks):  
            if self.is_it_possible == True:
                print ("\nTotal Number of attack pairs:", (int)(self.calculate_attack_pairs(self.queen_board,self.psize)))
                self.print_configuration(self.queen_board.board,self.psize)
        global restart_Strategy_steps
        #Increment the Steps counter in Random restart Hill climbing algorithm
        restart_Strategy_steps += 1 
        if self.cost == 0:
          break     
      if self.is_it_possible == True:
          print ("\n*****SOLUTION FOUND*****")
           #Incrementing the count for number of success incurred
      self.totalsucc += 1     
      return self.cost
  
  #Definition for the Random Restart with sideways allow hill climbing Algorithm  
  def random_Restart_with_sidemove(self):
      sidemove = 0
      while 1:        
        current_attacks = self.cost
        current_board = self.queen_board
        #Breaking if the random initial state itself is a sucess state
        if self.cost == 0:
            break
        #Call to generare the sucessesor board
        self.calc_hueristic(self.psize)
        #Check and logic for random Restart
        if current_board == self.queen_board:
          self.queen_board = board(self.psize,passedboard)
          global randomRestarts
          #Increment the Random Restarts counter
          randomRestarts += 1 
          self.cost = self.calculate_attack_pairs(self.queen_board,self.psize) 
        if current_attacks == self.cost:
          sidemove += 1
          if sidemove == 100:
            self.queen_board = board(self.psize,passedboard)
            #Increment the Random Restarts counter
            randomRestarts += 1 
            self.cost = self.calculate_attack_pairs(self.queen_board,self.psize)
        elif(current_attacks > self.cost):
          sidemove = 0
        global restart_Strategy_steps
        #Increment the Steps counter in Random restart Hill climbing algorithm
        restart_Strategy_steps += 1    
        if self.is_it_possible == True:
          print ("\nTotal number of attack pairs:", (int)(self.calculate_attack_pairs(self.queen_board,self.psize)))
          self.print_configuration(self.queen_board.board,self.psize)
        if self.cost == 0:
          break     
      if self.is_it_possible == True:
          print ("\n*****SOLUTION FOUND*****")
           #Incrementing the count for number of success incurred
      self.totalsucc += 1     
      return self.cost
 
  #Print Definition exclsive to each type of Hill climbing algorithm
  def print_results(self,search_type):
    print ("\nTotal Runs: ", self.totalruns)
    print ("Total Success: ", self.totalsucc)
    print ("Success Percentage: ", (float(self.totalsucc)/float(self.totalruns))*100,"%")
    
    #Print statements for Steepest Hill climbing Algorithm 
    # & Sideways Hill climbing Algorithm
    if(search_type == 1) or (search_type == 2):
        print ("Total Fail: ", self.totalfail)
        print ("Fail Percentage: ", (float(self.totalfail)/float(self.totalruns))*100,"%")
        if(self.totalsucc >= 1):
          print ("Average number of steps in success: ", float(self.stepforsucc)/float(self.totalsucc))
          print ("Total Steps for Success: ", self.stepforsucc)
        if(self.totalfail >= 1):
          print ("Total Steps for Fail: ", self.stepforfail)
          print ("Average number of steps in fail: ", float(self.stepforfail)/float(self.totalfail))
          
    #Print statements for Random Restart Hill climbing Algorithm
    if(search_type == 3) or (search_type == 4):
        print ("Number of random restarts:", randomRestarts)
        print ("Average number of random restarts: ", float(randomRestarts)/float(self.totalruns))
        print ("Average number of steps: ", float(restart_Strategy_steps)/float(self.totalruns));
    
  #Definition for calculating the number of attack pairs     
  def calculate_attack_pairs(self, puz_board, psize):

    #these are separate for easier debugging
    straight_attacks = 0
    diagonal_attacks = 0
    for i in range(0,psize):
      for j in range(0,psize):
        #if this node is a queen, calculate all attacks pairs
        if puz_board.board[i][j] == "Q":
          #We will subtract the total cost by 2 so that we don't count the self state
          straight_attacks -= 2
          for k in range(0,psize):
            if puz_board.board[i][k] == "Q":
              straight_attacks += 1
            if puz_board.board[k][j] == "Q":
              straight_attacks += 1
          #calculation of all diagonal attacks
          k, l = i+1, j+1
          while k < psize and l < psize:
            if puz_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k +=1
            l +=1
          k, l = i+1, j-1
          while k < psize and l >= 0:
            if puz_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k +=1
            l -=1
          k, l = i-1, j+1
          while k >= 0 and l < psize:
            if puz_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k -=1
            l +=1
          k, l = i-1, j-1
          while k >= 0 and l >= 0:
            if puz_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k -=1
            l -=1
    return ((diagonal_attacks + straight_attacks)/2)
 
  #This function tries moving every queen to every spot, with only one move
  #and returns the move that has the least number of attacks pairs
  def calc_leastcost(self,psize):
    least_cost = self.calculate_attack_pairs(self.queen_board, self.psize)
    desirable_cost = self.queen_board
    #We move one queen at a time
    for q_col in range(0,psize):
      for q_row in range(0,psize):
        if self.queen_board.board[q_row][q_col] == "Q":
          #We get the lowest cost configuration by moving each queen in its respective column
          for m_row in range(0,psize):
              if self.queen_board.board[m_row][q_col] != "Q":
                #Queen is placed in empty slot of each column
                temporary_board = copy.deepcopy(self.queen_board)
                temporary_board.board[q_row][q_col] = "."
                temporary_board.board[m_row][q_col] = "Q"
                temporary_board_cost = self.calculate_attack_pairs(temporary_board,psize)
                if temporary_board_cost < least_cost:
                  least_cost = temporary_board_cost
                  desirable_cost = temporary_board
    self.queen_board = desirable_cost
    self.cost = least_cost
 
  #This function tries moving every queen to every spot, with only one move
  #and returns the move that has the least number of attacks pairs or if not 
  #then it will atleast try to send the state with same heuristic
  def calc_hueristic(self,psize):
    equal_h_count = 0
    equi = {}
    presentcost = self.calculate_attack_pairs(self.queen_board,self.psize)
    least_cost = self.calculate_attack_pairs(self.queen_board,self.psize)
    desirable_cost = self.queen_board
    #move one queen at a time, the optimal single move by brute force
    for q_col in range(0,psize):
      for q_row in range(0,psize):
        if self.queen_board.board[q_row][q_col] == "Q":
          #get the lowest cost by moving this queen
          for m_row in range(0,psize):
              if self.queen_board.board[m_row][q_col] != "Q":
                #try placing the queen here and see if it's any better
                temporary_board = copy.deepcopy(self.queen_board)
                temporary_board.board[q_row][q_col] = "."
                temporary_board.board[m_row][q_col] = "Q"
                temporary_board_cost = self.calculate_attack_pairs(temporary_board,psize)
                if temporary_board_cost < least_cost:
                  least_cost = temporary_board_cost
                  desirable_cost = temporary_board
                if temporary_board_cost == presentcost:
                  equi[equal_h_count] = temporary_board
                  equal_h_count += 1
    if least_cost == presentcost:
        print("Successors with hueristic same as that of the current state:", equal_h_count)
        if(equal_h_count == 1):
            desirable_cost = equi[0]  
        elif(equal_h_count > 1):
            rand_ind = random.randint(0,equal_h_count - 1)
            print("Random index to choose one of the same heuristic ssuccessor:", rand_ind)
            desirable_cost = equi[rand_ind]
    self.queen_board = desirable_cost
    self.cost = least_cost




