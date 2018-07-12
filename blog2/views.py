from django.shortcuts import render, get_object_or_404 
from django.utils import timezone
from . models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
	object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	paginator = Paginator(object_list, 3)  #3 postari pe pagina
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog2/post_list.html', {'page' : page, 'posts' : posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog2/post_detail.html', {'post': post})

