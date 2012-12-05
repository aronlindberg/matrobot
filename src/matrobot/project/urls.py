from django.conf.urls.defaults import patterns


urlpatterns = patterns('matrobot.project.views',
    (r'^$', 'index'),
    (r'^download$', 'download'),
    (r'^long_term$', 'long_term'),
    (r'^top$', 'top_projects'),
)

