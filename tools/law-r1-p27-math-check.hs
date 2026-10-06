import Data.List (transpose)

type V=(Int,Int,Int)

n0Drop, n1Drop, gateDrop, n0Restore, n1Restore :: V
n0Drop=(-1,0,-1)
n1Drop=(-1,-1,-1)
gateDrop=(0,-1,-1)
n0Restore=(1,0,1)
n1Restore=(1,1,1)

det2 :: (Int,Int) -> (Int,Int) -> Int
det2 (a,b) (c,d)=a*d-b*c

rank2x3 :: V -> V -> Int
rank2x3 (a,b,c) (d,e,f)
  | all (==0) [a,b,c,d,e,f] = 0
  | or [det2 (a,b) (d,e)/=0, det2 (a,c) (d,f)/=0, det2 (b,c) (e,f)/=0] = 2
  | otherwise = 1

main :: IO ()
main=do
  let nonNested = n0Drop /= n1Drop
      oneSep = let (_,g0,_)=n0Drop; (_,g1,_)=n1Drop in g0 /= g1
      n0Rank=rank2x3 n0Drop gateDrop
      n1Rank=rank2x3 n1Drop gateDrop
      restoreRedundantN0 = n0Restore == let (a,b,c)=n0Drop in (-a,-b,-c)
      restoreRedundantN1 = n1Restore == let (a,b,c)=n1Drop in (-a,-b,-c)
      pass=and [nonNested,oneSep,n0Rank==2,n1Rank==2,restoreRedundantN0,restoreRedundantN1]
  putStrLn $ "P27_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "NON_NESTED=" ++ show nonNested
  putStrLn $ "ONE_INTERVENTION_SEPARATOR=" ++ show oneSep
  putStrLn $ "N0_KERNEL_RANK=" ++ show n0Rank
  putStrLn $ "N1_KERNEL_RANK=" ++ show n1Rank
  putStrLn $ "RESTORE_REDUNDANT_N0=" ++ show restoreRedundantN0
  putStrLn $ "RESTORE_REDUNDANT_N1=" ++ show restoreRedundantN1
  if pass then pure () else error "P27 math failed"
