from MR import *

N = input("From which integer do you want to start ?")
N = int(N)
k = input("Control the error with parameter k: ")
k = int(k)

n = N
while True:
    if mr(n, k) == 1:
            break
    n += 1

prob = 1-pow(4, -k)
print("The first probable prime after: ", N, "is ", n,
      ", with probability ", round(prob, 4))
