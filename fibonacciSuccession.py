def fibonacci_succession(sprint: int) -> str:
    count = 0
    fibonacci = ''
    succession = 0
    lastSuccession = 0
    while(count < sprint):
        if count == 0:
            succession = 0
            fibonacci = str(succession)
        elif count == 1:
            lastSuccession = 1
            fibonacci = fibonacci+","+str(lastSuccession)
        else:
            current = succession + lastSuccession
            fibonacci = fibonacci+","+str(current)
            succession = lastSuccession
            lastSuccession = current
        count += 1

    return fibonacci


result = fibonacci_succession(18)
