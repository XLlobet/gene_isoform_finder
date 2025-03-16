#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    Functions to extract sequences from the UniProt database
#               for the Gene Isoform Finder
#
# - This file contains all the Django framework urñs for the 
#   Gene Isoform Finder:
#
# - Funtions are:
#
#       - get_uniprot_data()
#       - find_fasta_accession()
#
# =====================================================================


# IMPORTS
# =====================================================================

import  json
import  requests
from    requests import Response


# FUNCTION
# =====================================================================

# Get UniProt data 
# ---------------------------------------------------------------------
def get_uniprot_data(entry_search:  str)->str:
    '''
    Find and return UniProt data for the searched protein in the 
    'entry_search' parameter.

    ## Parameters:
        - entry_search (str): the searched word by the user.

    ## Returns a tuple of:
        - uniprot_response_str (str): the raw sequence as a FASTA string.
    '''

    # Input searching word:
    search_word:            str     = entry_search

    # Organism. Always human, or can be homo sapiens also.
    organism:               str     = "human"

    # Url where to ask and get the data:
    uniprot_search:         str     = f"https://rest.uniprot.org/uniprotkb/search?query=\
                                        {search_word}+{organism}\
                                        &fields=accession,id,protein_name,gene_names,organism_name,length"
    
    # Get response data as string:
    uniprot_search_resp:    str     = requests.get(uniprot_search).text

    # Convert response data to a python's dictionary:
    uniprot_response_dict:              dict        = json.loads(uniprot_search_resp)
    # Check results. 'results' is the only key in the dictionary:
    uniprot_results_list:               list[dict]  = uniprot_response_dict['results']
    # Set variables where to store the data:

    entries_found:                      list        = []
    # entries_related:                    list        = []
    # fastas_dict:                        dict        = {}
    # is_match:                           bool        = False

    # If there is not result:
    if len(uniprot_results_list) <= 0:
        uniprot_response_str:   str         = 'Gene not found'
        
    # If there is a result:
    else:

        # Travel all the result entries:
        for entry in uniprot_results_list:
            # Get accession number and UniProt Id
            accession:                  str         = entry['primaryAccession']
            uniprot_id:                 str         = entry['uniProtkbId']
            # Find gene name::
            # gene_name: str = find_gene_name(entry)
            # Check if the search value is in the UniProt Id:
            if search_word.upper()+"_"+organism.upper() in uniprot_id:

                # Get FASTA sequence:
                uniprot_response_str:   str         = find_fasta_accession(accession)
                            
            # If search value is not in the UniProt Id:
            else:
                pass

        if entries_found == []:
            
            uniprot_search:             str         = f"https://rest.uniprot.org/uniprotkb/search?query=gene_exact:{search_word}+AND+organism_id:9606&fields=accession,id,protein_name,gene_names,organism_name,length"
            # Get response data as string:
            uniprot_search_resp:        str         = requests.get(uniprot_search).text
            # Convert response data to a python's dictionary:
            uniprot_response_dict:      dict        = json.loads(uniprot_search_resp)
            # Check results. 'results' is the only key in the dictionary:
            uniprot_results_list:       list[dict]  = uniprot_response_dict['results']
            # Set variable for UniPrpot response
            uniprot_response_str:       str         = ''
            # If there is not result:
            if len(uniprot_results_list) <= 0:
                pass
            else:
                entry:                  dict        = uniprot_results_list[0]
                accession:              str         = entry['primaryAccession']
                uniprot_id:             str         = entry['uniProtkbId']
                # Find gene name:
                # gene_name:              str         = find_gene_name(entry)
                uniprot_response_str                = find_fasta_accession(accession)
            

    return uniprot_response_str


# Search for protein fasta sequence
# ---------------------------------------------------------------------
def find_fasta_accession(accession: str)->str:
    '''
    Search for fasta sequence from accession id in the UniProt
    database, and return the raw sequence as string.

    ## Parameters:
        - accession (str): UniProt accession id for the searched
        protein.

    ## Return:
        - uniprot_response_str (str): the raw sequence as string.
    '''
    # Url where to ask and get fasta/s of the searched word:
    uniprot_search_fastas:  str         = f"https://rest.uniprot.org/uniprotkb/search?format=fasta&includeIsoform=true&query=accession%3A{accession}"
    # Get data:
    uniprot_fastas_resp:    Response    = requests.get(uniprot_search_fastas)
    # Get response data as string:
    uniprot_response_str:   str         = uniprot_fastas_resp.text

    return uniprot_response_str


