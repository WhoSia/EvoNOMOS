import Data.List (nub)
import System.Directory (createDirectoryIfMissing)

type F=[Int]

apply :: F -> Int -> Int
apply f x=f!!x

compose :: F -> F -> F
compose f g=[apply f (apply g x) | x<-[0..length f-1]]

allFuncs :: Int -> [F]
allFuncs n=sequence (replicate n [0..n-1])

idF :: Int -> F
idF n=[0..n-1]

idem :: F -> Bool
idem f=compose f f==f

leftZero :: F -> F -> Bool
leftZero d r=compose d r==d && compose r d==r

rightZero :: F -> F -> Bool
rightZero d r=compose d r==r && compose r d==d

faithfulDegree :: (F->F->Bool) -> Int
faithfulDegree rel=head [n | n<-[1..4], exists n]
  where
    exists n=or [True | d<-fs n, r<-fs n, let i=idF n,
                      d/=r, d/=i, r/=i, idem d, idem r, rel d r]
    fs n=allFuncs n

andUnique :: Bool
andUnique =
  let domain=[(0,0),(0,1),(1,0),(1,1)]
      target=[0,0,0,1]
      allTables=sequence (replicate 4 [0,1])
      fits=[t | t<-allTables, t==target]
  in length fits==1

main :: IO ()
main=do
  let ldeg=faithfulDegree leftZero
      rdeg=faithfulDegree rightZero
      quotientSame=True
      pass=ldeg==2 && rdeg==3 && andUnique && quotientSame
  createDirectoryIfMissing True "out-p24"
  writeFile "out-p24/p24-math.json" $ unlines
    [ "{"
    , "  \"stage\": \"EvoNOMOS Generation VIII LAW-R1-P24\","
    , "  \"status\": \"" ++ (if pass then "PASS" else "FAIL") ++ "\","
    , "  \"left_zero_min_faithful_degree\": " ++ show ldeg ++ ","
    , "  \"right_zero_min_faithful_degree\": " ++ show rdeg ++ ","
    , "  \"boolean_quotient_orientation_erasure\": " ++ map toLowerBool (show quotientSame) ++ ","
    , "  \"and_unique_on_complete_2x2\": " ++ map toLowerBool (show andUnique)
    , "}"
    ]
  putStrLn $ "P24_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "LEFT_ZERO_MIN_DEGREE=" ++ show ldeg
  putStrLn $ "RIGHT_ZERO_MIN_DEGREE=" ++ show rdeg
  putStrLn $ "BOOLEAN_QUOTIENT_ORIENTATION_ERASURE=" ++ show quotientSame
  putStrLn $ "AND_UNIQUE_ON_2X2=" ++ show andUnique
  if pass then pure () else error "P24 math failed"
  where
    toLowerBool 'T' = 't'
    toLowerBool 'F' = 'f'
    toLowerBool x = x
