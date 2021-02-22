# https://www.acmicpc.net/problem/2435
# 기상청 인턴 신현수

# input
N, K = map( int, input("").split() );
num = list(map( int, input("").split() ));

max = 0

# set initial value of 'max'
for i in range(0,K):
  max += num[i]

# retrieve max value
for i in range(0, N-K+1):
  sum = 0
  for j in range(i, i+K):
    sum += num[j]
  
  if(sum > max):
    max = sum

# output
print(max)