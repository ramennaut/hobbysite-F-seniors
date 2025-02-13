from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse("""
        <h1>Recipe Book</h1>
        <p><a href="/recipe/1/">Recipe 1</a></p>
        <p><a href="/recipe/2/">Recipe 2</a></p>
    """)

def recipe_1(request):
    return HttpResponse("""
        <h1>Recipe Book</h1>
        <h2>Recipe 1 Ingredients</h2>
        <ul>
            <li>Tomato - 3pcs</li>
            <li>Onion - 1pc</li>
            <li>Pork - 1kg</li>
            <li>Water - 1L</li>
            <li>Sinigang Mix - 1 packet</li>
        </ul>
    """)

def recipe_2(request):
    return HttpResponse("""
        <h1>Recipe Book</h1>
        <h2>Recipe 2 Ingredients</h2>
        <ul>
            <li>Garlic - 1 head</li>
            <li>Onion - 1pc</li>
            <li>Vinegar - 1/2 cup</li>
            <li>Water - 1 cup</li>
            <li>Salt - 1 tablespoon</li>
            <li>Whole black peppers - 1 tablespoon</li>
            <li>Pork - 1kg</li>
        </ul>
    """)
