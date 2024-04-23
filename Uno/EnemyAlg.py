#*****************************************************
# Ben Heffron
# Program: EnemyAlg
#
# 3/31/2023
# This algorithm works in the background of the UNO
# program. Detects what cards a player does not have
# and tracks the amount of cards each player has.
#
# 5/17/2023
# Program keeps track opf enemy players with 2 or less
# cards. Also detects the card color with the most
# cards.
#
# 5/18/2023
# Program shows the user which card to play based on 
# most cards in hand.
#
# 5/22/2023
# Program implements the most card color play method
#*****************************************************
import random
#from Card import*
class EnemyAlg:
   # initializes the EnemyAlg class
   def __init__(self, enemyCt):
      self.enemyCt = enemyCt
      self.enemyC = [[],[],[],[]]
      self.enemyN = [[],[],[],[]]
      self.danger = []
   
   # changes enemy card count
   def changeEnemyCt(self, cards):
      self.enemyCt = cards
      if len(self.danger) > 0:
         for i in range (0, len(self.danger)):
            if len(self.danger) > 0:
               self.danger.clear()
      for i in range(0, len(self.enemyCt)):
         if self.enemyCt[i] < 3:
            self.danger.append(i+1)
         
   
   # checks how many cards enemies have
   def checkEnemyCardCt(self):
      self.danger = []
      for i in range(0, len(self.enemyCt)):
         if self.enemyCt[i] < 3:
            self.danger.append(i+1)
   
   # saves the color and number that a player had drawn to
   def saveNoColor(self, player, color, num):
      check = []
      checkC = True
      checkN = True
      for i in range(0, len(self.enemyC[player-1])):
         if color == self.enemyC[player-1][i]:
            checkC = False
            break
      for i in range(0, len(self.enemyN[player-1])):
         if num == self.enemyN[player-1][i]:
            checkN = False
            break
      if checkC:
         self.enemyC[player-1].append(color)
      if checkN and num != 13 or num!= 14:
         self.enemyN[player-1].append(num)
      print(self.enemyC)
      print(self.enemyN)
      
   # will be able to have enemy players switch the card number or color based on card count
   def forceSwitch(self, turnNum):
      
      for i in range(0, len(enemyCt)):
         if self.enemyCt[i] <= 2 and (i+1) != turnNum:
            pass
            
   # checks whether the color should change
   def checkColorChange(self, player, color, num):
      checkN = []
      for i in range(0, len(self.enemyC[player-1])):
         if color != self.enemyC[player-1][i]:
            del self.enemyC[player-1][i]
      for i in range(0, len(self.enemyN[player-1])):   
         if num != self.enemyN[player-1][i]:
            del self.enemyN[player-1][i]
       
   # deletes the stated colors that a player has based off certain conditions in UNO      
   def deleteNoColor(self, player):
      if len(self.enemyN[player-1]) != 0: 
        for i in range(0, len(self.enemyC[player-1])):
          del self.enemyC[player-1][0]
        for i in range(0, len(self.enemyN[player-1])):
          del self.enemyN[player-1][0]
   
   # checks which card color is the most for a player
   def playOrder(self, pileColor, pileNum, playerCardsC, playerCardsN):
         r = 0
         b = 0
         g = 0
         y = 0
         most = 'red'
         mostC = 0
         for i in range(0, len(playerCardsC)):
            if playerCardsC[i] == 'red':
               r += 1
               mostC += 1
            elif playerCardsC[i] == 'blue':
               b += 1
            elif playerCardsC[i] == 'green':
               g += 1
            elif playerCardsC[i] == 'yellow':
               y += 1
         
         if b > r:
            most = 'blue'
            mostC = b
         if y > mostC:
            most = 'yellow'
            mostC = y
         if g > mostC:
            most = 'green'
         
         if pileColor == most:
            for i in range (0, len(playerCardsC)): 
               if most == playerCardsC[i]:
                  return(i+1)
         else:
            for i in range (0, len(playerCardsC)):
               if (playerCardsN[i] == pileNum and most == playerCardsC[i]):
                     return (i+1)
                  
            for i in range (0, len(playerCardsC)):
               if (playerCardsN[i] == pileNum or playerCardsC[i] == pileColor or playerCardsC[i] == 'wild'):
                  return(i+1)
                  
         return(0)
                  
               
            
      
      
      