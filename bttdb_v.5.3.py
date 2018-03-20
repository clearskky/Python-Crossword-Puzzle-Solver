def sonuc(ikib_liste, aranacaklar_listesi):
    kelime_harf_indis = dict()
    for kelime in aranacaklar_listesi:
        try:
            for satir in ikib_liste:
                for harf in satir:
                    if harf == kelime[0]:
                        yonlerikontrolet(ikib_liste, kelime, ikib_liste.index(satir), satir.index(harf), harf, kelime_harf_indis)
                        if len(kelime_harf_indis[kelime]) == len(kelime):
                            print(fucktrabzon)
        except:
            continue

    print(kelime_harf_indis)


def yonlerikontrolet(ikib_liste, kelime, satir, sutun, harf, indis_dict):
    indis_dict[kelime] = {}
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
                continue
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
                continue
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
                continue
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
                continue
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
                continue
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
                continue
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

    # Kuzey yönünü kontrol
    for karakter in kelime:
        try:
            if ikib_liste[satir][sutun] == karakter:
                indis_dict[kelime][(satir, sutun)] = karakter
                sutun -= 1
                if len(indis_dict[kelime]) == len(kelime):
                    return indis_dict
                continue
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
                continue
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
        ('F', 'G', 'A', 'R', 'İ', 'P', 'N', 'İ', 'G', 'N'),
        ('Y', 'A', 'M', 'U', 'Ö', 'L', 'O', 'D', 'İ', 'O'),
        ('C', 'L', 'H', 'D', 'F', 'Ç', 'E', 'K', 'G', 'H'),
        ('F', 'H', 'S', 'U', 'A', 'E', 'K', 'Ü', 'A', 'T'),
        ('C', 'Ö', 'Ö', 'Y', 'T', 'Ş', 'L', 'O', 'İ', 'Y'),
        ('G', 'K', 'L', 'N', 'F', 'M', 'D', 'C', 'M', 'P'),
        ('N', 'A', 'I', 'Z', 'E', 'H', 'Ğ', 'A', 'İ', 'İ'),
        ('P', 'S', 'Ü', 'K', 'P', 'Ğ', 'I', 'P', 'J', 'D')]

aranacaklar_listesi = ["PYTHON", "GARİP", "TUHAF", "PALYAÇO", "GÜLMEK", "ÜZGÜN", "DİCLE"]

sonuc(chars2D, aranacaklar_listesi)

input("Programdan çıkmak için bir şey gir: ")