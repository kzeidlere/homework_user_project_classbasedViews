from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View, FormView, DetailView, DeleteView

from user.models import User
from user.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class AddUserView(FormView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


class EditUserView(View):
    def get(self, request):
        user_id = request.POST['user_id']
        users = User.objects.get(pk=user_id)

        users.save()

        context = {
            'users': users,
        }
        return render(
            template_name='user_detail.html',
            request=request,
            context=context,
        )

    def post(self, request):

        user_id = request.POST['user_id']
        users = User.objects.get(pk=user_id)

        context = {
            'users': users,
        }

        return render(
            template_name='edit_user.html',
            request=request,
            context=context,
        )


class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = '/'
