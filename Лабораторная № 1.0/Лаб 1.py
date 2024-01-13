#
import doctest
class Lamp:
    def __init__(self, max_wattage: float, current_wattage: float):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param max_wattage: Максимальная мощность лампы
        :param current_wattage: Текущая мощность, с которой работает лампа

        Примеры:
        >>> lamp = Lamp(100, 60)  # инициализация экземпляра класса
        """
        if not isinstance(max_wattage, (int, float)):
            raise TypeError("Максимальная мощность должна быть типа int или float")
        if max_wattage <= 0:
            raise ValueError("Максимальная мощность должна быть положительным числом")
        self.max_wattage = max_wattage

        if not isinstance(current_wattage, (int, float)):
            raise TypeError("Текущая мощность должна быть int или float")
        if current_wattage < 0:
            raise ValueError("Текущая мощность не может быть отрицательным числом")
        self.current_wattage = current_wattage

    def turn_on(self) -> None:
        """
        Включение лампы.

        Примеры:
        >>> lamp = Lamp(100, 60)
        >>> lamp.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Выключение лампы.

        Примеры:
        >>> lamp = Lamp(100, 60)
        >>> lamp.turn_off()
        """
        ...

    def change_brightness(self, new_wattage: float) -> None:
        """
        Изменение яркости лампы.

        :param new_wattage: Новая мощность лампы
        :raise ValueError: Если новая мощность превышает максимальную мощность, то вызываем ошибку

        Примеры:
        >>> lamp = Lamp(100, 60)
        >>> lamp.change_brightness(80)
        """
        if not isinstance(new_wattage, (int, float)):
            raise TypeError("Новая мощность должна быть типа int или float")
        if new_wattage < 0:
            raise ValueError("Новая мощность должна быть положительным числом")
        if new_wattage > self.max_wattage:
            raise ValueError("Новая мощность не может превышать максимальную мощность лампы")
        ...


if __name__ == "__main__":
    doctest.testmod()