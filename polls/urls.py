from django.urls import path
from .views import home, detail, results, vote, index

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

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
#domain-name/polls/get-polls
#path('get-polls','',name='polls')
