from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Article
from .forms import ContactForm

# Page d'accueil
from .models import Category

from django.shortcuts import render
from .models import Category, Product, Article

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-published_at')[:4]

    return render(request, 'index.html', {
        'all_categories': categories,  # pour le menu déroulant
        'categories': categories,      # pour l'affichage sur la page
        'articles': articles,
    })



def product_detail(request, product_id):
    produit = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {
        'produit': produit,
    })

# Catégories
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


# Blog
def blog(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, 'blog.html', {'articles': articles})

# Article détail
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})

# Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    produits = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        'category': category,
        'produits': produits
    })
def product_list(request):
    produits = Product.objects.all()
    categories = Category.objects.all()

    # Filtres
    nom = request.GET.get('nom')
    prix_min = request.GET.get('prix_min')
    prix_max = request.GET.get('prix_max')
    categorie_id = request.GET.get('categorie')

    if nom:
        produits = produits.filter(name__icontains=nom)

    if prix_min:
        produits = produits.filter(price__gte=prix_min)

    if prix_max:
        produits = produits.filter(price__lte=prix_max)

    if categorie_id:
        produits = produits.filter(category_id=categorie_id)

    return render(request, 'product_list.html', {
        'produits': produits,
        'categories': categories
    })

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    produits = Product.objects.filter(category=category)

    # Récupérer les filtres de l'URL (GET)
    nom = request.GET.get('nom', '')
    prix_min = request.GET.get('prix_min')
    prix_max = request.GET.get('prix_max')

    if nom:
        produits = produits.filter(name__icontains=nom)
    if prix_min:
        try:
            produits = produits.filter(price__gte=float(prix_min))
        except ValueError:
            pass
    if prix_max:
        try:
            produits = produits.filter(price__lte=float(prix_max))
        except ValueError:
            pass

    return render(request, 'category_products.html', {
        'category': category,
        'produits': produits,
        'nom': nom,
        'prix_min': prix_min,
        'prix_max': prix_max,
    })


from .models import Category

def all_categories_context(request):
    return {
        'all_categories': Category.objects.all()
    }
