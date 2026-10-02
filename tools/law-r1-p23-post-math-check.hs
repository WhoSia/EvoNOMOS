import Data.List (nub, permutations)
import System.Directory (createDirectoryIfMissing)

type F = [Int]

apply :: F -> Int -> Int
apply f x = f !! x

compose :: F -> F -> F
compose f g = [apply f (apply g x) | x <- [0..length f - 1]]

idF :: Int -> F
idF n = [0..n-1]

allFuncs :: Int -> [F]
allFuncs n = sequence (replicate n [0..n-1])

idem :: F -> Bool
idem f = compose f f == f

leftZeroPair :: F -> F -> Bool
leftZeroPair d r = compose d r == d && compose r d == r

rightZeroPair :: F -> F -> Bool
rightZeroPair d r = compose d r == r && compose r d == d

faithfulExists :: Int -> (F -> F -> Bool) -> Bool
faithfulExists n orient =
  or [ orient d r
     | d <- fs, r <- fs
     , d /= r, d /= i, r /= i
     , idem d, idem r
     ]
  where
    fs = allFuncs n
    i = idF n

mulL :: Int -> Int -> Int
mulL 0 x = x
mulL x _ = x

mulR :: Int -> Int -> Int
mulR 0 y = y
mulR x 0 = x
mulR _ y = y

isIso :: (Int -> Int -> Int) -> (Int -> Int -> Int) -> Bool
isIso a b =
  any ok (permutations [0,1,2])
  where
    ok p = p !! 0 == 0 &&
      and [ p !! (a x y) == b (p !! x) (p !! y)
          | x <- [0,1,2], y <- [0,1,2] ]

qPresence :: Int -> Int
qPresence 0 = 1 -- LEGACY
qPresence 1 = 1 -- CANONICAL
qPresence 2 = 0 -- ABSENT
qPresence _ = error "bad state"

dK :: F
dK = [2,1,2]

rK :: F
rK = [1,1,2]

main :: IO ()
main = do
  let findMin xs = case xs of
        (x:_) -> x
        [] -> error "no faithful degree found in bounded search"
  let leftMin = findMin [n | n <- [1..4], faithfulExists n leftZeroPair]
  let rightMin = findMin [n | n <- [1..4], faithfulExists n rightZeroPair]
  let nonIso = not (isIso mulL mulR)
  let opposite = and [mulL x y == mulR y x | x <- [0,1,2], y <- [0,1,2]]
  let kubeRight = rightZeroPair dK rK
  let orderVisible = qPresence (apply (compose dK rK) 0) /= qPresence (apply (compose rK dK) 0)
  let endpointOnly = qPresence 0 == qPresence 1 && qPresence 1 /= qPresence 2
  let pass = leftMin == 2 && rightMin == 3 && nonIso && opposite && kubeRight && orderVisible && endpointOnly

  createDirectoryIfMissing True "out-p23-post"
  writeFile "out-p23-post/p23-post-math.json" $ unlines
    [ "{"
    , "  \"stage\": \"EvoNOMOS Generation VIII LAW-R1-P23\","
    , "  \"status\": \"" ++ (if pass then "PASS" else "FAIL") ++ "\","
    , "  \"authority\": \"POST_FRESH_DEVELOPMENT_ONLY\","
    , "  \"left_zero_min_faithful_degree\": " ++ show leftMin ++ ","
    , "  \"right_zero_min_faithful_degree\": " ++ show rightMin ++ ","
    , "  \"left_right_not_isomorphic\": " ++ show nonIso ++ ","
    , "  \"opposite_monoids\": " ++ show opposite ++ ","
    , "  \"kubernetes_right_zero_representation\": " ++ show kubeRight ++ ","
    , "  \"presence_observation_detects_order\": " ++ show orderVisible ++ ","
    , "  \"full_orbit_injectivity_not_necessary\": " ++ show endpointOnly
    , "}"
    ]

  putStrLn $ "P23_POST_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "LEFT_ZERO_MIN_DEGREE=" ++ show leftMin
  putStrLn $ "RIGHT_ZERO_MIN_DEGREE=" ++ show rightMin
  putStrLn $ "NONISOMORPHIC=" ++ show nonIso
  putStrLn $ "OPPOSITE=" ++ show opposite
  putStrLn $ "ORDER_VISIBLE=" ++ show orderVisible
  if pass then pure () else error "P23 post-fresh math failed"
