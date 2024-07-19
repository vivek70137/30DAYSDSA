def squirrel_play(temp, summer):
  if temp in range(60,91) or (summer) ==True:
    return True
  return False
    
print(squirrel_play(50,True))
