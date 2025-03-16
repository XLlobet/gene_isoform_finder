#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    Gene Isoform Finder views
#
# - This file contains all the Django framework views for the 
#   Gene Isoform Finder.
#
# - The views are divided in different fields/sections:
#
#   - Home
#
# - Home site allows to search and find gene sequences of its
#   isoforms.
#
# - Gene Isoform Finder, can search and find gene isoform sequences
#   extracted from UniProt database.
# =====================================================================


# IMPORTS
# =====================================================================

from django.shortcuts   import render
from .                  import dash_app
from .                  import uniprot_db


# VIEWS
# =====================================================================

def index(request):
    '''
    This function returns the landing view of Gene Isoform Finder.
    '''

    # If GET request
    if request.method == 'GET':

        context: dict = {'title':           'Gene Isoform Finder'}

        return render(request, 'seq_viewer_app/base.html', context)
    
    # If POST request
    if request.method == 'POST':

        input_gene:         str         = request.POST['gene_name']
        fasta_sequence:     str         = uniprot_db.get_uniprot_data(input_gene)       

        context:            dict        = {'title':           'Gene Isoform Finder',
                                           'seq_viewer_app':  'seq_viewer_app'}
        
        if fasta_sequence == 'Gene not found':
            
            dash_app.seq_viewer('')
            
            context['result']           = f"<span class='text-danger'>{fasta_sequence}: {input_gene.upper()}</span>"
        
        else:
            isoforms:       list[str]   = fasta_sequence.split("\n>")
            isoforms_list:  list[str]   = [isoform if '>' in isoform else f'> {isoform}' for isoform in isoforms]
            isoform_numb:   int         = 1
            app_names_list: list        = []

            for isoform in isoforms_list:

                current_app_name: str   = f"GeneIsoformFinder{isoform_numb}"
                app_names_list.append(current_app_name)

                dash_app.seq_viewer(input_gene.upper(),
                                    isoform,
                                    current_app_name,
                                    isoform_numb)
                
                isoform_numb = isoform_numb + 1
            
            context['apps_list']        = app_names_list
            context['result']           = f"<span class='text-success'>Gene found: {input_gene.upper()}</span>"

        return render(request, 'seq_viewer_app/base.html', context)