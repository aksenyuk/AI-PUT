#Ex 20
r1=c(1,0,5,2)
r2=c(4,8,1,2)
r3=c(1,6,3,3)
r4=c(9,7,2,4)
len=length(r1)
half=len/2
M=rbind(r1,r2,r3,r4)
BTr=function(M){
  M1 = M[c(1, half),c(1,half)]
  M2 = M[c(half+1, len), c(half+1, len)]
  return(M1)
  return(M2)
}
BTr(M)
print(M1+M2)

#Ex 21
r1=c(1,0,5,2)
r2=c(4,8,1,2)
r3=c(1,6,3,3)
r4=c(9,7,2,4)
len=length(r1)
half=len/2
M=rbind(r1,r2,r3,r4)
BSum=function(M){
  M1 = M[c(1, half),c(1,half)]
  M2 = M[c(half+1, len),c(1,half)]
  M3 = M[c(1, half),c(half+1,len)]
  M4 = M[c(half+1, len), c(half+1, len)] 
  return(M1)
  return(M2)
  return(M3)
  return(M4)
}
BSum(M)
print(M1+M2+M3+M4)