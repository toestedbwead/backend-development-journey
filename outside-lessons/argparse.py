# argparse crash course

import argparse 
# ^ gives all the tools to parse command-line arguments professionally 

def main():
    parser =  argparse.ArgumentParser(description='Expense Tracker CLI')
    # ^ creates the main parser - it understands commands. description appears when users run --help


    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    # ^ creates sub-commands like: add, list, delete, summary

    # dest='command' means: store the chosen command in args.command
    # help : shows available commands in help text



    # add command

    add_parser = subparsers.add_parser('add', help='Add a new expense')
    # ^ creates the add command parser - handle user type 'add'


    add_parser.add_argument('--description',required=True, help='Expense description')
    # ^ adds a flag --description to the add command
    # required=True : user MUST provide this
    # help : text shown in help

    add_parser.add_argument('--amount', type=float, required=True, help='Expense amount')
    # ^ another flag --amount
    # type=float : automatically converts input to decimal number
    # required=True : must be provided


    # list command
    list_parser = subparsers.add_parser('list', help='List all expenses')
    # ^ simple command, no arguments needed. just shows all expenses.


    # delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')

    delete_parser.add_argument('--id', type=int, required=True, help='Expense ID to delete')

    # ^ delete command with --id flag
    # type=int : automatically converts to integer

    # summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')

    summary_parser.add_argument('--month', type=int, help='Filter by month (1-12)')

    # ^summary command with optional --month flag
    # no required=True so it's optional


    args = parser.parse_args()
    # ^ python automatically
    # parses all the commands and flags, 
    # validates required arguments
    # converts types (strings -> float/int)
    # stores everything in args


'''
after parse_args():
1. args.command - which command was called('add','list', etc)
2. args.description - the description string (for 'add' command)
3. args.amount - the amount as float (for 'add' command)
4. args.id - the id as integer (for delete command)
5. args.month - the month as integer or None (for 'summary' command)
'''


