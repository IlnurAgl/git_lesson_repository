import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cars", default='50')
parser.add_argument("--barbie", default='50')
parser.add_argument("--movie", default="other")
args = parser.parse_args()
move = 0
if args.movie == "football":
    move = 100
elif args.movie == "other":
    move = 50
if int(args.cars) < 0 or int(args.cars) > 100:
    args.cars = 50
if int(args.barbie) < 0 or int(args.barbie) > 100:
    args.barbie = 50
boy = int((100 - int(args.barbie) + int(args.cars) + int(move)) / 3)
girl = 100 - boy
print('boy:', boy)
print('girl:', girl)