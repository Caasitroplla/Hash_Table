from src.table import Table

def main():
    table = Table()
    table.add('awsome', 'This is the hashed version of the word')
    print(table.get('awsome'))
    print(table)
    table.delete('awsome')
    print(table)

if __name__ == '__main__':
    main()