import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-1)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo(self):
        varasto = Varasto(10, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_lisays(self):
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-20)

        self.assertAlmostEqual(alkuperainen_saldo, self.varasto.saldo)

    def test_negatiivinen_otto(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-3), 0)

    def test_otetaan_liikaa(self):
        saldo = self.varasto.saldo
        self.assertAlmostEqual(self.varasto.ota_varastosta(saldo + 1), saldo)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_return_merkkijono_rep(self):
        self.varasto.lisaa_varastoon(8)
        tilaa = self.varasto.paljonko_mahtuu()

        haluttu_str = f"saldo = {self.varasto.saldo}, vielä tilaa {tilaa}"

        self.assertEqual(haluttu_str, str(self.varasto))
