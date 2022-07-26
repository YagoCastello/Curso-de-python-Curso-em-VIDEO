x=int(input('Digite um numero de  4 digitos de 0 a 9999:'))
U=x//1%10
D=x//10%10
C=x//100%10
M=x//1000%10
print("Unidade:{}{}{} \n Dezena:{}{}{} \n Centena:{}{}{} \n Milhar: {}{}{} ".format('\033[1;45;31m',U,'\033[m','\033[7;36;45m',D,'\033[m','\033[7;42;35m',C,'\033[m','\033[1;45;36m',M,'\033[m'))