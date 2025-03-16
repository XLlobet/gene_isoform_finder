#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    Contains the Gene Isoform Finder app
#
# - This file contains the function to generate the Gene Isoform Finder
#   app:
#
# - Funtions is:
#
#       - seq_viewer()
#
# =====================================================================


# IMPORTS
# =====================================================================

from    dash                        import  html
import  dash_bio                    as      dBio
from    dash_bio.utils              import  protein_reader
from    django_plotly_dash          import  DjangoDash
import  dash_bootstrap_components   as      dbc


# FUNCTION
# =====================================================================

def seq_viewer(gene_name:           str, 
               isoform_sequence:    str,
               app_name:            str,
               isoform_numb:        int):
    '''
    It generates a Sequence Viewer application using the Dash Bio library

    ## Parameters:
        - gene_name (str): the searched gene name.
        - isoform_sequence (str): the FASTA sequence.
        - app_name (str): the Dash application name.
        - isoform_numb (str): the number of the gene isoform.
    '''
    
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
    
    