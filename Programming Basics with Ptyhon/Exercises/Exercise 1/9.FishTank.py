daljina = int(input())
shirochina = int(input())
visochina = int(input())
procent = int(input())

obem = daljina * shirochina * visochina
zaeto_mqsto = (procent/100) * obem
ostanalo_mqsto = (obem - zaeto_mqsto) / 1000

print(f"{ostanalo_mqsto}")