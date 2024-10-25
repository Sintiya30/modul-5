#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:33:46 2024

@author: adesintia
"""

def convert_grade(grade):
    grades = {'A': 4.0, 'A-': 3.75, 'B+': 3.5, 'B': 3.0, 'B-': 2.75, 'C': 2.0, 'C-': 1.75, 'D': 1.50, 'E': 1.25}
    return grades.get(grade, None)

def main():
    total, count = 0, 0

    while True:
        grade = input("Masukkan Nilai: ")
        if grade.lower() == '' :
            break
        grade_value = convert_grade(grade)
        if grade_value is not None:
            print(f"nilai: {grade_value}")
            total += grade_value
            count += 1
        else:
            print(f"Kategori huruf '{grade}' tidak valid dan akan diabaikan.")

    if count:
        print(f"Rata-ratanya adalah: {total / count:.2f}")
    else:
        print("Tidak ada nilai yang valid dimasukkan.")

main()

