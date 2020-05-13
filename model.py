import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'w'
PORAZ = 'x'

class Igra: 
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

# geslo upper je da se use črke spremenijo v velike

# seznam smo pa nardil da se v vsakem seznamu posebi crke spremenijo v velke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

# vrne tiste crke ki jih ni v geslu        

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

# vrne crke ki so v geslu

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True
    # Drug nacin
    # def zmaga(self):
    #   return set(self.geslo) == set(self.pravilne_crke())
    # Tretji nacin
    # def zmaga(self):
    #   all(crka in self.crke for crka in self.geslo)

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            s += crka if crka in self.crke else '_'
        return s

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(ugibana_crka)
            if ugibana_crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else: 
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []
for beseda in open('besede.txt', encoding='utf-8'):
    bazen_besed.append(beseda.strip().upper())
#besede iz datoteke smo dodali v seznam in odstranili presledke in nrdil črke velke

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)

