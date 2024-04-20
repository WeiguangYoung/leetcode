s = input()[2:]

result = 0

for i in range(len(s) - 1, -1, -1):
    n = int(s[i]) if "0" <= s[i] <= "9" else ord(s[i]) - ord("A") + 10

    result += n * 16 ** (len(s) - i - 1)

print(result)
