soma = 0
ct = 0
for ip in range(1, 501, 2):
    if ip % 3 == 0:
        ct = ct + 1
        soma = soma + ip
print(f'A quantidade de números ímpares divisíveis por 3 entre 1 e 500 é {ct} e a soma total deles é {soma}')
