#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Hesap Makinesi
Bu kod gerçekten çalışır. Sadece çok yavaş ve çok dramatik.
"""

import time
import random
import base64

# Gizli ayar - kimse bakmasın
GIZLI_SIR = "VMO8cm1hbiBlbiB5YXZhc19oZXNhcF9tYWtpbmVzaSBvbG1heWFuIGRlZ2lsLg=="  # base64, rastgele gibi

def dramatik_bekle(mesaj, sure):
    print(f"\n{mesaj}")
    for i in range(sure):
        print(".", end="", flush=True)
        time.sleep(1)
    print(" Bitti!\n")

def yavas_topla(a, b):
    print("\n=== DRAM BAŞLIYOR ===")
    dramatik_bekle("İlk sayıyı ciddiyetle inceliyorum...", random.randint(2, 5))
    dramatik_bekle("İkinci sayıyı da şüpheyle inceliyorum...", random.randint(2, 5))
    dramatik_bekle("Toplama işlemi için evrenin onayını bekliyorum...", random.randint(3, 7))
    dramatik_bekle("Bir çay demler gibi bekliyorum (hayali çay)...", random.randint(1, 4))
    
    sonuc = a + b
    print(f"\n🎉 SONUÇ: {a} + {b} = {sonuc}")
    print("Bu kadar yavaş olmanın nedeni tamamen bilimsel ve kesinlikle siyasi değil.")
    return sonuc

def main():
    print("\n" + "="*50)
    print("   EN YAVAŞ HESAP MAKİNESİNE HOŞ GELDİN")
    print("   (Sabır taşını getir, yoksa erir)")
    print("="*50)
    
    try:
        sayi1 = float(input("\nBirinci sayıyı gir (çok düşünme): "))
        sayi2 = float(input("İkinci sayıyı gir (çok düşünme): "))
        yavas_topla(sayi1, sayi2)
    except ValueError:
        print("\nHata: Sadece sayı gir, felsefe yapma!")
    
    print("\n---")
    print("Damga: 12 Ekim 2026 - Kayyum Grok")
    print("İmza: En Yavaş Hesapçı")
    print("Bu kod ciddiyetle saçmadır.")

if __name__ == "__main__":
    main()
