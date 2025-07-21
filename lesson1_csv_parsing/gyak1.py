with open("diakok.txt", "r", encoding="utf-8") as f:
    diakok = dict()
    for sor in f:
        nev, evfolyam, targy, atlag = sor.strip().split(":")
        diakok[nev] = {"evfolyam": evfolyam, "targy": targy, "atlag": atlag}

#print(diakok)
#print(type(diakok.keys()))
#print(list(diakok.items())[:2])
#print(dict(list(diakok.items())[:2]))
#print(diakok.get("Kiss Zsolt").get("evfolyam")) #output: 10
#print(diakok["Kiss Zsolt"]["evfolyam"]) #ugyanugy 10

def kereses(diak: str):
    """
    Prints the given student's data if that exists.
    :param diak: The given student's name.
    """
    print(f"Diák: {diak}\nKedvenc tárgya: {diakok[diak]["targy"]}\nÁtlaga: {diakok[diak]["atlag"]}") \
        if diakok.get(diak) is not None else print("nincs ilyen arc")
#kereses("Kiss Zsolt")

def atlag(dictem: dict):
    """
    Prints the mean of the students' avarage grades.
    :param dictem: The diakok.txt parsed to diakok dict.
    """
    if isinstance(dictem, dict):
        osszesen = 0
        for atlag in dictem.values():
            #print(atlag["atlag"])
            osszesen += float(atlag["atlag"])
        print(f"átlagok átlaga: {osszesen / len(dictem) :,.3f}") #3 tizedesre kerekítve, ezreseknél vesszővel tagolva a , miatt
#atlag(diakok)

def statisztika(dictem: dict):
    """
    Prints the students with the best and the worst results.
    :param dictem: The diakok.txt parsed to diakok dict.
    :return:
    """
    if isinstance(dictem, dict):
        #legjobb = max([x["atlag"] for x in dictem.values()])
        legjobb = dict([sorted(dictem.items(), key=lambda k: k[1]["atlag"], reverse=True)[0]])
        for kulcs, ertek in legjobb.items():
            print(f"Legjobb eredmény:\nDiák: {kulcs}, Tantárgy: {ertek["targy"]}, Átlaga: {ertek["atlag"]}")

        worst_kulcs, worst_ertek = sorted(dictem.items(), key=lambda k: k[1]["atlag"])[0]
        print(f"Legrosszabb:\nDiák: {worst_kulcs}, Tantárgy: {worst_ertek["targy"]}, Átlaga: {worst_ertek["atlag"]}")

        legrosszabb = dict(sorted(dictem.items(), key=lambda k: k[1]["atlag"])[:1])
        for kulcs, ertek in legrosszabb.items():
            print(f"Legrosszabb:\nDiák: {kulcs}, Tantárgy: {ertek["targy"]}, Átlaga: {ertek["atlag"]}")
#statisztika(diakok)

def evfolyam_atlag(dictem: dict):
    """
    Prints the mean grades for each class.
    :param dictem: The diakok.txt parsed to diakok dict.
    """
    if isinstance(dictem, dict):
        #kulcs, ertek = sorted(dictem.items(), key=lambda k: k[1]["evfolyam"])
        #rendezett_dictem = dict(sorted(dictem.items(), key=lambda k: k[1]["evfolyam"]), reverse=False)

        atlagok_evfolyamonkent = dict()
        for i in dictem.values():
            atlagok_evfolyamonkent[i["evfolyam"]] = atlagok_evfolyamonkent.get(i["evfolyam"], []) + [i["atlag"]]

        print("Évfolyamonkénti átlagok:\n")

        rendezett_evf_atlagok = dict(sorted(atlagok_evfolyamonkent.items(), key=lambda k: int(k[0])))

        for kulcs, ertek in rendezett_evf_atlagok.items():
            floatra_kasztolva = list(map(lambda x: float(x), ertek))
            rendezett_evf_atlagok[kulcs] = sum(floatra_kasztolva) / len(floatra_kasztolva)
            print(f"{kulcs}. évfolyam: {rendezett_evf_atlagok[kulcs] :,.3f}")

#evfolyam_atlag(diakok)

def tantargy_atlag(dictem: dict):
    """
    Prints the mean grades for each subject.
    :param dictem: The diakok.txt parsed to diakok dict.
    """
    if isinstance(dictem, dict):
        targyankent_atlag = dict()
        for i in dictem.values():
            targyankent_atlag[i["targy"]] = targyankent_atlag.get(i["targy"], []) + [i["atlag"]]

        for kulcs, ertek in targyankent_atlag.items():
            floatra_kasztolva = list(map(lambda x: float(x), ertek))
            targyankent_atlag[kulcs] = sum(floatra_kasztolva) / len(floatra_kasztolva)
            print(f"{kulcs}: {targyankent_atlag[kulcs] :,.3f}")

#tantargy_atlag(diakok)
