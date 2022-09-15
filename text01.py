lis=[]
i=1
count=0
sum=0.0
avg=0.0
while i :
    str=input('输入一个数字：')
    if str=='done':
        break

    else:
        try:
            new_str=float(str)
            lis.append(new_str)
        except:
            print('输入错误！')

for n in lis:
    sum+=n
    count+=1

avg=sum/count

mx=max(lis)  #最大值
mi=min(lis)   #最小值

print('max:',mx,'min:',mi)
#print('sum=',sum,'count=',count,'avg=',avg)