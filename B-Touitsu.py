n=int(input())
a,b,c=[input() for i in range(3)]
cnt=0
 
a_=list(a)
b_=list(b)
c_=list(c)
 
for i in range(n):
  cnt += len(list({a_[i],b_[i],c_[i]}))-1
 
print(cnt)
