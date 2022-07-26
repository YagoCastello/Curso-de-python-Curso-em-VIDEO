m = float(input('Digite um valor em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(
    "O valor que você digitou equivale a :\n{} km={} {} \n{} hm={} {} \n {} dam={} {} \n {} m={} {} \n {} cm={} {}\n {} mm={} {}".format('\033[1;31;42m',km,'\033[m','\033[4;32;45m', hm,'\033[m','\033[7;33;44m',dam,'\033[m','\033[4;36;42m',m,'\033[m','\033[4;36;41m',cm,'\033[m','\033[7;32;46m',mm,'\033[m'))
