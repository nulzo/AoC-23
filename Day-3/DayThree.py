import re
from collections import defaultdict


def one():
    with open("./testData.txt", "r") as file:
        lines = file.read().splitlines()

        ############################## PART 1 ##############################
        total_sum = 0
        concat_output = ''
        for row, line in enumerate(lines):
            line += '.'
            for col, element in enumerate(line):
                if element.isdigit():
                    concat_output += element
                elif concat_output:
                    if any(lines[row_i][col_i] not in '.0123456789' for row_i in (range(max(0, row-1), min(len(lines), row+2)))
                           for col_i in range(max(0, col-1-len(concat_output)), min(len(line)-1, col+1))):
                        total_sum += int(concat_output)
                    concat_output = ''
        # print("Part 1:", total_sum)

        ############################## PART 2 ##############################
        coordinates = {}
        concat_output = ''
        for row, line in enumerate(lines):
            line += '.'
            for col, element in enumerate(line):
                if element.isdigit():
                    concat_output += element
                elif concat_output:
                    for row_i in (range(max(0, row-1), min(len(lines), row+2))):
                        for col_i in range(max(0, col-1-len(concat_output)), min(len(line)-1, col+1)):
                            if lines[row_i][col_i] == '*' and (row_i, col_i) not in coordinates:
                                coordinates[(row_i, col_i)] = [
                                    int(concat_output)]
                            elif lines[row_i][col_i] == '*' and (row_i, col_i) in coordinates:
                                coordinates[(row_i, col_i)
                                            ] += [int(concat_output)]
                    concat_output = ''
        total = sum(ab[0]*ab[1] for ab in coordinates.values() if len(ab) == 2)
        print(total)
        # print("Part 2:", p2)
        # s = file.read()
        # f = s.splitlines()
        # x = ''.join(f).split('.')
        # lines = []
        # y = [i for i in x if i.isdigit()]
        # for i in y:
        #     lines.append((s.find(i), i))
        # for i in lines:
        #     valid = False
        #     for k in range(len(i[1])):
        #         # print(s[i[0]+k])
        #         try:
        # if f[s[i[0]+k]-1][s[i[0]+k]-1] != '.' and not f[row-1][col-1].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row][col-1] != '.' and not f[row-1][col].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row+1][col-1] != '.' and not f[row-1][col+1].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row-1][col] != '.' and not f[row][col-1].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row][col] != '.' and not f[row][col].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row+1][col] != '.' and not f[row][col+1].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row-1][col+1] != '.' and not f[row+1][col-1].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row][col+1] != '.' and not f[row+1][col].isdigit():
        #                 valid = True
        #         except:
        #             continue
        #         try:
        #             if f[row+1][col+1] != '.' and (not f[row+1][col+1].isdigit()):
        #                 valid = True
        #         except:
        #             print()
        #         if valid:
        #             print(i)
        # for row in range(len(f)):
        #     for col in range(len(f)):
        #         if f[row][col].isdigit():
        #             valid = False
        #             try:
        #                 if f[row-1][col-1] != '.' and not f[row-1][col-1].isdigit():
        #                     valid = True
        #                 if f[row][col-1] != '.' and not f[row-1][col].isdigit():
        #                     valid = True
        #                 if f[row+1][col-1] != '.' and not f[row-1][col+1].isdigit():
        #                     valid = True
        #                 if f[row-1][col] != '.' and not f[row][col-1].isdigit():
        #                     valid = True
        #                 if f[row][col] != '.' and not f[row][col].isdigit():
        #                     valid = True
        #                 if f[row+1][col] != '.' and not f[row][col+1].isdigit():
        #                     valid = True
        #                 if f[row-1][col+1] != '.' and not f[row+1][col-1].isdigit():
        #                     valid = True
        #                 if f[row][col+1] != '.' and not f[row+1][col].isdigit():
        #                     valid = True
        #                 if f[row+1][col+1] != '.' and (not f[row+1][col+1].isdigit()):
        #                     valid = True
        #                 if valid:
        #                     print(i)
        #             except:
        #                 print("OUT")
        #     print()
        # for row in range(len(f)):
        #     for col in range(len(f)):
        #         if f[row][col].isdigit():
        #             valid = False
        #             if row != 0 and row != len(f) - 1 and col != 0 and col != len(f) - 1:
        #                 try:
        #                     if f[row-1][col-1] != '.':
        #                         valid = True
        #                     if f[row][col-1] != '.':
        #                         valid = True
        #                     if f[row+1][col-1] != '.':
        #                         valid = True
        #                     if f[row-1][col] != '.':
        #                         valid = True
        #                     if f[row][col] != '.':
        #                         valid = True
        #                     if f[row+1][col] != '.':
        #                         valid = True
        #                     if f[row-1][col+1] != '.':
        #                         valid = True
        #                     if f[row][col+1] != '.':
        #                         valid = True
        #                     if f[row+1][col+1] != '.':
        #                         valid = True
        #                 except:
        #                     print("OUT")
        #             elif row == 0 and col == 0:
        #                 try:
        #                     if f[row-1][col-1] != '.':
        #                         valid = True
        #                     if f[row][col-1] != '.':
        #                         valid = True
        #                     if f[row+1][col-1] != '.':
        #                         valid = True
        #                     if f[row-1][col] != '.':
        #                         valid = True
        #                     if f[row][col] != '.':
        #                         valid = True
        #                     if f[row+1][col] != '.':
        #                         valid = True
        #                     if f[row-1][col+1] != '.':
        #                         valid = True
        #                     if f[row][col+1] != '.':
        #                         valid = True
        #                     if f[row+1][col+1] != '.':
        #                         valid = True
        #                 except:
        #                     print("OUT")
        # if valid:
        #     print(f[row][col])
        # print('')


one()
