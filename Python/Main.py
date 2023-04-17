from ChessFunctions import *

tahta = [[None for i in range(8)] for j in range(8)]

tas_secili_mi = False
sah_mi = False
hamle_sayisi = 0
miktar = 0
sah_ceken_taslar = []
takım_hamle = []
secilen_tas_poz = 0
sahken_hamle = []

window = True

tahta_olustur()
taslari_yerlestir()
pozisyonlari_belirle(tahta)

while window:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not sah_mi:
                if not tas_secili_mi:
                    tas_secili_mi, secilen_tas_poz = tas_kontrol_et(tahta)
                else:
                    tas_secili_mi, miktar = secili_tas_kontrol_et(secilen_tas_poz, tahta)
                    hamle_sayisi += miktar
                    sah_mi, sah_ceken_taslar, takım_hamle = sah_kontrol(tahta)
            else:
                if not tas_secili_mi:
                    tas_secili_mi, secilen_tas_poz, sahken_hamle = sah_tas_kontrol(tahta, sah_ceken_taslar, takım_hamle)
                else:
                    tas_secili_mi, miktar = secili_sah_tas_kontrol(secilen_tas_poz, tahta, sahken_hamle)
                    hamle_sayisi += miktar
    miktar = 0
    pygame.display.update()

pygame.quit()
quit()
