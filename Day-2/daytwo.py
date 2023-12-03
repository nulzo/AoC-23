import re


def one():
    with open("./data.txt", "r") as file:
        f = file.read().splitlines()
        d = {"red": 12, "green": 13, "blue": 14}
        t = 0
        for line in f:
            mapped = re.split(': |;', line)
            u = mapped[0]
            x = [x.strip().split(',') for x in mapped[1:]]
            valid = True
            for i in x:
                for r in i:
                    v = r.strip().split(' ')
                    thresh = d.get(v[1])
                    if int(v[0]) > thresh:
                        valid = False
            if valid:
                t += int(u.strip().split(' ')[1])
        print(t)


def two():
    with open("./data.txt", "r") as file:
        f = file.read().splitlines()
        t = 0
        for line in f:
            mapped = re.split(': |;', line)
            x = [x.strip().split(',') for x in mapped[1:]]
            max_r = 0
            max_g = 0
            max_b = 0
            for v in x:
                for i in v:
                    n = i.strip().split(' ')
                    if n[1] == 'blue' and int(n[0]) > max_b:
                        max_b = int(n[0])
                    if n[1] == 'green' and int(n[0]) > max_g:
                        max_g = int(n[0])
                    if n[1] == 'red' and int(n[0]) > max_r:
                        max_r = int(n[0])
            t += max_r * max_b * max_g
        print(t)


two()
