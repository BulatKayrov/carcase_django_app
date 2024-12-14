from core.apps.product.models import YouModel
from core.domains.repository.interfaces.you_file_interface import IYouModelRepository


class YouModelRepository(IYouModelRepository):
    model = YouModel

    def find_all(self):
        return self.model.objects.all()

    def find_by_id(self, pk):
        return self.model.objects.filter(pk=pk)
