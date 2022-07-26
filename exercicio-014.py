c=float(input('Digite a temperatura em graus Cº:'))
f=c*1.8+32
k=c+273
print(' {}{:.2f}{} Cº equivale a : \n {}{:.2f}{} ºF \n {}{:.2f}{} ºK'.format('\033[1;33;45m',c,'\033[m','\033[4;31;47m',f,'\033[m','\033[31;7;46m',k,'\033[m'))