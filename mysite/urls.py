from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

#import numpy as np
#import matplotlib.pyplot as plt


#def graph(request):
#    data = [33, 25, 20, 12, 10]
#    plt.figure(num=1, figsize=(6, 6))
#    plt.axes(aspect=1)
#    plt.title('Plot 3', size=14)
#    plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))

#    plt.savefig('static/images/1.png', format='png')   
#    return render(request, "graph/graph1.html",)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^graph/', graph, name='graph'),
    url(r'', include('blog.urls')),
#    url(r'^accounts/login/$', views.login, name='login'),
#    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('registrations.urls')),
]





