import time
tic = time.perf_counter()
file = open('cvicenie1data.txt', 'r')
number_of_lines = file.readline()
number_of_nums = file.readline()
sum_of_lines = 0
while next_line := file.readline():
    next_line = next_line.split()
    next_line = [eval(i) for i in next_line]
    best_can = [0, 1]
    y = 100000000000000
    for i in range(int(number_of_nums)):
        for j in range(int(number_of_nums)):
            if j == i:
                continue
            x = next_line[i] + next_line[j]
            if abs(x) < abs(y):
                if sum_of_lines < 0 and x < 3280:
                    continue
                if sum_of_lines > 1415 and x > -1500:
                    continue
                best_can[0] = i
                best_can[1] = j
                y = x
    sum_of_lines += next_line[best_can[0]]
    sum_of_lines += next_line[best_can[1]]
toc = time.perf_counter()
print("Čas: " + str(toc - tic))
print("Súčet: " + str(sum_of_lines))
