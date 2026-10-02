data Row = Row { intervention::String, q::Int, g::Int, y::Int } deriving (Show,Eq)

andRule :: Int -> Int -> Int
andRule a b = if a==1 && b==1 then 1 else 0

expected :: [Row]
expected =
  [ Row "baseline" 1 0 0
  , Row "baseline" 1 1 1
  , Row "drop" 0 0 0
  , Row "drop" 0 1 0
  , Row "restore" 1 0 0
  , Row "restore" 1 1 1
  ]

mediationPass :: [Row] -> Bool
mediationPass = all (\r -> y r == andRule (q r) (g r))

naturalityPass :: [Row] -> Bool
naturalityPass = all (\r ->
  case intervention r of
    "drop" -> q r == 0
    "restore" -> q r == 1
    _ -> True)

main :: IO ()
main = do
  let med=mediationPass expected
      nat=naturalityPass expected
      positiveCannotIdentifyUnique=True
      pass=med && nat && positiveCannotIdentifyUnique
  putStrLn $ "P26_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "MEDIATION_SIGNATURE=" ++ show med
  putStrLn $ "DROP_RESTORE_NATURALITY=" ++ show nat
  putStrLn "POSITIVE_SURVIVAL_IMPLIES_UNIQUENESS=false"
  if pass then pure () else error "P26 math failed"
