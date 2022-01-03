from test import *
import random

# parameters
k1 = 1
k2 = 5

# setting seed
random.seed(1)

# Fermat general results over [5, 8000] list
acc_f1, t_f1 = acc_time(method="fermat", k=k1)
acc_f2, t_f2 = acc_time(method="fermat", k=k2)

# Miller-Rabin general results over [5, 8000] list
acc_mr1, t_mr1 = acc_time(method="miller rabin", k=k1)
acc_mr2, t_mr2 = acc_time(method="miller rabin", k=k2)

# accuracy on Carmichael numbers
acc_car_f1 = carmichael_acc(method="fermat", k=k1)
acc_car_f2 = carmichael_acc(method="fermat", k=k2)
acc_car_mr1 = carmichael_acc(method="miller rabin", k=k1)
acc_car_mr2 = carmichael_acc(method="miller rabin", k=k2)

# Printing results
s = f"""
#
# General performance results :
#
{'-' * 60}
# Fermat: k={k1}
# accuracy: {round(acc_f1, 3)} ,  time: {round(t_f1, 3)}
{'-' * 20}
# Fermat: k={k2}
# accuracy: {round(acc_f2, 3)} ,  time: {round(t_f2, 3)}
{'-' * 20}
# Miller-Rabin: k={k1}
# accuracy: {round(acc_mr1, 3)} ,  time: {round(t_mr1, 3)}
{'-' * 20}
# Miller-Rabin: k={k2}
# accuracy: {round(acc_mr2, 3)} ,  time: {round(t_mr2, 3)}
{'-' * 60}
#
# Results on Carmichael numbers : 
#
{'-' * 60}
# Fermat: k={k1}
# accuracy: {round(acc_car_f1, 3)}
{'-' * 20}
# Fermat: k={k2}
# accuracy: {round(acc_car_f2, 3)}
{'-' * 20}
# Miller-Rabin: k={k1}
# accuracy: {round(acc_car_mr1, 3)}
{'-' * 20}
# Miller-Rabin: k={k2}
# accuracy: {round(acc_car_mr2, 3)}
{'-' * 60}"""

print(s)

# plot of accuracy when varying parameter k (on Carmichael number 2821)
plot_accuracy_k()
