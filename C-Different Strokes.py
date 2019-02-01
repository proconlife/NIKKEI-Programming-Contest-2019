n=int(input())
a_=[]
b_=[]
 
for i in range(n):
    a,b = map(int,input().split())
    a_.append([a+b,a,i])
    b_.append([a+b,b,i])
 
sa_ = sorted(
  a_,
  key = lambda x: (x[0], x[1]),
)
sb_ = sorted(
  b_,
  key = lambda x: (x[0], x[1]),
)
 
i_={}
res=0
 
for i in range(n):
    if i % 2 :
        item = sb_.pop()
        while ( item[2] in i_ ) :
            item = sb_.pop()
        res -= item[1]
        i_[item[2]]=1
    else :
        item = sa_.pop()
        while ( item[2] in i_ ) :
            item = sa_.pop()
        res += item[1]
        i_[item[2]]=1
 
print(res)
