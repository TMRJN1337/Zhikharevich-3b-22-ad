def count_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i] == s[j-1]:  # если первый и последний символы подстроки равны
                count += 1  # увеличиваем счетчик
    return count
s = input("Введите строку: ")
count = count_substrings(s)  # вызываем функцию count_substrings
print("Количество подстрок, начинающихся и заканчивающихся одним и тем же символом:", count)
