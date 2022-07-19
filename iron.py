import requests
from lxml import etree
from io import StringIO

URL = "https://www.iranjib.ir/showgroup/38/%D9%82%DB%8C%D9%85%D8%AA-%D8%A2%D9%87%D9%86-%D8%A2%D9%84%D8%A7%D8%AA/"
parser = etree.HTMLParser()


class Stuff:
    """get prices of iron stuffs from iranjib"""

    def __init__(self, title, group, today_price, weight, lentgh, diffrent):
        """(Stuff, str, str, int, int, int, int) -> NoneType

        Initial parameters for Iron stuff.

        >>> t_12 = Stuff("Girder_12", "girder", 2330000, 122, 12, -10000)
        >>> t_12.title
        'Girder_12'
        >>> t_12.today_price
        2330000

        """

        self.title = title
        self.group = group
        self.today_price = today_price
        self.weight = weight
        self.lentgh = lentgh
        self.diffrent = diffrent

    def former_price(self):
        """(Stuff) -> NoneType

        Return yesterday price.

        >>> t_12 = Stuff("Girder_12", "girder", 2330000, 122, 12, -10000)
        >>> t_12.former_price()
        2320000

        """

        return self.today_price + self.diffrent

    def price_per_kg(self):
        """ (Stuff) -> float

        Return value of a kg.

        >>> t_12 = Stuff("Girder_12", "girder", 2330000, 122, 12, -10000)
        >>> t_12.price_per_kg()
        19098.360655737706

        """

        return self.today_price / self.weight

    def weight_per_meter(self):
        """ (Stuff) -> float

        Return weight of a meter.

        >>> t_12 = Stuff("Girder_12", "girder", 2330000, 122, 12, -10000)
        >>> t_12.weight_per_meter()
        10.166666666666666

        """

        return self.weight / self.lentgh


def get_status_code():
    """ (NoneType) -> int

    Return status code of a webpage

    >>> get_status_code()
    200

    """
    session = requests.get(URL)
    return session.status_code


def get_information():
    """ (NoneType) -> list of list of str

    Return status code of a webpage

    """
    req = requests.get(URL)
    return req.text


def parse():
    res = requests.get(URL)
    tree = etree.parse(StringIO(res.text), parser)
    return tree.xpath("//tr")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    assert get_status_code() == 200, "Check enternet connection"
    print(parse())
    # print(get_information())
