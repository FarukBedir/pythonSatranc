import pygame
from Tas import *

pygame.init()

beyaz = (255, 255, 255)
siyah = (0, 0, 0)
pencere = pygame.display.set_mode((800, 800))
square = pencere.get_width() / 8


#
def tahta_olustur():
    pygame.display.set_caption("Chess")
    pencere.fill(siyah)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(pencere, beyaz, (square * i, square * j, square, square))


#
def taslari_yerlestir():
    s_piyon = pygame.image.load('siyahpiyon.png')
    s_piyon = pygame.transform.scale(s_piyon, (square, square))
    b_piyon = pygame.image.load('beyazpiyon.png')
    b_piyon = pygame.transform.scale(b_piyon, (square, square))
    s_sah = pygame.image.load('siyahşah.png')
    s_sah = pygame.transform.scale(s_sah, (square, square))
    s_vezir = pygame.image.load('siyahvezir.png')
    s_vezir = pygame.transform.scale(s_vezir, (square, square))
    b_sah = pygame.image.load('beyazşah.png')
    b_sah = pygame.transform.scale(b_sah, (square, square))
    b_vezir = pygame.image.load('beyazvezir.png')
    b_vezir = pygame.transform.scale(b_vezir, (square, square))

    for i in range(8):
        pencere.blit(s_piyon, (square * i, square))
        if i == 2 or i == 5:
            resim = pygame.image.load('siyahfil.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, (i * square, 0))
        if i == 1 or i == 6:
            resim = pygame.image.load('siyahat.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, (i * square, 0))
        if i == 0 or i == 7:
            resim = pygame.image.load('siyahkale.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, ((i * square), 0))
    pencere.blit(s_sah, (4 * square, 0))
    pencere.blit(s_vezir, (3 * square, 0))

    for i in range(8):
        pencere.blit(b_piyon, (square * i, square * 6))
        if i == 2 or i == 5:
            resim = pygame.image.load('beyazfil.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, (i * square, square * 7))
        if i == 1 or i == 6:
            resim = pygame.image.load('beyazat.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, (i * square, square * 7))
        if i == 0 or i == 7:
            resim = pygame.image.load('beyazkale.png')
            resim = pygame.transform.scale(resim, (square, square))
            pencere.blit(resim, ((i * square), square * 7))
    pencere.blit(b_sah, (4 * square, square * 7))
    pencere.blit(b_vezir, (3 * square, square * 7))


#
def pozisyonlari_belirle(tahta):
    s_at_1, s_at_2 = At('siyah', [0, 1], 'siyahat.png'), At('siyah', [0, 6], 'siyahat.png')
    s_kale_1, s_kale_2 = Kale('siyah', [0, 0], 'siyahkale.png'), Kale('siyah', [0, 7], 'siyahkale.png')
    s_fil_1, s_fil_2 = Fil('siyah', [0, 2], 'siyahfil.png'), Fil('siyah', [0, 5], 'siyahfil.png')
    s_vezir_1 = Vezir('siyah', [0, 3], 'siyahvezir.png')
    s_sah_1 = Sah('siyah', [0, 4], 'siyahşah.png')
    b_at_1, b_at_2 = At('beyaz', [7, 1], 'beyazat.png'), At('beyaz', [7, 6], 'beyazat.png')
    b_kale_1, b_kale_2 = Kale('beyaz', [7, 0], 'beyazkale.png'), Kale('beyaz', [7, 7], 'beyazkale.png')
    b_fil_1, b_fil_2 = Fil('beyaz', [7, 2], 'beyazfil.png'), Fil('beyaz', [7, 5], 'beyazfil.png')
    b_vezir_1 = Vezir('beyaz', [7, 3], 'beyazvezir.png')
    b_sah_1 = Sah('beyaz', [7, 4], 'beyazşah.png')
    for i in range(8):
        tahta[1][i] = Piyon('siyah', [1, i], 'siyahpiyon.png')
    for i in range(8):
        tahta[6][i] = Piyon('beyaz', [6, i], 'beyazpiyon.png')
    tahta[0] = [s_kale_1, s_at_1, s_fil_1, s_vezir_1, s_sah_1, s_fil_2, s_at_2, s_kale_2]
    tahta[7] = [b_kale_1, b_at_1, b_fil_1, b_vezir_1, b_sah_1, b_fil_2, b_at_2, b_kale_2]
    for i in range(8):
        for j in range(6):
            if j == 0 or j == 1:
                pass
            else:
                tahta[j][i] = None


#
def tas_kontrol_et(tahta):
    y, x = pygame.mouse.get_pos()
    x = int(x / 100)
    y = int(y / 100)
    if isinstance(tahta[x][y], Piyon):
        arr = piyon_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    elif isinstance(tahta[x][y], At):
        arr = at_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    elif isinstance(tahta[x][y], Vezir):
        arr = vezir_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    elif isinstance(tahta[x][y], Kale):
        arr = kale_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    elif isinstance(tahta[x][y], Fil):
        arr = fil_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    elif isinstance(tahta[x][y], Sah):
        arr = sah_hamle_kontrol_et(tahta[x][y], tahta)
        if len(arr):
            pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
            sprite = pygame.image.load(tahta[x][y].resim)
            sprite = pygame.transform.scale(sprite, (square, square))
            pencere.blit(sprite, (y * square, x * square))
            for i in range(len(arr)):
                a = arr[i][0]
                b = arr[i][1]
                if tahta[a][b] is not None:
                    ye_vurgula(tahta[a][b])
                else:
                    bos_vurgula([a, b])
        else:
            return False, [-1, -1]
    return True, [x, y]


#
def secili_tas_kontrol_et(poz, tahta):
    arr = []
    y, x = pygame.mouse.get_pos()
    x = int(x / 100)
    y = int(y / 100)
    if isinstance(tahta[poz[0]][poz[1]], Piyon):
        arr = piyon_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    elif isinstance(tahta[poz[0]][poz[1]], At):
        arr = at_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    elif isinstance(tahta[poz[0]][poz[1]], Vezir):
        arr = vezir_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    elif isinstance(tahta[poz[0]][poz[1]], Kale):
        arr = kale_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    elif isinstance(tahta[poz[0]][poz[1]], Fil):
        arr = fil_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    elif isinstance(tahta[poz[0]][poz[1]], Sah):
        arr = sah_hamle_kontrol_et(tahta[poz[0]][poz[1]], tahta)
    if tahta[x][y] is not None:
        if tahta[x][y].pozisyon in arr:
            tas_sil(tahta, [x, y])
            tahta[poz[0]][poz[1]].pozisyon = [x, y]
            tahta[x][y] = tahta[poz[0]][poz[1]]
            tahta[poz[0]][poz[1]] = None
            tekrar_ciz(tahta)
            return False, 1
        else:
            tekrar_ciz(tahta)
            return False, 1
    else:
        tahta[poz[0]][poz[1]].pozisyon = [x, y]
        tahta[x][y] = tahta[poz[0]][poz[1]]
        tahta[poz[0]][poz[1]] = None
        tekrar_ciz(tahta)
        return False, 1


#
def tahta_limiti(pozisyon):
    if -1 < pozisyon[0] < 8 and 8 > pozisyon[1] > -1:
        return True
    else:
        return False


#
def bos_vurgula(poz):
    x = poz[0]
    y = poz[1]
    pygame.draw.rect(pencere, (50, 205, 50), (square * y, square * x, square, square))


#
def ye_vurgula(tas):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    pygame.draw.rect(pencere, (255, 0, 255), (square * y, square * x, square, square))
    sprite = pygame.image.load(tas.resim)
    sprite = pygame.transform.scale(sprite, (square, square))
    pencere.blit(sprite, ((y * square), square * x))


#
def sah_kontrol(tahta):
    arr_s = []
    arr_b = []
    taslar = []
    beyaz_sah_poz = []
    siyah_sah_poz = []
    for i in range(8):
        for j in range(8):
            if tahta[i][j] is not None:
                if isinstance(tahta[i][j], Sah):
                    if tahta[i][j].takim == 'beyaz':
                        beyaz_sah_poz = tahta[i][j].pozisyon
                    else:
                        siyah_sah_poz = tahta[i][j].pozisyon
    for i in range(8):
        for j in range(8):
            if tahta[i][j] is not None:
                if not isinstance(tahta[i][j], Sah):
                    if tahta[i][j].takim == 'siyah':
                        if isinstance(tahta[i][j], Piyon):
                            arr_s += piyon_hamle_kontrol_et(tahta[i][j], tahta)
                            if beyaz_sah_poz in arr_s:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], At):
                            arr_s += at_hamle_kontrol_et(tahta[i][j], tahta)
                            if beyaz_sah_poz in arr_s:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Vezir):
                            arr_s += vezir_hamle_kontrol_et(tahta[i][j], tahta)
                            if beyaz_sah_poz in arr_s:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Fil):
                            arr_s += fil_hamle_kontrol_et(tahta[i][j], tahta)
                            if beyaz_sah_poz in arr_s:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Kale):
                            arr_s += kale_hamle_kontrol_et(tahta[i][j], tahta)
                            if beyaz_sah_poz in arr_s:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        for a in range(len(arr_s)):
                            if beyaz_sah_poz == arr_s[a]:
                                ye_vurgula(tahta[beyaz_sah_poz[0]][beyaz_sah_poz[1]])
                                tahta[beyaz_sah_poz[0]][beyaz_sah_poz[1]].tehlike = True
                                return True, taslar, arr_s
                    else:
                        if isinstance(tahta[i][j], Piyon):
                            arr_b += piyon_hamle_kontrol_et(tahta[i][j], tahta)
                            if siyah_sah_poz in arr_b:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], At):
                            arr_b += at_hamle_kontrol_et(tahta[i][j], tahta)
                            if siyah_sah_poz in arr_b:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Vezir):
                            arr_b += vezir_hamle_kontrol_et(tahta[i][j], tahta)
                            if siyah_sah_poz in arr_b:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Fil):
                            arr_b += fil_hamle_kontrol_et(tahta[i][j], tahta)
                            if siyah_sah_poz in arr_b:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        elif isinstance(tahta[i][j], Kale):
                            arr_b += kale_hamle_kontrol_et(tahta[i][j], tahta)
                            if siyah_sah_poz in arr_b:
                                tahta[i][j].sah_cekiyor_mu = True
                                taslar.append(tahta[i][j])
                        for a in range(len(arr_b)):
                            if siyah_sah_poz == arr_b[a]:
                                ye_vurgula(tahta[siyah_sah_poz[0]][siyah_sah_poz[1]])
                                tahta[siyah_sah_poz[0]][siyah_sah_poz[1]].tehlike = True
                                return True, taslar, arr_b
    return False, taslar, arr_s


#
def piyon_hamle_kontrol_et(tas, tahta):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    arr = []
    if tas.takim == 'beyaz':
        if x == 6:
            if tahta[5][y] is None:
                arr.append([5, y])
                if tahta[4][y] is None:
                    arr.append([4, y])
        else:
            if tahta_limiti([x - 1, y]):
                if tahta[x - 1][y] is None:
                    arr.append([x - 1, y])
        if tahta_limiti([x - 1, y - 1]):
            if tahta[x - 1][y - 1] is not None:
                arr.append([x - 1, y - 1])

        if tahta_limiti([x - 1, y + 1]):
            if tahta[x - 1][y + 1] is not None:
                arr.append([x - 1, y + 1])
    else:
        for i in range(8):
            if tas.pozisyon == [1, i]:
                if tahta[2][i] is None:
                    arr.append([2, i])
                    if tahta[3][i] is None:
                        arr.append([3, i])
            else:
                if tahta_limiti([x + 1, y]):
                    if tahta[x + 1][y] is None:
                        arr.append([x + 1, y])
        if tahta_limiti([x + 1, y - 1]):
            if tahta[x + 1][y - 1] is not None:
                arr.append([x + 1, y - 1])
        if tahta_limiti([x + 1, y + 1]):
            if tahta[x + 1][y + 1] is not None:
                arr.append([x + 1, y + 1])
    return arr


#
def at_hamle_kontrol_et(tas, tahta):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    arr = []
    for i in range(-2, 3, 4):
        for j in range(-1, 2, 2):
            if tahta_limiti([x + i, y + j]):
                if tahta[x + i][y + j] is None:
                    arr.append([x + i, y + j])
                else:
                    if tahta[x + i][y + j].takim != tas.takim:
                        arr.append([x + i, y + j])
            if tahta_limiti([x + j, y + i]):
                if tahta[x + j][y + i] is None:
                    arr.append([x + j, y + i])
                else:
                    if tahta[x + j][y + i].takim != tas.takim:
                        arr.append([x + j, y + i])
    return arr


#
def vezir_hamle_kontrol_et(tas, tahta):
    arr = kale_hamle_kontrol_et(tas, tahta)
    arr2 = fil_hamle_kontrol_et(tas, tahta)
    if len(arr2):
        arr = arr + arr2
    return arr


#
def sah_hamle_kontrol_et(tas, tahta):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    arr = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not [x, y] == [x + i, y + j]:
                if tahta_limiti([x + i, y + j]):
                    if tahta[x + i][y + j] is None:
                        arr.append([x + i, y + j])
                    else:
                        if tahta[x + i][y + j].takim != tas.takim:
                            arr.append([x + i, y + j])
    return arr


#
def fil_hamle_kontrol_et(tas, tahta):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    kesili_mi_1 = False
    kesili_mi_2 = False
    kesili_mi_3 = False
    kesili_mi_4 = False
    arr = []
    for i in range(1, 8):
        while not kesili_mi_1:
            if tahta_limiti([x + i, y + i]):
                if tahta[x + i][y + i] is None:
                    arr.append([x + i, y + i])
                    break
                else:
                    if tahta[x + i][y + i].takim != tas.takim:
                        arr.append([x + i, y + i])
                        kesili_mi_1 = True
                    else:
                        kesili_mi_1 = True
            else:
                kesili_mi_1 = True
        while not kesili_mi_2:
            if tahta_limiti([x - i, y - i]):
                if tahta[x - i][y - i] is None:
                    arr.append([x - i, y - i])
                    break
                else:
                    if tahta[x - i][y - i].takim != tas.takim:
                        arr.append([x - i, y - i])
                        kesili_mi_2 = True
                    else:
                        kesili_mi_2 = True
            else:
                kesili_mi_2 = True
        while not kesili_mi_3:
            if tahta_limiti([x + i, y - i]):
                if tahta[x + i][y - i] is None:
                    arr.append([x + i, y - i])
                    break
                else:
                    if tahta[x + i][y - i].takim != tas.takim:
                        arr.append([x + i, y - i])
                        kesili_mi_3 = True
                    else:
                        kesili_mi_3 = True
            else:
                kesili_mi_3 = True
        while not kesili_mi_4:
            if tahta_limiti([x - i, y + i]):
                if tahta[x - i][y + i] is None:
                    arr.append([x - i, y + i])
                    break
                else:
                    if tahta[x - i][y + i].takim != tas.takim:
                        arr.append([x - i, y + i])
                        kesili_mi_4 = True
                    else:
                        kesili_mi_4 = True
            else:
                kesili_mi_4 = True
    return arr


#
def kale_hamle_kontrol_et(tas, tahta):
    x = tas.pozisyon[0]
    y = tas.pozisyon[1]
    kesili_mi_1 = False
    kesili_mi_2 = False
    kesili_mi_3 = False
    kesili_mi_4 = False
    arr = []
    for i in range(1, 8):
        while not kesili_mi_1:
            if tahta_limiti([x + i, y]):
                if tahta[x + i][y] is None:
                    arr.append([x + i, y])
                    break
                else:
                    if tahta[x + i][y].takim != tas.takim:
                        arr.append([x + i, y])
                        kesili_mi_1 = True
                    else:
                        kesili_mi_1 = True
            else:
                kesili_mi_1 = True
        while not kesili_mi_2:
            if tahta_limiti([x, y + i]):
                if tahta[x][y + i] is None:
                    arr.append([x, y + i])
                    break
                else:
                    if tahta[x][y + i].takim != tas.takim:
                        arr.append([x, y + i])
                        kesili_mi_2 = True
                    else:
                        kesili_mi_2 = True
            else:
                kesili_mi_2 = True
        while not kesili_mi_3:
            if tahta_limiti([x - i, y]):
                if tahta[x - i][y] is None:
                    arr.append([x - i, y])
                    break
                else:
                    if tahta[x - i][y].takim != tas.takim:
                        arr.append([x - i, y])
                        kesili_mi_3 = True
                    else:
                        kesili_mi_3 = True
            else:
                kesili_mi_3 = True
        while not kesili_mi_4:
            if tahta_limiti([x, y - i]):
                if tahta[x][y - i] is None:
                    arr.append([x, y - i])
                    break
                else:
                    if tahta[x][y - i].takim != tas.takim:
                        arr.append([x, y - i])
                        kesili_mi_4 = True
                    else:
                        kesili_mi_4 = True
            else:
                kesili_mi_4 = True
    return arr


def tur_belirle(hamle):
    if hamle % 2 == 0:
        return 'beyaz'
    else:
        return 'siyah'



#
def tekrar_ciz(tahta):
    pencere.fill(siyah)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(pencere, beyaz, (square * j, square * i, square, square))
            if tahta[i][j] is not None:
                sprite = pygame.image.load(tahta[i][j].resim)
                sprite = pygame.transform.scale(sprite, (square, square))
                pencere.blit(sprite, (j * square, i * square))


#
def tas_sil(tahta, poz):
    x = poz[0]
    y = poz[1]
    tahta[x][y] = None


def sah_tas_kontrol(tahta, taslar, hamleler):
    y, x = pygame.mouse.get_pos()
    x = int(x / 100)
    y = int(y / 100)

    sah = Tas('bos', [-1, -1], 'bos')
    kareler = []
    for i in range(8):
        for j in range(8):
            if tahta[i][j] is not None:
                if isinstance(tahta[i][j], Sah):
                    if tahta[i][j].tehlike:
                        sah = tahta[i][j]
    for i in range(len(taslar)):
        tas = taslar[i]
        poz = tas.pozisyon
        s_poz = sah.pozisyon
        if isinstance(tas, At):
            kareler += tas.pozisyon
        else:
            if s_poz[0] == poz[0]:
                for j in range(min(s_poz[1], poz[1]), max(s_poz[1], poz[1])):
                    kareler += [poz[0], j]
            elif s_poz[1] == poz[1]:
                for j in range(min(s_poz[0], poz[0]), max(s_poz[0], poz[0])):
                    kareler += [j, poz[1]]
            else:
                if poz[1] > s_poz[1] and poz[0] > s_poz[0]:
                    for j in range(s_poz[0] + 1, poz[0] + 1):
                        kareler += [j, j]
                else:
                    a = abs(poz[0] - s_poz[0])
                    if poz[0] > s_poz[0]:
                        for j in range(a):
                            kareler += [poz[0] - j, poz[1] + j]
                    if poz[1] > s_poz[1]:
                        for j in range(a):
                            kareler += [poz[0] + j, poz[1] - j]
    if len(taslar) > 1:
        if isinstance(tahta[x][y], Sah):
            arr = sah_hamle_kontrol_et(tahta[x][y], tahta)
            if len(arr):
                pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                sprite = pygame.image.load(tahta[x][y].resim)
                sprite = pygame.transform.scale(sprite, (square, square))
                pencere.blit(sprite, (y * square, x * square))
                for i in range(len(arr)):
                    if kareler.count(arr[i]) > 1:
                        arr.remove(arr[i])
                    elif kareler.count(arr[i]) == 1:
                        for j in range(len(taslar)):
                            if hamleler.count(taslar.pozisyon) > 0:
                                arr.remove(arr[i])
                            else:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                    else:
                        bos_vurgula([arr[i][0], arr[i][1]])
            else:
                pygame.quit()
        else:
            return False, [-1, -1], [0,0]
    else:
        if isinstance(tahta[x][y], Sah):
            arr = sah_hamle_kontrol_et(tahta[x][y], tahta)
            if len(arr):
                pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                sprite = pygame.image.load(tahta[x][y].resim)
                sprite = pygame.transform.scale(sprite, (square, square))
                pencere.blit(sprite, (y * square, x * square))
                for i in range(len(arr)):
                    if kareler.count(arr[i]) > 1:
                        arr.remove(arr[i])
                    elif kareler.count(arr[i]) == 1:
                        for j in range(len(taslar)):
                            if hamleler.count(taslar.pozisyon) > 0:
                                arr.remove(arr[i])
                            else:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                    else:
                        bos_vurgula([arr[i][0], arr[i][1]])
            else:
                return False, [-1, -1] ,[0,0]
        elif tahta[x][y].pozisyon in kareler:
            return False, [-1, -1], [0,0]
        else:
            if isinstance(tahta[x][y], Piyon):
                arr = piyon_hamle_kontrol_et(tahta[x][y], tahta)
                if len(arr):
                    pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                    sprite = pygame.image.load(tahta[x][y].resim)
                    sprite = pygame.transform.scale(sprite, (square, square))
                    pencere.blit(sprite, (y * square, x * square))
                    for i in range(len(arr)):
                        if arr[i] in kareler:
                            if tahta[arr[i][0]][arr[i][1]] is not None:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                            else:
                                bos_vurgula(arr[i])
                        else:
                            arr.remove(arr[i])
                else:
                    return False, [-1, -1], [0,0]
            elif isinstance(tahta[x][y], At):
                arr = at_hamle_kontrol_et(tahta[x][y], tahta)
                if len(arr):
                    pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                    sprite = pygame.image.load(tahta[x][y].resim)
                    sprite = pygame.transform.scale(sprite, (square, square))
                    pencere.blit(sprite, (y * square, x * square))
                    for i in range(len(arr)):
                        if arr[i] in kareler:
                            if tahta[arr[i][0]][arr[i][1]] is not None:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                            else:
                                bos_vurgula(arr[i])
                        else:
                            arr.remove(arr[i])
                else:
                    return False, [-1, -1], [0,0]
            elif isinstance(tahta[x][y], Kale):
                arr = kale_hamle_kontrol_et(tahta[x][y], tahta)
                if len(arr):
                    pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                    sprite = pygame.image.load(tahta[x][y].resim)
                    sprite = pygame.transform.scale(sprite, (square, square))
                    pencere.blit(sprite, (y * square, x * square))
                    for i in range(len(arr)):
                        if arr[i] in kareler:
                            if tahta[arr[i][0]][arr[i][1]] is not None:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                            else:
                                bos_vurgula(arr[i])
                        else:
                            arr.remove(arr[i])
                else:
                    return False, [-1, -1], [0,0]
            elif isinstance(tahta[x][y], Fil):
                arr = fil_hamle_kontrol_et(tahta[x][y], tahta)
                if len(arr):
                    pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                    sprite = pygame.image.load(tahta[x][y].resim)
                    sprite = pygame.transform.scale(sprite, (square, square))
                    pencere.blit(sprite, (y * square, x * square))
                    for i in range(len(arr)):
                        if arr[i] in kareler:
                            if tahta[arr[i][0]][arr[i][1]] is not None:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                            else:
                                bos_vurgula(arr[i])
                        else:
                            arr.remove(arr[i])
                else:
                    return False, [-1, -1], [0,0]
            elif isinstance(tahta[x][y], Vezir):
                arr = vezir_hamle_kontrol_et(tahta[x][y], tahta)
                if len(arr):
                    pygame.draw.rect(pencere, (255, 127, 80), (square * y, square * x, square, square))
                    sprite = pygame.image.load(tahta[x][y].resim)
                    sprite = pygame.transform.scale(sprite, (square, square))
                    pencere.blit(sprite, (y * square, x * square))
                    for i in range(len(arr)):
                        if arr[i] in kareler:
                            if tahta[arr[i][0]][arr[i][1]] is not None:
                                ye_vurgula(tahta[arr[i][0]][arr[i][1]])
                            else:
                                bos_vurgula(arr[i])
                        else:
                            arr.remove(arr[i])
                else:
                    return False, [-1, -1], [0,0]
    return True, [x, y], arr


def secili_sah_tas_kontrol(poz, tahta, secili_hamle):
    arr = []
    y, x = pygame.mouse.get_pos()
    x = int(x / 100)
    y = int(y / 100)
    if tahta[x][y] is not None:
        if tahta[x][y].pozisyon in secili_hamle:
            tas_sil(tahta, [x, y])
            tahta[poz[0]][poz[1]].pozisyon = [x, y]
            tahta[x][y] = tahta[poz[0]][poz[1]]
            tahta[poz[0]][poz[1]] = None
            tekrar_ciz(tahta)
            return False, 1
        else:
            tekrar_ciz(tahta)
            return False, 1
    else:
        tahta[poz[0]][poz[1]].pozisyon = [x, y]
        tahta[x][y] = tahta[poz[0]][poz[1]]
        tahta[poz[0]][poz[1]] = None
        tekrar_ciz(tahta)
        return False, 1
