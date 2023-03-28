from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes(request, item):
    servings = 0
    context = {}
    for key, value in DATA.items():
        if key == item:
            servings = request.GET.get('servings')
            for i in value.keys():
                value[i] *= int(servings)
            context['recipe'] = value
            return render(request, 'calculator/index.html', context)

    # context = {
    #
    #     'recipe': {
    #         'яйца, шт': 2,
    #         'молоко, л': 0.1,
    #         'соль, ч.л.': 0.5,
    #     }
    # }
    # for key, value in DATA.items():
    #     context['recipe'] = value
    # return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def test_print(request):

    context = {
        'first': [1, 2, 3]
    }
    return render(request, 'test_print.html', context)

def why_not_work(request):
    return render(request, 'test_print.html')