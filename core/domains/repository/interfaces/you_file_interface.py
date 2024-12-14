from abc import ABC, abstractmethod


class IYouModelRepository(ABC):

    model = None

    @abstractmethod
    def you_abstract_method(self):
        raise NotImplementedError

