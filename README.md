# KarenPythonCode

Notes from training:

<!-- to display errors at the top of the page
<ul>
{% if errors %}
{% for error in errors %}
    <li> {{error}}</li>
{% endfor %}
</ul>-->


Job appears and disappears
Can call this one with no parameters
Best way to set library list to create profile that can be used to set to list (ie ALUSER4 PGUSER4)
def connect(dsn, user='', password='', host='', database='',
conn_options=None):



persistent job ( like when you set a library list and want to reuse it)
def pconnect(dsn, user='', password='', host='', database='',
conn_options=None):
