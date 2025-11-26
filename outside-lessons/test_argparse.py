import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Expense Tracker CLI')

    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--amount', type=float, required=True)

    args = parser.parse_args()
    print("What argparse understood: ")
    print(f"Command: {args.command}")
    print(f"Description: {args.description}")
    print(f"Amount: {args.amount}")

if __name__ == "__main__":
    main()