from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    context = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', context)


def login(request):
    title = 'вход'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if next == 'None':
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponseRedirect(reverse('mainapp:index'))

    context = {'title': title, 'next': request.GET.get('next')}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


# class EditView(UpdateView):
#     model = ShopUser
#     template_name = 'authapp/edit.html'
#     fields = ('username', 'first_name', 'last_name', 'age')
#     success_url = reverse_lazy('main')
#
#     def get_context_data(self, **kwargs):
#         context = super(EditView, self).get_context_data(**kwargs)
#         context['title'] = 'Изменение пользователя'
#         print(context)
#         return context

def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {'title': title, 'edit_form': edit_form}
    print(edit_form)
    return render(request, 'authapp/edit.html', context)
