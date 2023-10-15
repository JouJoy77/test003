"""
Написать функцию, возвращающую N первых “счастливых” автобусных билетов.
В автобусном билете 6 цифр. Будем подразумевать, что любой автобусный билет имеет такую длину
Минимальный подходящий номер - 001001
Максимальный подходящий номер - 999999
Можно подразумевать, что 001001 = 1001 и возврщать число в качестве номера,
но для удобства при выводе я решил конкатенировать нули
"""

LEN_OF_TICKET_NUMBER = 6


def sum_of_digits(n):
    """Get the sum of the digits of a number."""
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def is_lucky(num):
    """Check if the ticket is lucky."""
    first_part = num // 1000
    second_part = num % 1000
    return sum_of_digits(first_part) == sum_of_digits(second_part)


def generate_lucky_tickets(N):
    """Generate the first N lucky tickets."""
    tickets = []
    for num in range(1001, 1000000):
        if is_lucky(num):
            N -= 1
            num_as_str = str(num)
            num_as_str = ''.join(
                ['0' for _ in range(LEN_OF_TICKET_NUMBER -
                                    len(num_as_str))]+list(num_as_str)
            )
            tickets.append(num_as_str)
        if N == 0:
            break
    return tickets


if __name__ == "__main__":
    N = 10000
    lucky_tickets = generate_lucky_tickets(N)
    print(lucky_tickets)
