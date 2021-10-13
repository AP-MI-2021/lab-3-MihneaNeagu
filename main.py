def check_if_palindrome(n):
    '''
    Functia verifica daca un numar este palindrom
    param: n-numarul de verificat
    return: True daca nr este palindrom, False daca nu
    '''
    aux=n
    inv=0
    while aux:
        inv=inv*10+int(aux%10)
        aux=int(aux/10)
    if n==inv:
        return True
    else:
        return False
def check_if_power(n,k):
    '''
    Functia verifica daca un numar este putere a unui divizor al sau la puterea k
    param: n-numarul de verificat, k-puterea
    return: True daca nr este putere a unui divizor al sau la puterea k, False daca nu
    '''
    for d in range(1,n//2+1):
        if d**k==n:
            return True
    return False
def check_if_prime(n):
    '''
    Functia verifica daca un numar este prim
    param: n-numarul de verificat
    return: True daca nr este prim, False daca nu
    '''
    if n==2:
        return True
    if n==1 or n<=0:
        return False
    for d in range(2,n):
        if n%d==0:
            return False
    return True
    
def get_longest_all_palindromes(list):
    '''
    Functia calculeaza subsecventa cea mai lunga de numere palindrom
    param: list-lista de numere
    return: rezultat-cea mai lunga subsecventa cu conditia data
    '''
    largest = 0
    temp_largest = 0
    location = 0
    for count, value in enumerate(list):
        if check_if_palindrome(value)==True:
            temp_largest += 1
        else:
            temp_largest = 0
        if temp_largest >= largest:
            largest = temp_largest
            location = count + 1 - temp_largest
    rezultat = []
    for i in range(location,location+largest):
        rezultat.append(list[i])
    
    return rezultat


def get_longest_powers_of_k(list,k):
    '''
    Functia calculeaza subsecventa cea mai lunga de numere ce pot fi scrise la puterea k
    param: list-lista de numere,k-puterea
    return: rezultat-cea mai lunga subsecventa cu conditia data
    '''
    largest = 0
    temp_largest = 0
    location = 0
    for count, value in enumerate(list):
        if check_if_power(value,k)==True:
            temp_largest += 1
        else:
            temp_largest = 0
        if temp_largest >= largest:
            largest = temp_largest
            location = count + 1 - temp_largest
    rezultat= []
    for i in range(location,location+largest):
        rezultat.append(list[i])
    return rezultat

def get_longest_all_primes(list):
    '''
    Functia calculeaza subsecventa cea mai lunga de numere prime
    param: list-lista de numere
    return: rezultat-cea mai lunga subsecventa cu conditia data
    '''
    largest = 0
    temp_largest = 0
    location = 0
    for count, value in enumerate(list):
        if check_if_prime(value)==True:
            temp_largest += 1
        else:
            temp_largest = 0
        if temp_largest >= largest:
            largest = temp_largest
            location = count + 1 - temp_largest
    rezultat = []
    for i in range(location,location+largest):
        rezultat.append(list[i])
    return rezultat

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1,111,333,222,54,23])==[1,111,333,222]

test_get_longest_all_palindromes()

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([8,27,64,5,23,11],3)==[8,27,64]

test_get_longest_powers_of_k()

def test_get_longest_all_primes():
    assert get_longest_all_primes([5,7,11,20,13,15])==[5,7,11]

test_get_longest_all_primes

def citire_afisare_get_longest_all_palindromes():
    list=[]
    while True:
        element=input("Element: ")
        if element=="x":
            break
        else:
            list.append(int(element))
    print(get_longest_all_palindromes(list))

def citire_afisare_get_longest_powers_of_k():
    list=[]
    while True:
        element=input("Element: ")
        if element=="x":
            break
        else:
            list.append(int(element))
    k=int(input("Puterea: "))
    print(get_longest_powers_of_k(list,k))

def citire_afisare_get_longest_all_primes():
    list=[]
    while True:
        element=input("Element: ")
        if element=="x":
            break
        else:
            list.append(int(element))
    print(get_longest_all_primes(list))

def main():
    # interfata de tip consola aici
    secventa=input("Secventa: ")
    if secventa=="1":
        citire_afisare_get_longest_all_palindromes()
    if secventa=="2":
        citire_afisare_get_longest_powers_of_k()
    if secventa=="3":
        citire_afisare_get_longest_all_primes()


    
main()
exit(0)