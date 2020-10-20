def factorization(num, prime, ans):
    while num != 1:
        if num % prime == 0:
            ans.append(prime)
            num = num / prime
        else:
            if prime == 2:      #tento blok říká, že pokud jsme dělili číslem 2,
                prime = 3       #další máme zvolit číslo 3, jinak skáčeme o 2 čísla
            else:               #(nemá smysl testovat sudá čísla)
                prime += 2
        
ans = []
num = int(input("Vložte číslo, jehož faktorizaci chcete provést.\n"))
prime = 2
factorization(num, prime, ans)
print(ans)
input()
