from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order, Instructors, Branches, Comments, User
from .forms import InstructorSearchForm, CommentsForm, OrderForm, SignUpForm



# Create your views here.
def home(request):
    branches = Branches.objects.all()
    context = {'branches': branches}
    return render(request, 'home.html', context)


def get_all_branch(request, pk):
    branch_id = Branches.objects.get(id=pk)
    instructors = Instructors.objects.filter(branches=branch_id)
    context = {'instructor': instructors}
    return render(request, 'branches.html', context)


def get_full_inst(request, pk):
    instructor = Instructors.objects.get(id=pk)
    comments = Comments.objects.filter(user_topic=instructor)
    order = Order.objects.filter(sub_inst=instructor)

    error = ''
    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            user_comment = form.cleaned_data['user_comment']
            user = request.user
            Comments.objects.create(user=user, user_topic=instructor, user_comment=user_comment).save()
            return redirect('/')
        else:
            error = form.errors

    form1 = OrderForm()
    if request.method == 'POST':
        form1 = OrderForm(request.POST)
        if form1.is_valid():
            user = request.user
            user_name = form1.cleaned_data['user_name']
            sub = form1.cleaned_data['subscription']
            phone = form1.cleaned_data['phone_num']
            Order.objects.create(user=user, user_name=user_name,
                                 subscription=sub, phone_num=phone, sub_inst=instructor).save()
            return redirect('/')
        else:
            error = form1.errors
    context = {
        'instructor': instructor,
        'comments': comments,
        'order': order,
        'form': form,
        'error': error,
        'form1': form1
    }

    return render(request, 'instructor.html', context)


def search_in(request):
    form = InstructorSearchForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        search = form.cleaned_data.get('search')
        result = Instructors.objects.filter(name__icontains=search)
    else:
        result = Instructors.objects.all()

    context = {'result': result,
               'form': form}
    return render(request, 'search_result.html', context)


def get_all_orders(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'ORDERS.html', context)


def logout_review(request):
    logout(request)
    return redirect('/')


def sign_up(request):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error = form.errors

    form = SignUpForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/signup.html', context)