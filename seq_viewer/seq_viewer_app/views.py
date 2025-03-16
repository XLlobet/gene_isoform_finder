#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    ECT (Demo) views
#
# - This file contains all the Django framework views for the 
#   Endometrial Cancer Tool (Demo).
#
# - The views are divided in different fields/sections:
#
#   - Home
#
# - Home site for a summary of the ECT purpose and the data used.
#
# - EC Tool (Demo), can plot with no need of statistical knowledge, Progression-Free
#   and Overall survival for some clinical categories.
#
# =====================================================================
# IMPORTS
# =====================================================================


from django.shortcuts   import render
from .                  import dash_app
from .                  import uniprot_db

# Create your views here.

def index(request):
    '''
    This function returns the Sequence Viewer view.
    '''

    if request.method == 'GET':

        context: dict = {'title':           'Gene Isoform Finder'}

        return render(request, 'seq_viewer_app/base.html', context)
    
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

                current_app_name: str   = f"SequenceViewer{isoform_numb}"
                app_names_list.append(current_app_name)

                dash_app.seq_viewer(input_gene.upper(),
                                    isoform,
                                    current_app_name,
                                    isoform_numb)
                
                isoform_numb = isoform_numb + 1
            
            context['apps_list']        = app_names_list
            context['result']           = f"<span class='text-success'>Gene found: {input_gene.upper()}</span>"

        return render(request, 'seq_viewer_app/base.html', context)