package f20audit

// Actual observations transcribed from verified original job raw logs in
// GitHub Actions run 41995425112, dated 2026-11-05. This is retrospective,
// after the historical commit subjects/patches were exposed to researchers.
func OriginalCohort() []OriginalCase {
 return []OriginalCase{
  {
   ID:"chi",Repo:"go-chi/chi",
   ParentSHA:"882c15e6462ce0630529d04c330e84942ebd059d",
   FixedSHA:"6ceb498b221efa11f559602beb2463b8b52c2161",
   AuthoredUTC:"2024-09-26T17:44:06Z",
   CommitSubject:"Fix Mux.Find not correctly handling nested routes",
   Observer:RoutePattern,Input:"Find(POST,/api/groups/v2/17)",
   Before:"/{id}",After:"/api/groups/v2/{id}",
   OriginalJobID:127137439627,PublicAPI:true,SubjectDisclosedBeforeOracle:true,
  },
  {
   ID:"httprouter",Repo:"julienschmidt/httprouter",
   ParentSHA:"ef8578da8d8e1217ea44313b23edf46154b198ab",
   FixedSHA:"484018016424d215c0b87c42f4c9b57d980fbd00",
   AuthoredUTC:"2024-01-30T10:56:56Z",
   CommitSubject:"fix: only append MethodOptions as allowed method if HandleOPTIONS is true",
   Observer:AllowedMethodsHelper,Input:"allowed(/probe,POST) with HandleOPTIONS=false",
   Before:"GET, OPTIONS",After:"GET",
   OriginalJobID:127137439769,PublicAPI:false,SubjectDisclosedBeforeOracle:true,
  },
  {
   ID:"gin",Repo:"gin-gonic/gin",
   ParentSHA:"9d11234efec1e5517b2887a6e7dfbc9c017bc52c",
   FixedSHA:"ea53388e6ee4a6a0a1647b390c56eeed780e7e56",
   AuthoredUTC:"2024-10-26T00:28:59Z",
   CommitSubject:"fix tree Keep panic infos consistent when wildcard type build failed",
   Observer:InternalPanic,Input:"node.insertChild(*all,*all,nil) internal invalid input",
   Before:"runtime error: index out of range [-1]",
   After:"no / before catch-all in path '*all'",
   OriginalJobID:127137439315,PublicAPI:false,SubjectDisclosedBeforeOracle:true,
  },
 }
}
