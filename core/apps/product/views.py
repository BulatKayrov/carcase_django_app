from django.views import generic

from django.shortcuts import render

from core.apps.product.tasks import you_task
from core.domains.repository.you_file_repository import YouModelRepository
from core.domains.services.you_file_services import YouService

from django.core.cache import cache


class IndexView(generic.View):
    product_service = YouService(YouModelRepository())
    template_name = 'product/index.html'

    def get(self, request):
        products = cache.get('products', None)
        if products is None:
            products = self.product_service.find_all()
            cache.set('products', products, 30)

        you_task.delay()
        context = {
            'products': products
        }
        return render(request=request, template_name=self.template_name, context=context)
