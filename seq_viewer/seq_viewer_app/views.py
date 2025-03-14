from django.shortcuts   import render
from .                  import dash_app

# Create your views here.

def index(request):
    '''
    This function returns the Sequence Viewer view.
    '''

    if request.method == 'GET':

        context: dict = {'title':           'Sequence Viewer'}

        return render(request, 'seq_viewer_app/base.html', context)
    
    if request.method == 'POST':

        input_sequence: str = request.POST['input_sequence']

        dash_app.seq_viewer(input_sequence)

        context: dict = {'title':           'Sequence Viewer',
                         'seq_viewer_app':  'seq_viewer_app'}

        return render(request, 'seq_viewer_app/base.html', context)