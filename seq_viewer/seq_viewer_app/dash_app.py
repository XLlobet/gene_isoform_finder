#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    Contains the Gene Isoform Finder app
#
# - This file contains the function to generate the Gene Isoform Finder
#   app:
#
# - Funtion is:
#
#       - seq_viewer(): Create a Dash Sequence Viewer app.
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
    It generates a Sequence Viewer application for the entry sequence 
    isoform using the Dash Bio library

    ## Parameters:
        - gene_name (str): the searched gene name. Used in the app title.
        - isoform_sequence (str): the FASTA sequence to display in the app.
        - app_name (str): the Dash Sequence Viewer app name.
        - isoform_numb (str): the number of the gene isoform. Used in the 
        app title.
    '''
    
    # Create the Django Dash application
    app = DjangoDash(app_name)

    # Read the FASTA sequence isoform
    seq = protein_reader.read_fasta(datapath_or_datastring=isoform_sequence,
                                    is_datafile=False)[0]['sequence']

    # Application layout
    app.layout = dbc.Container([

        # HTML P tag for the application title
        html.P( children        = f'{gene_name} Isoform {isoform_numb}',
                className       = 'text-success fs-2 fw-bold'),

        # HTML Div tag for the Sequence Viewer class
        html.Div(
            [dBio.SequenceViewer(
                sequence        = seq,
                charsPerLine    = 40,
                toolbar         = True)]),
    ])
