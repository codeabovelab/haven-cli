"""Tests output."""

from lib.tabulate import tabulate

def main():

    table = [["Sun",696000,1989100000],["Earth",6371,5973.6], ["Moon",1737,73.5],["Mars",3390,641.85]]
    print(tabulate(table))

if __name__ == '__main__':
    main()