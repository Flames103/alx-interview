def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_choose_prime(numbers):
        for num in numbers:
            if is_prime(num):
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        numbers = list(range(1, n + 1))
        maria_turn = True

        while can_choose_prime(numbers):
            prime_to_remove = 2 if maria_turn else 3

            for num in numbers:
                if num % prime_to_remove == 0 and is_prime(num):
                    numbers.remove(num)

            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)
 
