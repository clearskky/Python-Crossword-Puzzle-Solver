def sonuc(ikib_liste, aranacaklar_listesi):
    harf_index_dict = dict()
    for kelime in aranacaklar_listesi:
        harf_index_dict[kelime] = {}
        breakLoop = True
        for satir in range(len(ikib_liste)):
            for sutun in range(len(ikib_liste[satir])):
                if ikib_liste[satir][sutun] == kelime[0]:
                    yonlerikontrolet(ikib_liste, kelime, satir, sutun, harf_index_dict)
                    if len(harf_index_dict[kelime]) == len(kelime):
                        breakLoop = False
                        break
            if breakLoop == False:
                break

    for index in harf_index_dict:
        print(index + ': ' + index[0] + '=' + str(list(harf_index_dict[index].keys())[0]) + ' ' + index[len(index) - 1] + '=' + str(list(harf_index_dict[index].keys())[len(index) - 1]))


def yonlerikontrolet(ikib_liste, kelime, satir, sutun, indis_dict):
    backup_satir = satir
    backup_sutun = sutun

    # Kuzey yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir -= 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Kuzeydoğu yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir -= 1
                sutun += 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Doğu yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                sutun += 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Güneydoğu yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir += 1
                sutun += 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Güney yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir += 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Güneybatı yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir += 1
                sutun -= 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Batı yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                sutun -= 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    # Kuzeybatı yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                satir -= 1
                sutun -= 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
            else:
                indis_dict[kelime].clear()
                satir = backup_satir
                sutun = backup_sutun
                break
        except IndexError:
            indis_dict[kelime].clear()
            satir = backup_satir
            sutun = backup_sutun
            break

    return indis_dict

chars2D = [
        ('B', 'M', 'H', 'V', 'D', 'Ş', 'L', 'İ', 'Ü', 'S'),
        ('Y', 'N', 'Ü', 'G', 'Z', 'Ü', 'A', 'T', 'T', 'P'),
        ('F', 'G', 'G', 'A', 'R', 'İ', 'P', 'İ', 'G', 'N'),
        ('Y', 'A', 'M', 'U', 'Ö', 'L', 'O', 'D', 'İ', 'O'),
        ('C', 'L', 'H', 'D', 'F', 'Ç', 'E', 'K', 'G', 'H'),
        ('F', 'H', 'S', 'U', 'A', 'E', 'K', 'Ü', 'A', 'T'),
        ('C', 'Ö', 'Ö', 'Y', 'T', 'Ş', 'L', 'O', 'İ', 'Y'),
        ('G', 'K', 'L', 'N', 'F', 'M', 'D', 'C', 'M', 'P'),
        ('N', 'A', 'I', 'Z', 'E', 'H', 'Ğ', 'A', 'İ', 'İ'),
        ('P', 'S', 'Ü', 'K', 'P', 'Ğ', 'I', 'P', 'J', 'D')]

aranacaklar_listesi = ["GARİP", "TUHAF", "PALYAÇO", "GÜLMEK", "ÜZGÜN", "DİCLE"]

sonuc(chars2D, aranacaklar_listesi)

print("FREEEDOOOOOOM")
