import Data.List (nub)
import System.Directory (createDirectoryIfMissing)

data S = P | L deriving (Eq, Ord, Show)
data E = I | D | R deriving (Eq, Ord, Show)

apply :: E -> S -> S
apply I s = s
apply D _ = L
apply R _ = P

compose :: E -> E -> E
compose f g =
  head [h | h <- [I,D,R], all (\s -> apply h s == apply f (apply g s)) [P,L]]

eval :: [E] -> E
eval = foldr compose I

parts3 :: [[[E]]]
parts3 =
  [ [[I],[D],[R]]
  , [[I,D],[R]]
  , [[I,R],[D]]
  , [[I],[D,R]]
  , [[I,D,R]]
  ]

sameBlock :: [[E]] -> E -> E -> Bool
sameBlock p x y = any (\b -> elem x b && elem y b) p

isCongruence :: [[E]] -> Bool
isCongruence p = and
  [ not (sameBlock p x y) ||
    (sameBlock p (compose a x) (compose a y) &&
     sameBlock p (compose x a) (compose y a))
  | x <- [I,D,R], y <- [I,D,R], a <- [I,D,R]
  ]

wordsN :: Int -> [[E]]
wordsN 0 = [[]]
wordsN k = [x:xs | x <- [I,D,R], xs <- wordsN (k-1)]

wordsUpTo :: Int -> [[E]]
wordsUpTo n = concatMap wordsN [0..n]

normalFormExpected :: [E] -> E
normalFormExpected w =
  case dropWhile (==I) w of
    [] -> I
    (x:_) -> x

obsEraseOrder :: (S -> Int) -> Bool
obsEraseOrder q =
  all (\s -> q (apply R (apply D s)) == q (apply D (apply R s))) [P,L]

main :: IO ()
main = do
  let congruences = filter isCongruence parts3
  let expectedCongruences = [[[I],[D],[R]], [[I],[D,R]], [[I,D,R]]]
  let uniqueProper = congruences == expectedCongruences
  let normalFormPass = all (\w -> eval w == normalFormExpected w) (wordsUpTo 7)
  let twoStateFaithful = length (nub [[apply e P, apply e L] | e <- [I,D,R]]) == 3
  let qDistinguish P = 1 :: Int
      qDistinguish L = 0
      qCollapse _ = 0 :: Int
  let observationTheorem = not (obsEraseOrder qDistinguish) && obsEraseOrder qCollapse
  let pass = normalFormPass && uniqueProper && twoStateFaithful && observationTheorem

  createDirectoryIfMissing True "out-p23"
  writeFile "out-p23/p23-math.json" $ unlines
    [ "{"
    , "  \"stage\": \"EvoNOMOS Generation VIII LAW-R1-P23\","
    , "  \"status\": \"" ++ (if pass then "PASS" else "FAIL") ++ "\","
    , "  \"normal_form\": \"" ++ (if normalFormPass then "PASS" else "FAIL") ++ "\","
    , "  \"unique_nontrivial_proper_congruence_D_eq_R\": \"" ++ (if uniqueProper then "PASS" else "FAIL") ++ "\","
    , "  \"minimal_faithful_state_size_two\": \"" ++ (if twoStateFaithful then "PASS" else "FAIL") ++ "\","
    , "  \"noncommutativity_observation_theorem\": \"" ++ (if observationTheorem then "PASS" else "FAIL") ++ "\","
    , "  \"monoid_type\": \"identity_adjoined_two_element_left_zero_band\","
    , "  \"proper_boolean_quotient\": \"D~R\""
    , "}"
    ]

  putStrLn $ "P23_MATH=" ++ if pass then "PASS" else "FAIL"
  putStrLn $ "NORMAL_FORM=" ++ if normalFormPass then "PASS" else "FAIL"
  putStrLn $ "UNIQUE_PROPER_CONGRUENCE=" ++ if uniqueProper then "PASS" else "FAIL"
  putStrLn $ "MIN_FAITHFUL_DEGREE_2=" ++ if twoStateFaithful then "PASS" else "FAIL"
  putStrLn $ "OBSERVATION_THEOREM=" ++ if observationTheorem then "PASS" else "FAIL"
  if pass then pure () else error "P23 math checker failed"
