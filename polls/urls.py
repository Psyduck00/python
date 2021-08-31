from django.urls import path
from .views import DetailView, ResultsView, vote, IndexView, user_form

app_name = 'polls'

#urlpatterns = [
#    path('',home,name='home-page'),
        # ex: /polls/5/
#    path('specifics/<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/results/
#    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
#    path('<int:question_id>/vote/', vote, name='vote'),
#]

#urlpatterns = [
 #       path('', index, name='index'),
 #   path('<int:question_id>/', detail, name='detail'),
 #   path('<int:question_id>/results/', results, name='results'),
 #   path('<int:question_id>/vote/', vote, name='vote'),
#]
#domain-name/polls/get-polls
#path('get-polls','',name='polls')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('user-form/', user_form, name='user-form'),
]
