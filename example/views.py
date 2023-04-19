from django.views.generic import FormView

from .forms import ExampleForm


class ExampleFormView(FormView):
    form_class = ExampleForm
    template_name = 'form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET.get('validate'):
            kwargs['data'] = {}
        return kwargs
