import os
import zipfile
import itertools
import string
import time
import shutil

start = time.perf_counter()


def clear():
    os.system('clear')


def crack(zip, pwd, lines, columns):
    try:
        zip.extractall(pwd=str.encode(pwd))
        for _ in range(lines // 2):
            print('')
        print(f'Success: Password is {pwd}'.center(columns))
        print(f'{time.perf_counter() - start} seconds ...'.center(columns))
        return pwd
    except:
        pass


def simple_bruteforce(path):
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    zip_file = zipfile.ZipFile(path)
    ascii_pool = string.ascii_letters + string.digits + string.punctuation
    for i in range(3, 10):
        for j in map(''.join, itertools.product(ascii_pool, repeat=i)):
            for _ in range(lines//2):
                print('')
            print(j.center(columns))
            clear()
            if crack(zip_file, j, lines, columns) == j:
                return j


def dictionary_attack(path, pwd_list):
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    zip_file = zipfile.ZipFile(path)
    passwords = open(pwd_list)
    for line in passwords.readlines():
        pwd = line.strip("\n")
        for _ in range(lines // 2):
            print('')
        print(pwd.center(columns))
        clear()
        if crack(zip_file, pwd, lines, columns) == pwd:
            return pwd
            
