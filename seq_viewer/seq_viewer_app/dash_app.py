from    dash                        import  html, dcc, Output, Input
import  dash_bio                    as      dBio
from    dash_bio.utils              import  protein_reader
from    django_plotly_dash          import  DjangoDash
import  dash_bootstrap_components   as      dbc

def seq_viewer(gene_name:           str, 
               isoform_sequence:    list,
               app_name:            str,
               isoform_numb:        int):

    app = DjangoDash(app_name)

    seq = protein_reader.read_fasta(datapath_or_datastring=isoform_sequence,
                                    is_datafile=False)[0]['sequence']

    app.layout = dbc.Container([

        html.P( children        = f'{gene_name} Isoform {isoform_numb}',
                className       = 'text-success fs-2 fw-bold'),

        html.Div(
            [dBio.SequenceViewer(
                sequence        = seq,
                charsPerLine    = 40,
                toolbar         = True)]),
    ])
    
    