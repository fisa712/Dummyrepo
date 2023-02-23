import numpy as np 
import pandas as pd

class Wallet:
  def __init__(self):
    self.balance = np.array(0)
   
  def setAmount(self, amount):
    self.balance = np.array(amount)
    
  def getAmount(self):
    return self.balance
  
  def removeAmount(self, withdrawal):
    if self.balance>=withdrawal:
      self.balance -= withdrawal
    else:
       return 'Low_Amount'
    return 'Succesfully Done'
