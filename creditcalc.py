import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=['annuity', 'diff'])
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()
arg_list = [args.type, args.principal, args.periods, args.interest, args.payment]
if args.principal is not None and args.principal < 0 or \
        args.periods is not None and args.periods < 0 or \
        args.interest is None or args.interest < 0 or \
        args.type is None or \
        args.payment is not None and args.payment < 0:
    print('Incorrect parameters.')
else:
    if len(arg_list) != 5 or args.type == 'diff' and args.payment is not None:
        print('Incorrect parameters.')
    else:
        interest = args.interest / 12 / 100
        if args.type == 'annuity':
            if args.principal is not None and args.payment is not None and args.periods is None:
                periods = math.ceil(math.log(args.payment / (args.payment - interest * args.principal), interest + 1))
                if periods < 12:
                    print(f'You number of months = {periods}!')
                else:
                    periods_years = int(periods / 12)
                    print(f'Your number of years  = {periods_years}!')
                overpayment = periods * args.payment - args.principal
                print(f'Overpayment = {overpayment}')
            if args.periods is not None and args. principal is not None and args.payment is None:
                payment = math.ceil(float(args.principal * (interest * pow(1 + interest, args.periods) / (pow(1 + interest, args.periods) - 1))))
                print(f'Your annuity payment = {payment}!')
                overpayment = args.periods * payment - args.principal
                print(f'Overpayment = {overpayment}')
            if args.periods is not None and args.payment is not None and args.principal is None:
                principal = math.ceil(float(args.payment / ((interest * pow(1 + interest, args.periods)) / (pow(1 + interest, args.periods) - 1))))
                print(f'Your loan principal = {principal}!')
                overpayment = args.periods * args.payment - principal
                print(f'Overpayment = {overpayment}')
        if args.type == 'diff' and args.periods is not None and args.principal is not None:
            summ = 0
            for i in range(1, args.periods + 1):
                month_th = math.ceil(float((args.principal / args.periods) + interest * (args.principal - (args.principal * (i - 1)) / args.periods)))
                print(f'Month {i}: payment is {month_th}')
                i += 1
                summ = summ + month_th
            overpayment = summ - args.principal
            print(f'Overpayment = {overpayment}')
