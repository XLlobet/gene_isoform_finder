from    dash                        import  html, dcc, Output, Input
import  dash_bio                    as      dBio
from    django_plotly_dash          import  DjangoDash

def seq_viewer(sequence: str):

    app = DjangoDash("SequenceViewer")

    app.layout = html.Div(
        [dBio.SequenceViewer(
            sequence    = sequence,
            toolbar     = True)])
    