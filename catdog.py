def cat_dog(str):
  a="cat"
  b="dog"
  s=0
  c=0
  while(i<=str):
    i=i+1
    if a in i:
     s=s+1
    elif b in i:
      c=c+1
    if s==c:
      return True
      print("true")
    else :
      return False
    
    if(s==c):
        print("true")
  return cat_dog("catdog") 
