# Contains helper functions for your apps!
from os import listdir, remove

# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'
def check_for_and_del_io_files():
    # Your code goes here.
    import os
    names = os.listdir()
    if 'currency_pair.txt' in names:
        os.remove('currency_pair.txt')
    if 'currency_pair_history.csv' in names:
        os.remove('currency_pair_history.csv')
    if 'trade_order.p' in names:
        os.remove('trade_order.p')
    # pass # nothing gets returned by this function, so end it with 'pass'.