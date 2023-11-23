using Random
using LinearAlgebra
c = randn(5)
sqrNrm1 = norm(c)^2 
sqrNrm2 = dot(c,c)
areEqual = isapprox(sqrNrm1,sqrNrm2)
println("The two values are equal:")
println(areEqual)



