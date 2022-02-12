classifyNumber x = if x < 0 then return "negative" else return "nonnegative"
main = print (classifyNumber 5)

  
