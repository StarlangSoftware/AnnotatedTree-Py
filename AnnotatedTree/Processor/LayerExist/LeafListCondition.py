from abc import abstractmethod


class LeafListCondition:

    @abstractmethod
    def satisfies(self, leafList: list) -> bool:
        pass
