from core.domains.dto.you_file_dto import YouModelDTO
from core.domains.repository.interfaces.you_file_interface import IYouModelRepository


class YouService:

    def __init__(self, repository: IYouModelRepository):
        self.__repository = repository

    def find_all(self):
        result = [
            YouModelDTO(
                title=item.title,
                description=item.description,
                price=item.price,
                category=item.category.pk,
                created_at=item.created_at,
                updated_at=item.updated_at
            )
            for item in self.__repository.find_all()
        ]
        return result
