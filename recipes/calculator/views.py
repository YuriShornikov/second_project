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
    context = {}
    if DATA.get(item) is None:
        pass
    else:
        servings = request.GET.get('servings')
        if servings is None:
            context['recipe'] = DATA[item]
        else:
            context['recipe'] = DATA[item].copy()
            for ckey, cvalue in context['recipe'].items():
                cvalue *= int(servings)
                context['recipe'][ckey] = round(cvalue, 2)

    return render(request, 'calculator/index.html', context)
