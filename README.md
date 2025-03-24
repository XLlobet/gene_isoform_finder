# Gene Isoform Finder
## Projects Aim

The **Gene Isoform Finder** is a cutting-edge web application designed to easily find protein sequences (and all its isoforms) by searching a gene name. It simplifies the complex process to find patterns in protein sequences.

Search, and analyze gene isoform sequences from **UniProt** database. It integrates a powerful sequence search and pattern matching functionality, enabling to quickly identify specific patterns within the data.

Central to the application is the **Plotly Dash Bio** library, a suite of bioinformatics components that make it simpler to analyze and visualize bioinformatics data and interact with them in a Dash application.

The **Sequence Viewer** component from Dash Bio, is offering fast, efficient pattern recognition and search capabilities. The application provides an intuitive interface for managing gene isoforms, ensuring ease of use while leveraging the advanced features of the Sequence Viewer component for in-depth analysis

## Technologies and libraries

- Python 3.10.12
- Django 4.2.20
- Dash 2.18.2
- Dash Bio 1.0.2
- Plotly 6.0.0
- HTML.
- CSS.
- Bootstrap.

## Project

1. ### Directory structure.
	All the project directories are named and explained in the next list. At the end of the list there is a structure tree image:
	- **<font size=4>gene_isoform_finder</font>**: This is the <span style="color: green;">**main folder**</span> that contains the <span style='color: lightgreen;'>**seq_viewer**</span> project, and the **requirements.txt** file.

		- **<font size=4><span style='color: lightgreen;'>seq_viewer</span></font>**: This is the project folder that contains the <span style='color: steelblue;'>**seq_viewer**</span> and the <span style='color: lightblue;'>**seq_viewer_app**</span> folders.

			- **<font size=3><span style='color: steelblue;'>**seq_viewer:**</span></font>** Contains all the settings for the Django project.
			- **<font size=3><span style='color: lightblue;'>**seq_viewer_app:**</span></font>** The Django app called **Gene Isoform Finder**. Contains all the front-end and back-end code for the Gene Isoform Finder application, following the Django project structure specifications.

				- **<font size=3>migrations:</font>** Gene Isoform Finder model migrations.
				- **<font size=3>static/ect_tool:</font>** Contains all the files for styling and event management for the **Gene Isoform Finder**. CSS, images, videos, JavaScript and Bootstrap files.
					- **css**: All CSS files for the Gene Isoform Finder style.
					- **img**: Predefined images for the Gene Isoform Finder views.
					- **vendor**: Folder containing Bootstrap, jQuery and jQuery-UI files.
				- **<font size=3>templates/ect_tool:</font>** Contains all the HTML templates for the Gene Isoform Finder.			
		
	- <font size=4>**Directory tree structure**</font>:

 	 	![Directory structure](https://github.com/XLlobet/gene_isoform_finder/blob/main/geneif_tree.png)

2. ### Location of the main function.
      The main door or function of the project, is the ***ìndex()*** function from **views.py** file from ***'gene_isoform_finder/seq_viewer/seq_viewer_app'*** folder. 

3. ### How run the application.
   
   	Install the packages needed using the **requirements.txt** file.
   
	```bash
	pip install -r requirements.txt
	```

	Clone the repository.

	```bash
	git clone git@github.com:XLlobet/gene_isoform_finder.git
	cd gene_isoform_finder/seq_viewer
	```

	Run the application:

	```bash
	python3 manage.py migrate
	python3 manage.py runserver
	```

  	 Visite the app in your brouser at ***http://127.0.0.1:8000/***

