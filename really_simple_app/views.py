from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def really_simple_function(request):
    return HttpResponse("""
    <h1>A Really Simple App</h1>
        <h2>In Django</h2>
            <h3>Does not</h3>
                <p>It does not include database, forms, or template.</p>
                <p>It does not even add any files other than created by Django.</p>
            <h3>Does</h3>
                <p>
                    <a href='/simple_url_routing'>
                        Show how to do URL routing--in the simplest, but not best, way.
                    </a>
                </p>

                <p>Return HTML really simply.</p>"""
    )

def simple_url_routing_function(request):
    return HttpResponse("""
        <h1>Routing of HTML requests</h1>
            <h2>Simplest sample</h2>
                <h3>In urls.py of the project</h3>
                    <p>Include the views.py in the app's folder</p>
                    <pre>
from really_simple_app import views as really_simple_app_views
                    </pre>
                    <p>In the <code>urlpatterns</code> list add a <code>path</code> function that will call the function to respond to the HTTP request.</p>
                    <pre>
urlpatterns = [
    path('really_simple_home/',
        really_simple_app_views.really_simple_function,
        name='really-simple-home'),
    ...
                    </pre>
                <div>
                    <a href='/really_simple_home'>
                        Back to home.
                    </a>
                </div>

"""
    )
