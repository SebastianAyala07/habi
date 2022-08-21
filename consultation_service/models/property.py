class Property(object):

    db_name = "property"
    fields = ["id", "address", "city", "price", "description", "year"]

    id_: int
    address: str
    city: str
    price: float
    description: str
    year: int

    def __init__(self, **kwargs):
        self.id_ = kwargs.get("id")
        self.address = kwargs.get("address")
        self.city = kwargs.get("city")
        self.price = kwargs.get("price")
        self.description = kwargs.get("description")
        self.year = kwargs.get("year")
