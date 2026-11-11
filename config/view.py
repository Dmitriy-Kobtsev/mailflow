from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Главная страница сервиса.

    Пока — заглушка со ссылками на разделы. Когда появятся
    реальные ListView рассылок/клиентов, можно заменить на редирект
    или на сводку (последние рассылки, статистика).
    """
    template_name = "home.html"