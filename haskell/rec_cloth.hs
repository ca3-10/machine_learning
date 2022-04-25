
recommendClothing degreeC 
    | degreeF >= 80 = "wear a shortsleeve shirt"
    | (80 > degreeF) && (degreeF >= 65) = "wear a longsleeve shirt"
    | (65 > degreeF) && (degreeF >= 50) = "wear a sweater"
    | degreeF <= 50 = "wear a jacket"
    where degreeF = (degreeC * 1.8) + 32
