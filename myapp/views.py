from django.shortcuts import render
import json
import datetime
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
# Create your views here.


# Create your views here.
class LoginRequiredMixin(object):
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/users/login')


class HomeView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get(self, request):
        recent_movie_list = MovieModel.objects.order_by("-publish_time")[:9]
        recommend_movie_list =  MovieModel.objects.order_by("-star")[:10]
        return render(request, 'index.html',{"recent_movie_list":recent_movie_list,
                                             "recommend_movie_list": recommend_movie_list})

class SortView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SortView, self).dispatch(*args, **kwargs)

    def get(self, request):
    
        _type=request.GET.get("_type")
        recent_movie_list = MovieModel.objects.order_by("-publish_time")[:5]
        option_list = ClassifyModel.objects.all()
        if _type:
            movie_list = MovieModel.objects.filter(classify__name = _type)
        else:
            movie_list = MovieModel.objects.all()
        return render(request, 'sort.html', {"movie_list": movie_list, "option_list": option_list})

    def post(self,request):
        q = request.POST.get("q")
        movie_list = MovieModel.objects.filter(name__contains=q)
        option_list = ClassifyModel.objects.all()

        return render(request, 'sort.html', {"movie_list": movie_list, "option_list": option_list})


class MovieDetail(View):
    def get(self, request):
        movie_id = int(request.GET.get("id"))
        item = MovieModel.objects.get(id = movie_id)
        return render(request, 'movie_item.html', {'item': item})


class PublishCommentView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PublishCommentView, self).dispatch(*args, **kwargs)

    def post(self, request):
        try:
            uid = int(request.POST["id"])
            movie = MovieModel.objects.get(id=uid)
            score = int(request.POST['score'])
            content = request.POST['content']
            CommentModel.objects.create(person=request.user, content=content, create_time=datetime.datetime.now(), movie=movie,score=score)
            commenList = movie.tie_comment.all()
            sum = 0
            count =0 
            for comment in commenList:
                sum += comment.score
                count +=1 
            
            movie.star = int(sum/count/20)
            movie.save()
            return HttpResponse(json.dumps({"err": 0}), content_type='application/json')
        except Exception as e:
            raise Http404