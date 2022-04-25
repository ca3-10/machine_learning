


reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]

getFirstElements n _ | n <= 0 = []
getFirstElements _ [] = []
getFirstElements n (x:xs) = x : getFirstElements (n-1) xs

getLastElements n = reverseList . getFirstElements n . reverseList


