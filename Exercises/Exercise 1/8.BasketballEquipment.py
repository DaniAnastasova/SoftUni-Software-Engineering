godishna_taksa = int(input())

shoes = godishna_taksa - ((40/100) * godishna_taksa)
ekip = shoes - ((20/100)* shoes)
ball = (1/4) * ekip
acsesoari = (1/5) * ball

final_price = shoes + ekip + ball + acsesoari + godishna_taksa
print(f"{final_price}")
