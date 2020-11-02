from django.http import JsonResponse
from django.contrib import messages



class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, sataus =400)
        else :
            return response
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Succesfully submitted form data"
            }
            return JsonResponse(data)

        else :
            return response
