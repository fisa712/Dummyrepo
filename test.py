import numpy as np
from wallet import Wallet

def test_getAmount():
  asif = Wallet()
  asif.setAmount(1000)
  assert asif.getAmount()==np.array(1000)
  
  
def test_removeAmount_pass():
  asif = Wallet()
  asif.setAmount(1000)
  assert asif.removeAmount(100)=='Succesfully Done'

def test_removeAmount_low():
  asif = Wallet()
  asif.setAmount(1000)
  assert asif.removeAmount(2000)=='Low Amount'
