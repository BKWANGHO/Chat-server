from dataclasses import dataclass

@dataclass
class MemberModel:

    _name : str = ''
    _height : float = 0.0
    _weight : float = 0.0

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name: str): self._name = name

    @property
    def height(self) -> float: return self._height

    @height.setter
    def height(self, height: float): self._height = height

    @property
    def weight(self) -> float : return self._weight

    @weight.setter
    def weight(self, weight: float): self._weight = weight