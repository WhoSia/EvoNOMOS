tables :: [(String,[Int])]
tables =
  [ ("AND",   [0,0,0,1])
  , ("OR",    [0,1,1,1])
  , ("XOR",   [0,1,1,0])
  , ("Q_ONLY",[0,0,1,1])
  , ("G_ONLY",[0,1,0,1])
  , ("NOR",   [1,0,0,0])
  , ("NAND",  [1,1,1,0])
  , ("XNOR",  [1,0,0,1])
  ]

dedup :: Eq a => [a] -> [a]
dedup []=[]
dedup (x:xs)=x:dedup (filter (/=x) xs)

uniqueMatch :: [Int] -> Maybe String
uniqueMatch xs = case [n | (n,t)<-tables, t==xs] of
  [n] -> Just n
  _   -> Nothing

main :: IO ()
main = do
  let packet=[0,0,0,1]
      m=uniqueMatch packet
      allDistinct=length (map snd tables)==length (dedup (map snd tables))
      pass=m==Just "AND" && allDistinct
  putStrLn $ "P25_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "AND_PACKET_MATCH=" ++ show m
  putStrLn $ "FROZEN_STANDARD_RIVALS_DISTINCT=" ++ show allDistinct
  if pass then pure () else error "P25 math failed"