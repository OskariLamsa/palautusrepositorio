"""This is a docstring that explains something?"""

class Varasto:
    """This class is a class"""

    def __init__(self, tilavuus, alku_saldo = 0):
        """Initti"""

        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea.
    # Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """Palauttaa intin joka kertoo jäljellä olevan tilavuuden"""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon epänegatiivisen intin verran mikäli mahtuu.
        Jos ei, tilavuus täyteen"""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ota varastosta epänegatiivinen määrä tavaraa.
        Viittaa kaikki_mita_voidaan jos haluttu määrä ylittää saldon"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Stringi edustus"""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
