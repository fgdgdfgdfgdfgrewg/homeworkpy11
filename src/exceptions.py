class ZeroQuantityError(ValueError):
    """
    Исключение, возникающее при попытке добавить товар с нулевым количеством

    Attributes:
        message (str): Пояснение к ошибке
    """

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)
