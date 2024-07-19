def in1to10(n, outside_mode):
  if (n in range (1,11)) :
    return True  
  elif  (outside_mode==True) :
     if(n<=1) or( n>=10):
      return True
  return False
