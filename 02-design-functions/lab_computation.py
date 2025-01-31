
def add_numbers(a, b):
    c = a + b
    print("Summan av dessa är: " + c)


def double_nums(nums):
    for n in nums:
        if type(n) == int:
            doubled_num = n * 2
            print("Nummer: ", doubled_num)
        else:
            print("Kan endast dubbla en sträng")


def alert(message):
    for char in message:
        print(char.upper())


def show_numbers(num_list):
    for num in num_list:
        print("Tal:", num)

def reverse_string(string):
    rev_string = string[::-1]
    print("Omvänd sträng: ", rev_string)


def main():
    num1 = int(input("Ange ett nummer: "))
    num2 = int(input("Ange ett annat nummer: "))
    add_numbers(num1, num2)

    measurements1 = [1, 2, 3, 4, 5]
    measurements2 = [10, 20, 30, 40]
    double_nums(measurements1)
    alert("hello")
    show_numbers(measurements2)
    message = input("Mata in en sträng: ")
    reverse_string(message)


# koden i denna if-statement körs endast när filen kallas som ett
# skript, och inte om den importeras
if __name__ == '__main__':
    main()
