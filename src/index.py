from varasto import Varasto

def indent():
    print("hi")

def print_varasto_details(varasto_name, varasto_obj):
    print(f"{varasto_name} saldo = {varasto_obj.saldo}")
    print(f"{varasto_name} tilavuus = {varasto_obj.tilavuus}")
    print(f"{varasto_name} paljonko_mahtuu = {varasto_obj.paljonko_mahtuu()}")

def handle_mehu_operations(mehua):
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto lisäyksen jälkeen: {mehua}")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto otoksen jälkeen: {mehua}")

def handle_error_cases():
    for description, capacity, saldo in [("Varasto(-100.0)",
                                          -100.0, 0),
                                          ("Varasto(100.0, -50.7)",
                                           100.0, -50.7)]:
        print(f"{description}: {Varasto(capacity, saldo)}")

def handle_olut_operations(olutta):
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto lisäyksen jälkeen: {olutta}")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"Olutvarasto oton jälkeen: {olutta}, saatiin: {saatiin}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}")

    if olutta.tilavuus:
        print("olutta")

    print("Olut getterit:")
    print_varasto_details("Olut", olutta)

    handle_mehu_operations(mehua)
    handle_error_cases()
    handle_olut_operations(olutta)

    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto lisäyksen jälkeen: {mehua}")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"Mehuvarasto oton jälkeen: {mehua}, saatiin: {saatiin}")

if __name__ == "__main__":
    main()
