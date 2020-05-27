import csv
import getInput
import plot

testlist = [
    'monobit_test',
    'frequency_within_block_test',
    'runs_test',
    'longest_run_ones_in_a_block_test',
    'binary_matrix_rank_test',
    'dft_test',
    'non_overlapping_template_matching_test',
    'overlapping_template_matching_test',
    'maurers_universal_test',
    'linear_complexity_test',
    'serial_test',
    'approximate_entropy_test',
    'cumulative_sums_test',
    'random_excursion_test',
    'random_excursion_variant_test'
]

# Get data set
# getInput.getInput()


def line2bits(line):
    line = ''.join([c for c in line if c not in [' ', '\t', '\n']])
    line = ''.join(["{:04b}".format(int(c,16)) for c in line])
    return line


def main():
    input = "input.txt"  # input file containing bit strings

    NUM_TEST = 15

    # Write output to csv files
    fieldnames = [None] * NUM_TEST  # fieldnames associating with outputs of each test
    fieldnames[0] = ['n', 'zeroes count', 'ones count', 'abs(ones-zeroes)', 'p-value', 'success']
    fieldnames[1] = ['n', 'chi_sq', 'p-value', 'success']
    fieldnames[2] = ['n', 'zeroes count', 'ones count', 'one_prop', 'vobs', 'p-value', 'success']
    fieldnames[3] = ['n', 'chi_sq', 'p-value', 'success']
    fieldnames[4] = ['n', 'M', 'Q', 'N', 'FM', "FMM", 'chi_sq', 'p-value', 'success']
    fieldnames[5] = ['n', 'N0', 'N1', 'd', 'p-value', 'success']
    fieldnames[6] = ['n', 'mu', 'sigma', 'chi_sq', 'p-value', 'success']
    fieldnames[7] = ['n', 'template', 'M', 'N', 'K', 'model', 'v', 'lambda', 'eta', 'chi_sq', 'p-value', 'success']
    fieldnames[8] = ['n', '#blocks', 'L', 'K', 'Q', 'sigma', 'p-value', 'success']
    fieldnames[9] = ['n', 'M', 'N', 'K', 'v', 'mu', 'chi_sq', 'p-value', 'success']
    fieldnames[10] = ['n', 'psi_sq_m', 'psi_sq_mm1', 'psi_sq_mm2', 'delta1', 'delta2', 'p1', 'p2', 'p_average',
                      'success']
    fieldnames[11] = ['n', 'appen_m', 'chi_sq', 'p-value', 'success']
    fieldnames[12] = ['n', 'p_forward', 'p_backward', 'success']
    fieldnames[13] = ['n', 'J', 'chi_sq', 'p-value', 'p_average', 'success']
    fieldnames[14] = ['n', 'J', 'count', 'p-value', 'p_average', 'success']

    fo = [None] * NUM_TEST  # list of output file

    output = [None] * NUM_TEST  # output file name
    writer = [None] * NUM_TEST  # writers of csv file

    source = [None] * NUM_TEST

    for i in range(NUM_TEST):
        if i < 9:
            output[i] = "results/result_0" + str(i + 1) + "_" + testlist[i] + ".csv"
        else:
            output[i] = "results/result_" + str(i + 1) + "_" + testlist[i] + ".csv"

        if fieldnames[i] is not None:
            fo[i] = open(output[i], mode="w+")
            writer[i] = csv.DictWriter(fo[i], fieldnames=fieldnames[i])
            writer[i].writeheader()

    # fi = open(input, "r") # input file

    result = [None] * NUM_TEST

    for i in range(NUM_TEST):
        total_count = 0
        success_count = 0
        p_average = 0.0
        # Get corresponding .py test file
        if i < 9:
            testFile = __import__("0" + str(i + 1) + "_" + testlist[i])
        else:
            testFile = __import__(str(i + 1) + "_" + testlist[i])

        fi = open(input, "r")  # input file

        '''
        Handle special cases: concatenate multiple lines into one to obtain 
        input with enough bit length for each test
        '''
        # binary_matrix_rank_test
        if i == 4:

            bits = ''
            for line in fi:
                bits += line2bits(line)

                if len(bits) < 38912 * 2:  # recommended input size
                    continue

                else:

                    total_count += 1
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
            bits = ''

        # overlapping_template_matching_test            
        elif i == 7:
            bits = ''
            for line in fi:
                bits += line2bits(line)
                if len(bits) < 1028016 * 2:  # recommended input size
                    continue
                else:
                    total_count += 1
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
            bits = ''

        # maurers_universal_test
        elif i == 8:
            bits = ''
            for line in fi:
                bits += line2bits(line)
                if len(bits) < 387840 * 2:  # recommended input size
                    continue
                else:
                    total_count += 1
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
            bits = ''

        # linear_complexity_test
        elif i == 9:

            bits = ''
            for line in fi:
                bits += line2bits(line)
                if len(bits) < 1000000:  # recommended input size
                    continue
                else:
                    total_count += 1
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
            bits = ''

        # random_excursion_test and random_excursion_variant_test
        elif i == 13 or i == 14:
            bits = ''
            for line in fi:
                bits += line2bits(line)
                if len(bits) < 1000000 * 2:  # recommended input size
                    continue
                else:
                    total_count += 1
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    if x[1] < 500:
                        x[len(x) - 1] = str(x[len(x) - 1]) + " NOT RELIABLE: J < 500"

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
            bits = ''
        else:

            for line in fi:

                total_count += 1
                if fieldnames[i] is not None:

                    bits = line2bits(line)
                    x = testFile.test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    writeDict[fieldnames[i][0]] = len(bits)

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j + 1]] = x[j]

                    writer[i].writerow(writeDict)

        success_ratio = 0
        total_average = 0
        if total_count:
            success_ratio = float(success_count) / total_count
            total_average = p_average / total_count

        writeDict = {}
        print(i, total_count)
        writeDict[fieldnames[i][len(fieldnames[i]) - 1]] = success_ratio
        writeDict[fieldnames[i][len(fieldnames[i]) - 2]] = total_average
        writer[i].writerow(writeDict)

        print("p_average = " + str(total_average))
        print("passed percentage = " + str(success_ratio))
        print("Test " + str(i + 1) + ": " + testlist[i] + " finished!")

    for i in range(13):
        print(output[i])
        print(i)
        plot.plot(output[i], i)
    print(output[4])
    print(4)
    plot.plot(output[4], 4)


if __name__ == "__main__":
    main()
