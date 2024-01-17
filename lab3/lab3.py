def hush_1(name):
    return len(name) % 10

def hush_2(name):
    first_char_value = ord(name[0].lower()) - ord('a') + 1
    return first_char_value % 10

def hush_3(name):
    primes = generate_primes(26)
    name = name.replace(' ', '')
    hash_value = sum(primes[ord(char.lower()) - ord('a')] for char in name)
    return hash_value % 10

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def hash_and_store(arr, hash_func, name, value):
    index = hash_func(name)
    arr[index] = value

arr = [""] * 10
hash_and_store(arr, hush_1, "Alice", "555-1234")
hash_and_store(arr, hush_1, "Bob", "555-5678")
hash_and_store(arr, hush_1, "Charlie", "555-9876")
hash_and_store(arr, hush_1, "David", "555-4321")
print("Hash 1, Names and Phone Numbers:", arr)

arr = [""] * 10
hash_and_store(arr, hush_2, "Emily", "88005553535")
hash_and_store(arr, hush_2, "Brian", "88005552525")
hash_and_store(arr, hush_2, "Beth", "88005551515")
hash_and_store(arr, hush_2, "Daniel", "88005550505")
print("Hash 2, Names and Phone Numbers:", arr)

arr = [""] * 10
hash_and_store(arr, hush_3, "Grace", "88001112222")
hash_and_store(arr, hush_3, "Benjamin", "88001113333")
hash_and_store(arr, hush_3, "Olivia", "88001114444")
hash_and_store(arr, hush_3, "Daniel", "88001115555")
print("Custom Hash 3, Names and Updated Phone Numbers:", arr)
