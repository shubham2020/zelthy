# Zelthy

Django Super User:-

Username :- shubham

Password :- pathakji

## Installation guide
1. Create a python virtual environment with python2.7
2. Activate the virtual environment
3. Install all the dependencies in the requirements.txt file
4. Setup the Database, Username and Password configuration in settings.py file inside the zelthy
   folder
5. Run the server > python manage.py runserver 0.0.0.0:8000

## Pushing data to the database
1. Open the dataPushSrcCode folder 
2. To Generate fresh data :- Uncomment line 53 and comment out line 55 in
   purchaseModelDataGeneration.py to generate data to push to database on the fly
   
   To use the pre-Computed data :- make no changes
3. To push the data to the database run > python3 dataPushingScript.py from the same directory

## Opening the graph page
1. Open http://0.0.0.0:8000/purchase/data-retrieve/ in the browser to get the graph
2. Select start date and it will show the total quantity in a month corresponding to all the
   months in the following year from the start date