#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:26:18 2024

@author: adesintia
"""

def hitung_tiket(umur):
    if umur <= 2:
        return 0 # Gratis
    elif 3 <= umur <= 12:
        return 14
    elif umur >= 65:
        return 18
    else:
        return 23  # Normal

def main():
    total_harga = 0
    
    while True:
        try:
            umur = int(input("Masukkan umur pengunjung (atau ketik -1 untuk keluar): "))
            if umur == -1:
                break
            
            harga = hitung_tiket(umur)
            total_harga += harga
            
            print(f"Harga tiket untuk umur {umur} tahun: ${harga}")
        
        except ValueError:
            print("Input tidak valid. Mohon masukkan umur yang benar.")

    if total_harga > 0:
        print(f"\nTotal keseluruhan harga tiket: ${total_harga}")
        
        while True:
            try:
                pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: $"))
                if pembayaran < total_harga:
                    print("Uang yang dibayarkan kurang. Mohon masukkan jumlah yang cukup.")
                else:
                    kembalian = pembayaran - total_harga
                    print(f"Kembalian Anda: ${kembalian:.2f}")
                    break
            except ValueError:
                print("Input tidak valid. Mohon masukkan jumlah uang yang benar.")

if __name__ == "__main__":
    main()