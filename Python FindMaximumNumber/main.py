numbers = input("Sayı dizisi giriniz. Sayıları virgüller ile giriniz.")
strNumbers = numbers.split(",")
intNumbers = list(map(int, strNumbers))
maxNumber = intNumbers[0]
for item in intNumbers:
    if item > maxNumber:
        maxNumber = item
print(f"Dizideki en büyük sayı {maxNumber}")
    
