import random

def lotto_recommend(count=5):
    results = []
    for _ in range(count):
        numbers = []
        while len(numbers) < 6:
            n = random.randint(1, 45)
            if n not in numbers:
                numbers.append(n)
        numbers.sort()
        bonus = random.randint(1, 45)
        while bonus in numbers:
            bonus = random.randint(1, 45)
        results.append((numbers, bonus))
    return results

if __name__ == "__main__":
    print("행운의 777 로또 번호 추천기 ")
    for i, (nums, bonus) in enumerate(lotto_recommend(5), 1):
        print(f"{i}번 세트: {nums} + 보너스 {bonus}")

