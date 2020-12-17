import System.IO.Unsafe

-- PARSE AND READ THE FILE
textFromFile :: String -> String
textFromFile file = do unsafePerformIO (readFile file)

split :: Char -> String -> [String]
split _ "" = []
split delimiter str = 
    let (start, rest) = break (== delimiter) str
        (_, remain) = span (== delimiter) rest
     in start : split delimiter remain

-- Check for amount
passWordOccurrences :: String -> Char -> Int
passWordOccurrences pwd c = length ([x | x <- pwd, x == c])

sufficientCharacters :: String -> Char -> Int -> Int -> Bool
sufficientCharacters pwd c mn mx = mn <= amount && amount <= mx
                        where amount = (passWordOccurrences pwd c)

correctLine :: String -> Bool
correctLine line = sufficientCharacters (tail (part !! 1)) (values !! 1 !! 0) (read (numbers !! 0)) (read (numbers !! 1))
                    where part = split ':' line
                          values = split ' ' (part !! 0)
                          numbers = split '-' (values !! 0)

answer :: Int
answer = length [1 | x <- init (lines (textFromFile "input.txt")), correctLine x]
