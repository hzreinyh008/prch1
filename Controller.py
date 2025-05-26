
from Model import remove_molecule, get_molecules, get_hybridization_molecule, get_geometry_molecule, get_nep_molecule
from View import *


def main():
    show_message("Привет! Данное приложение поможет тебе изобразить трехмерную структуру вещества, геометрическую форму, а также ты можешь получить информацию по поводу гибридизации, геометрии молекулы и количества неподеленных электронных пар.")
    while True:

        choice = display_menu()

        if choice == '1':

            molecules = get_molecules()
            show_molecules(molecules)

        elif choice == '2':

            molecules = get_molecules()
            show_molecules(molecules)
            molecule_index = get_molecule_index()

            try:
                index = int(molecule_index)

                if remove_molecule(index):
                    show_message("Молекула удалена")
                else:
                    show_message("Такого индекса нет")

            except ValueError:
                show_message("Введи корректный номер")

        elif choice == '3':

            molecules = get_molecules()
            show_molecules(molecules)
            molecule_name = get_molecule_title()

            if molecule_name in molecules:
                show_message("Для закрытия изображения нажмите клавишу 0")
                show_molecule(molecule_name)
            else:
                show_message("Такой молекулы нет")

        elif choice == '4':
            molecules = get_molecules()
            show_molecules(molecules)

            molecule_name = get_molecule_title()
            vvv = get_hybridization_molecule(molecule_name)

            if vvv:
                show_message(f"Гибридизация {molecule_name}: " + vvv)
            else:
                show_message("Не удалось найти гибридизацию")

        elif choice == '5':
            molecules = get_molecules()
            show_molecules(molecules)

            molecule_name = get_molecule_title()
            bbb = get_geometry_molecule(molecule_name)

            if bbb:
                show_message(f"Геометрию молекулы {molecule_name}: " + bbb)
            else:
                show_message("Не удалось найти геометрию молекулы")

        elif choice == '6':

            molecules = get_molecules()
            show_molecules(molecules)
            molecule_name = get_molecule_title()

            if molecule_name in molecules:
                show_message("Для закрытия изображения нажмите клавишу 0")
                show_gm_molecule(molecule_name)
            else:
                show_message("Такой молекулы нет")

        elif choice == '7':
            molecules = get_molecules()
            show_molecules(molecules)

            molecule_name = get_molecule_title()
            nnn = get_nep_molecule(molecule_name)

            if nnn:
                show_message(f"НЕП молекулы {molecule_name}: " + nnn)
            else:
                show_message("Не удалось найти НЕП молекулы")

        elif choice == '0':

            show_message("Дос!")
            break

        else:
            show_message("Неверный выбор, попробуй снова")


if __name__ == "__main__":
    main()
