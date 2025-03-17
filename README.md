# Gene Isoform Finder
## Projects Aim

The Gene Isoform Finder is a cutting-edge web application designed to easily find protein sequences (and all its isoforms) by searching a gene name.

It simplifies the complex process to find patterns in protein sequences.

## Technologies and libraries

- Python 3.10.12
- Django 5.1.1
- django-debug-toolbar==4.2.0
- django-pandas==0.6.7
- django-plotly-dash==2.4.5
- dash==2.18.2
- dash-bio==1.0.2
- dash-bootstrap-components==1.5.0
- dash-core-components==2.0.0
- dash-html-components==2.0.0
- dash-table==5.0.0
- plotly==6.0.0
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

 	 	![Directory structure](https://github.com/P4kD3v/ect_demo/blob/main/ect_demo%20tree.png?raw=true)

2. ### Location of the main function.
      The main door or function of the project, is the ***ìndex()*** function from **views.py** file from ***'gene_isoform_finder/seq_viewer/seq_viewer_app'*** folder. 

3. ### How run the application.
   
   	Install the packages needed using the **requirements.txt** file.
   
	```bash
	pip install -r requirements.txt
	```

	Clone the repository.

	```bash
	git clone https://github.com/P4kD3v/ect_demo.git
	cd ect_demo/ect_demo
	```

	Run the application:

	```bash
	python3 manage.py migrate
	python3 manage.py runserver
	```

  	 Visite the app in your brouser at ***http://127.0.0.1:8000/***

