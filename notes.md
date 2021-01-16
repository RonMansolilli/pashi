

## PASHI Log/Notes ##

**30 Dec**
- Discussion with Austen on expanding framework documentation, utilizing Panda's to manipulate datasets, utilizing django filter backend module, drop_all null, and merge.  Also discussion on utilizing extended user-model, many-to-many models, etc.

**2 Jan**
- Research on Customer User Model, further refinements to documentation and project guide

**4 Jan**
- Project approved.  Moved directory, files, and set up new repository.  Tested for functionality and accuracy.  Study/Research on custom user model.

**5 Jan**
- Many to many model -> look at ManyToManyField (as alternative to Join table).  Back-study on Django project initialization and folder management.
- Started building out CSS Framework.  

**6 Jan**
- Attempted coup/insurrection in U.S. - little distracted, but still managed to build out a rough CSS Framework for UI.

**7 Jan**
- Continued building out framework (lots of CSS manipulation, research, and trial/error), built initial logo, formatting UI.  
  - <IDEA> add public comments for properties?  Maybe it's counter-productive - maybe just a simple thumbs up/down, etc..</IDEA>
  - Issue trying to making column match previous column height.  <put on back-burner - not required for MVP>

**8 Jan**  

- Completed framework (...as is - i.e. time to move on). Re-did on logo, built mini-logo, finished formatting landing page with skeleton framework and place holders and data-logic.  
- In the 'main' area (UI)
  - Put choices for searching (dropdowns)?
  - On load Display: 1) for anonymous user (alphetical list of housing), i.e. Default Result OR 2) if user log-ins; saved units (if any)
  - On search Display results; unit (from housing_data) and the associated neighborhoood info (from neighborhood_data)</center>
  - If user is logged in, results should also include ability for user to save and take notes.

**11 Jan**

- Research, tutorials, and refamiliarization with SQL, excel scripting/macro, and data manipulation.

**12 Jan** 

- Building .csv files for database implementation, researched and downloaded latest datasets from City of Portland.  Began data manipulation.  Added zips to 350 rows.  

**13 Jan**
 
- Building out master .csv file. 
- Future fields:  neighborhood, avgRent, rentLow, rentHigh, walkIndex, quadrant, numCrimes, violenceIndex, crimeTime
- Made minor alterations to web UI

**14 Jan**

- Utilized SQL scripts to populate data in working crime csv file - populated zip codes, crime count, crime severity.  Deleted non-matching or null values in both datasets (especially those with non-matching zip_codes).  
- Researched django built-in many-to-many relationships - went with using the built in many-to-many djnago field (which auto generated join table)

**15 Jan**

- Finally completed all models, built API (and serializers). 
- Populated database with data.  
- Encountered issues with a 'float to string' error'.  Lots of issues due to transferring data in manually to the database (resolved with troubleshooting serializers and models). 

**16 Jan** 

- Completed testing in database admin page and django object browser (via django). Objects can be saved, altered in both neighborhood & housing data tables. 
- Further altered serializers and models to ensure easy future upgrades. 
- Update documentation and notes.

**17 Jan**

- xxxxxx






