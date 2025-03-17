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
# - Home site allows to search and find gene sequences and its
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
        
        # Django template context
        context:            dict        = {'title':             'Gene Isoform Finder',
                                           'field':             'home'}

        return render(request, 'seq_viewer_app/base_home.html', context)
    
    # If POST request
    if request.method == 'POST':

        # Django template context
        context:            dict        = {'title':             'Gene Isoform Finder',
                                           'field':             'home'}

        return render(request, 'seq_viewer_app/base_home.html', context)

        
def gene_isoform_finder(request):
    '''
    This function returns the Gene Isoform Finder view.
    '''

    # If GET request
    if request.method == 'GET':
        
        # Django template context
        context:            dict        = {'title':             'Gene Isoform Finder',
                                           'field':             'gene_isoform_finder'}

        return render(request, 'seq_viewer_app/base_gene_isoform_finder.html', context)
    
    # If POST request
    if request.method == 'POST':

        # Get gene name input
        input_gene:         str         = request.POST['gene_name']

        # Get gene sequence with all isoforms from UniProt
        fasta_sequence:     str         = uniprot_db.get_uniprot_data(input_gene)       

        # Django template context
        context:            dict        = {'title':             'Gene Isoform Finder',
                                           'field':             'gene_isoform_finder'}
        
        # Get gene name not found
        if fasta_sequence == 'Gene not found':
            
            # Add the result message to the template context variables
            context['result']           = f"<span class='text-danger'>{fasta_sequence}: {input_gene.upper()}</span>"
        
        # Get gene name was found
        else:
            # Split gene sequence isoforms
            isoforms:       list[str]   = fasta_sequence.split("\n>")
            isoforms_list:  list[str]   = [isoform if '>' in isoform else f'> {isoform}' for isoform in isoforms]
            
            # Set ther starting number to ennumerate sequence isoforms
            isoform_numb:   int         = 1

            # Set an empty list to store the Dash Sequence Viewer apps.
            # One app name for each isoform
            # It will be sended to the Django template to display the different apps
            app_names_list: list        = []

            # Loop that travels all the isoforms
            for isoform in isoforms_list:

                # Current Dash Sequence Viewer app name
                current_app_name: str   = f"GeneIsoformFinder{isoform_numb}"

                # Store the app name
                app_names_list.append(current_app_name)

                # Create the Dash Sequence Viewer app for the current isoform
                dash_app.seq_viewer(input_gene.upper(),
                                    isoform,
                                    current_app_name,
                                    isoform_numb)
                
                # Update the isoform number
                isoform_numb = isoform_numb + 1
            
            # Add the app names and the result message to the template 
            # context variables
            context['apps_list']        = app_names_list
            context['result']           = f"<span class='text-success'>Gene found: {input_gene.upper()}</span>"

        return render(request, 'seq_viewer_app/base_gene_isoform_finder.html', context)