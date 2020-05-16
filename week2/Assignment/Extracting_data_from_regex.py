import re

if __name__ == '__main__':
    file = open('regex_sum_544321.txt')
    sum = 0
    for line in file:
        temp = line.rstrip()
        temp = re.findall('[0-9]+', temp)
        if len(temp) > 0:
            for w in temp:
                sum += int(w)

    print('The sum for the sample text above is %d\n' % sum)

#Ans
#The sum for the sample text above is 372643