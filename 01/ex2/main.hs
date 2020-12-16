import System.IO.Unsafe

-- Last step: find the correct numbers
findSum :: [Int] -> Int
findSum xs = head [a*b*c | a <- xs, b <- xs, c <- xs, a + b + c == 2020]


-- PARSE AND READ THE FILE
textFromFile :: String -> String
textFromFile file = do unsafePerformIO (readFile file)

convertToInts :: String -> [Int]
convertToInts s = [read num :: Int | num <- init (lines s)]


-- Main function, tie everything together
answer :: Int
answer = findSum (convertToInts (textFromFile "input.txt"))
