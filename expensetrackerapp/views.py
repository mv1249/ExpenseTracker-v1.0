from django.shortcuts import render
from expensetrackerapp.models import Expenses, Todo, CreateUser
from pprint import pprint
from collections import defaultdict

# Create your views here.


def login(request, methods=['GET', 'POST']):

    final_dict = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        count = 1
        for user in CreateUser.objects.all():
            final_dict[count] = user.__dict__
            count += 1

        final_users = []
        final_passwords = []
        for key, value in final_dict.items():
            for key1, value1 in value.items():
                if key1 == 'username':
                    final_users.append(value1)
                if key1 == 'password':
                    final_passwords.append(value1)

        # print(f'Final Passwords: {final_passwords}')
        # print(f'Final Users : {final_users}')
        user_map = {}
        for key, value in final_dict.items():
            for key1, value1 in value.items():
                if key1 == 'username':
                    user_map[value[key1]] = value['password']

        # print(f' Final dict is : {user_map}')

        if username == '':
            context = {'createvalue': True, 'username': True}
            return render(request, 'createerror.html', context=context)

        elif password == '':
            context = {'createvalue': True, 'password': True}
            return render(request, 'createerror.html', context=context)

        elif username in user_map.keys():
            if password == user_map[username]:
                return render(request, 'index.html')

            else:
                context = {'setuser': True}
                return render(request, 'login.html', context)
        else:
            context = {'createvalue': True, 'usernotfound': True}
            return render(request, 'login.html', context)

    return render(request, 'login.html')


def createaccount(request, methods=['GET', 'POST']):

    all_users = {}
    count = 1
    for user in CreateUser.objects.all():
        all_users[count] = user.__dict__
        count += 1
    fullnames = []
    usernames = []
    passwords = []
    for key, value in all_users.items():
        for key1, val1 in value.items():
            if key1 == 'fullname':
                fullnames.append(val1)
            if key1 == 'username':
                usernames.append(val1)
            if key1 == 'password':
                passwords.append(val1)

    # print(f' AllFullnamess are : {fullnames}')
    # print(f' All Usernames are : {usernames}')
    # print(f' Password is : {passwords}')

    if request.method == 'POST':
        fullname = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if fullname == '':
            context = {'value': True, 'fullname': True}
            return render(request, 'createerror.html', context=context)

        elif username == '':
            context = {'value': True, 'username': True}
            return render(request, 'createerror.html', context=context)

        elif password == '':
            context = {'value': True, 'password': True}
            return render(request, 'createerror.html', context=context)

        elif fullname in fullnames or username in usernames or password in passwords:
            context = {'value': True, 'userexists': True}
            return render(request, 'createerror.html', context=context)

        else:
            instance = CreateUser(
                fullname=fullname, username=username, password=password)
            instance.save()
            context = {'value': True}
            return render(request, 'login.html', context=context)

    return render(request, 'createaccount.html')


def createerror(request):
    return render(request, 'createerror.html')


def home(request, methods=['GET', 'POST']):

    return render(request, 'index.html')


def dashboard(request, methods=['GET', 'POST']):

    expenditure_dict = {}
    income_dict = {}
    particular_month_income_dict = {}
    particular_month_expenditure_dict = {}
    total_month_income_dict = {}
    total_month_expenditure_dict = {}
    total_expenses = defaultdict(list)
    present_expenses = defaultdict(list)
    total_months = []
    total_income = defaultdict(list)
    present_income = defaultdict(list)

    expenses = 1
    incomes = 1
    year_map = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    if request.method == 'POST':
        name = request.POST.get('name')
        anual_income = request.POST.get('income')
        month = request.POST.get('month')

        completedata = Expenses.objects.filter(name=name)

    # <--------------------Calculating Total Income and Total Expenses Month Wise----------------->

        total_expense = 1
        for expense in Expenses.objects.filter(name=name, savingexp='expenditure'):
            total_month_expenditure_dict[total_expense] = expense.__dict__
            total_expense += 1

        total_incomes = 1
        for expense in Expenses.objects.filter(name=name, savingexp='gain'):
            total_month_income_dict[total_incomes] = expense.__dict__
            total_incomes += 1

        # print(f' Total Expenditure : {total_month_expenditure_dict}')
        # print(f' Total Income : {total_month_income_dict}')

        for key, value in total_month_expenditure_dict.items():

            total_expenses[year_map[value['month']]].append(value['value'])

        for key, value in total_month_income_dict.items():
            total_income[year_map[value['month']]].append(value['value'])

        total_expenses = dict(total_expenses)
        total_income = dict(total_income)

        for key, val in total_expenses.items():
            val = [int(i) for i in val]
            total_expenses[key] = sum(val)
        for key, val in total_income.items():
            val = [int(i) for i in val]
            total_income[key] = sum(val)

        # print(f' Total Expenses is : {total_expenses}')
        # print(f' Total Income is : {total_income}')

    # -------------------------------Total Expenses and Incomes till now------------------>

        total_income_uptilnow = sum(list(total_income.values()))
        total_expense_uptilnow = sum(list(total_expenses.values()))

        # print(f' Total Expenses till now is :{total_expense_uptilnow}')
        # print(f' Total Income till now is :{total_income_uptilnow}')

    # <------------------------------Base Conditions------------------------------------>

        if len(completedata) == 0:
            context = {'namenotfoundindb': False}
            return render(request, 'error.html', context)

        elif name == '':
            context = {'value': True, 'namenotfound': True}
            return render(request, 'error.html', context)

        elif anual_income == '':
            context = {'value': True, 'month_topass': False}
            return render(request, 'error.html', context)

        elif month == 'None':
            context = {'value': True, 'month_topass': True}
            return render(request, 'error.html', context)

    # <---------------------------------Present Conditions------------------------------>
        else:
            for expense in Expenses.objects.filter(name=name, savingexp='expenditure', month=month):
                expenditure_dict[expenses] = expense.__dict__
                expenses += 1

            for income in Expenses.objects.filter(name=name, savingexp='gain', month=month):
                income_dict[incomes] = income.__dict__
                incomes += 1

            if len(income_dict) == 0 and len(expenditure_dict) == 0:
                context = {'noincomeexpense': True}
                return render(request, 'dashboarderror.html', context)

            else:

                for key, val in expenditure_dict.items():
                    present_expenses[val['date']].append(val['value'])

                for key, val in income_dict.items():
                    present_income[val['date']].append(val['value'])

                # print(f' Present Expenditure is : {present_expenses}')
                # print(f' Present income is : {present_income}')

                expense_current_date = list(present_expenses.keys())
                income_current_date = list(present_income.keys())

                current_expense = list(present_expenses.values())
                current_expense = [int(i[0]) for i in current_expense]

                current_income = list(present_income.values())
                current_income = [int(i[0]) for i in current_income]

                # print(f' Current Expense is : {current_expense}')
                # print(f' Current Expense Date is : {expense_current_date}')

                # print(f' Current Income Date is : {income_current_date}')
                # print(f' Current Income is : {current_income}')

                total_cur_exp = sum(current_expense)
                total_cur_income = sum(current_income)
                monthly_income = int(anual_income)//12
                profityaloss = False
                plval = 0

                # Loss

                if total_cur_exp > total_cur_income:
                    plval = abs(monthly_income+total_cur_income-total_cur_exp)
                    paise = abs(monthly_income-plval)

                # Profit

                elif total_cur_income > total_cur_exp:
                    plval = abs(
                        (monthly_income+total_cur_income)-total_cur_exp)
                    paise = abs(monthly_income-plval)
                    profityaloss = True

                year_map = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                            '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

                context = {
                    'current_expense_date': expense_current_date,
                    'current_income_date': income_current_date,
                    'current_expenses': current_expense,
                    'current_income': current_income,
                    'total_expenses': total_expenses,
                    'total_income': total_income,
                    'present_expenses': dict(present_expenses),
                    'present_income': dict(present_income),
                    'month': year_map[month],
                    'showchart': True,
                    'profityaloss': profityaloss,
                    'plval': plval,
                    'paise': paise,
                }
        return render(request, 'dashboard.html', context)

    return render(request, 'dashboard.html')


def transactions(request, method=['GET', 'POST']):

    year_map = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    if request.method == 'POST':
        name = request.POST.get('name')
        month = request.POST.get('month')

        completedata = Expenses.objects.filter(name=name, month=month)

        # Basic Checks

        if name == '':
            context = {'value': True, 'namenotfound': True}
            return render(request, 'error.html', context)

        elif month == 'None':
            context = {'value': True, 'monthnotfound': True}
            return render(request, 'dashboarderror.html', context)

        context = {
            'value': True,
            'allTodo': completedata,
            'month_topass': year_map[month],
            'todolength': len(completedata),
        }

        return render(request, 'transaction.html', context=context)

    return render(request, 'transaction.html')


def addtodo(request, method=['GET', 'POST']):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        month = request.POST.get('month')
        value = request.POST.get('value')

        instance = Todo(name=name, date=date, month=month, value=value)
        instance.save()
    return render(request, 'index.html')


def expenses(request, methods=['GET', 'POST']):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        gainexp = request.POST.get('gainexp')
        date = request.POST.get('date')
        month = request.POST.get('month')
        week = request.POST.get('week')
        value = request.POST.get('value')

        instance = Expenses(name=fullname, savingexp=gainexp, date=date,
                            month=month, expensegain=week, value=value)

        instance.save()

        # print(
        #     f' Gainexp is : {gainexp}, month : {month},date : {date},week : {week},value : {value}')
    # expenses = Expenses.objects.all()
    # print(dict(expenses))
    return render(request, 'index.html')


def displaytodo(request, methods=['GET', 'POST']):

    year_map = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    if request.method == 'POST':
        name = request.POST.get('name')
        month = request.POST.get('month')

        allcollection = Todo.objects.filter(name=name, month=month)
        # pprint(allcollection)

        if name == '':
            context = {'value': True, 'namenotfound': True}
            return render(request, 'error.html', context)

        elif month == 'None':
            context = {'value': True, 'monthnotfound': True}
            return render(request, 'dashboarderror.html', context)

        context = {
            'value': True,
            'allTodo': allcollection,
            'month_topass': year_map[month],
            'todolength': len(allcollection),
        }

        return render(request, 'todolist.html', context)

    return render(request, 'todolist.html')


def error(request):
    return render(request, 'error.html')


def expenseerror(request):
    return render(request, 'expenseerror.html')


def todoerror(request):
    return render(request, 'todoerror.html')


def exception(request):
    return render(request, 'exception.html')


def dashboarderror(request):
    return render(request, 'dashboarderror.html')
