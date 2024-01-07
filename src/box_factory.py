# box_factory.py
from box import Box
from constantes import Colors


class BoxFactory:
    @staticmethod
    def create_boxes():
        """
        Crea una lista de instancias de la clase Box con información predeterminada.

        :return: Lista de instancias de la clase Box.
        """
        box_list = [
            Box(
                name="box_score",
                position_x=580,
                position_y=240,
                width=200,
                height=50,
                color=Colors.custom_color,
            ),
            Box(
                name="box_next_block",
                position_x=580,
                position_y=340,
                width=200,
                height=140,
                color=Colors.custom_color,
            ),
        ]

        return box_list

    @staticmethod
    def get_box_by_name(name):
        """
        Busca una caja por su nombre en la lista de cajas creadas por create_boxes.

        :param name: Nombre de la caja a buscar.
        :return: La caja con el nombre correspondiente o None si no se encuentra.
        """
        box_list = BoxFactory.create_boxes()
        for box in box_list:
            if box.name == name:
                return box
        return None
