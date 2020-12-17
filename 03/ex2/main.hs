import System.IO.Unsafe

-- PARSE AND READ THE FILE
textFromFile :: String -> String
textFromFile file = do unsafePerformIO (readFile file)

-- Split into lines, remove carriage returns
lineByline :: String -> [String]
lineByline file = [init x | x <- lines (textFromFile file)]

split :: Char -> String -> [String]
split _ "" = []
split delimiter str = 
    let (start, rest) = break (== delimiter) str
        (_, remain) = span (== delimiter) rest
     in start : split delimiter remain

-- Look for trees (420 WEED NOT FOUND)
getCoords :: Int -> Int -> Int -> [(Int, Int)]
getCoords down right mx = [(i*down, i*right) | i <- [0..mx], i*down < mx]

getTerrain :: [String] -> (Int, Int) -> Char
getTerrain field coords = (field !! (fst coords)) !! (snd coords `mod` width)
                        where width = length (field !! 0)

countTrees :: [String] -> Int -> Int -> Int
countTrees field down right = length [1 | x <- dir, (getTerrain field x) == '#']
                    where   l = length field
                            dir = getCoords down right l

calculateDirection :: Int -> Int -> Int
calculateDirection down right = countTrees (lineByline "input.txt") down right

answer :: Int
answer = product [calculateDirection (snd dir) (fst dir) | dir <- [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
