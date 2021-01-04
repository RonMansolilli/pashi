## PASHI Documentation ##
*Last updated:  04 Jan 2020*

Working Link: https://mansolilli.com/pashi/test.html  
Future Link: https://mansolilli.com/pashi/
## ##  
**PASHI -> Portland Affordable, Safe Housing Initiative**  
*"Giving those in need an ability to find, not only affordable, but SAFE housing in the City of Portland."*

### Project Information

Obtaining affordable housing in the City of Portland (CoP) is challenging; finding affordable housing that is also safe and desirable is even more challenging especially for those in need.  This app is designed to allow users to view their options and make informed decisions based on a location factoring in its safety for themselves and/or families.

### Features

- List all available units in the Portland Area designated ‘affordable’
- List out safest units in Portland area (ranked)
- Allow users to login, establish profile, save units, and make notes.  
- Designed for mobile use (those in need may not have access to computers)

### Project Outline

&ensp; Section 1.  Administration.  Setting up project admin, mapping project, etc.  
&ensp; Section 2.  App Framework.  Building out shell and UXI.  Ensuring user login works.    
&ensp; Section 3a.  Prepping Datasets.  Building out datasets with appropriate data.  
&ensp; Section 3b.  App Backend.  Building out models, logic, and API.    
&ensp; Section 4.  App Frontend.  Add functionality to the UXI - make input/output functions usable.  
&ensp; Section 5.  Formatting UX.  Final formatting for overall website and polished UX.  
&ensp; Section 6.  Testing/Rollout.  Independent testing. Fix edge cases, bugs.  
&ensp; Section 7.  Post Rollout/Future Features.

### Project Milestones


  | Week 1                  | Week 2                        | Week 3                          | Week 4                        |
  | ----------------------- | ----------------------------- | ------------------------------- | ----------------------------- |
  | S1. Admin Start/Finish  | S2. (MVP) Framing Finish      | S3b. (MVP) Backend Finish       | S5. (MVP) UX Dev Start/Finish |
  | S2. Framing Start       | S3a. Prep Data Start/Finish   | S4. (MVP) Frontend Start/Finish | S6. Testing/Rollout           |
  |                         | S3b. Backend Start            |                                 |                               |

### Languages/Libraries/Frameworks

- Django REST / Vue.js
- CSS / HTML
- Javascript
- Python

### S1. Administration

**Tasks:**

  - [x] a. Intro to Github and project management
  - [x] b. Buildout hosting area / Set up file structure
  - [x] c. Setup app documentation and formatting style (readme.md)
  - [x] d. Create project milestone framework
  - [x] e. White board project
  - [x] f. Identify data required
  - [x] g. Model the models (see Section 3b)
  - [x] h. Naming conventions/general coding notes

**Notes on tasks:**

a. Utilizing modified Agile Framework with MVP milestones at set stages.  

f. Datasets
   - Primary:  
     - Crime_Data *Obtained from CoP Crime Datasets  
     - Housing_Data *Obtain from CoP or Oregon State data website (API)  
   - Secondary:    
     - Zip-code info associated with unique Portland Areas  
     - Zip-code info associated with housing data addresses  

h. Code naming convention  
   - Variables (single value):  camelCase  
   - Lists/Arrays:  name_name  

### S2. App Framework

  **Tasks:**
   - [ ] a. Build django framework in project folder  
         - Start Django project documentation  
         - Create app
         - Configure settings, admin, urls
   - [ ] b. Build out first model  
         - See section S3b  
         - Activate Models  
         - Testing  
   - [ ] c. Build CSS Structure with place holders  
         - Setup static templates, images, and static folders  
         - Testing
   - [ ] d. Build user functionality (login/logout/register)   
         - Customer User Model  
   - [ ] e. Build user registration page and login templates  
         - Configure with Django  
   - [ ] f. Show welcome user info (on login)
         - Testing and QA

### S3a. Dataset Prep

  **Tasks:**
  - [ ] a. Pull datasets from CoP or figure out if an API call would work
  - [ ] b. Pull zip code dataset based on Portland neighborhoods
  - [x] c. Pull 2020 crime dataset from CoP crime data site and evaluate
  - [ ] d. Build out crime_index as noted in methodology
  - [ ] e. Build out housing_data as noted in methodology


  **Crime Data Methodology:**
```
-> raw Crime Data -> scrub for anomalies and null data  
-> merge data with zip code dataset   
-> rank Crimes based on severity (i.e. assign value -> new field)   
-> add up value of crimes based on zip codes (intValue) -> new list crime_index

**crime_index = [{'id' : idNum, ‘zipCode#’: intValue,}]**  
(better name? safety_rank?)  
```
  **Housing Data Methodology:**  
```  
-> raw Housing Data (or API) -> scrub and sanitize  
-> merge data with zip code data based on addresses (create new field)

**housing_data = [{'id' : idNum, 'zipCode' : 'zipCode#', etc., }]**
```  

**Integrity and accuracy:**  
Testing ongoing at each stage of manipulation to ensure data integrity.  

**Discussion on dataset logic**:  
The crime_index could be derived in a number of ways; however, for the purposes of this app/project, the value of the offense type will be given a value of 1-20 (i.e. murder = 20, parking violation = 1) and then summed by zip-code to develop an ‘index’.  This methodology could potentially skew data (in a circumstance of a high murder rate, low overall occurance of crime), however, it appears to make the most sense over counting the number of crimes in an area (i.e. averaging data based on the severity of crime vs. treating all crimes as equal).  

### S3b. Backend

  **Tasks:**
  - [ ] a. Build out Models
  - [ ] a. Build out API
  - [ ] a. Test models

  **Models**

  ```
  crime_index = [               // Crime index
    {'id' : sysAssigned,        // * Utilize to rank locations
    ‘zipCode#’: intValue,}      // * Ties broken by overall crime occurence
  ]
  ```
  ```
  housing_data = [             // Housing data with incorporated zip data
    {'id' : idNum,
    'zipCode' : 'string',
    'address' : 'string',
    'phoneContact' : 'string',
    }
  ]
  ```
  ```
  user_data = [                  // Standard user data
    {'id' : sysAssigned,
    'userName : 'string',
    'userPwd : sysAssigned,
    'firstName' : 'string',
    'lastName' : 'string',
    }
  ]
  ```
  ```
  join_table = [                 // Join table will link users to saved housing units
    {'id' : sysAssigned,         // many-to-many relationship btw user_data and housing_data
    'user_data.id' : integer,
    'housing_data.id' : integer,
    'userNotes' : 'string',
    }
  ]
  ```

### S4. Frontend  

  **Features:**
  - Should allow anonymous users access to search functionality (but no saving/notes)
  - Registered users (when logging in) will auto-populate saved unit_search (or null if none)
  - Reg users will also have access to notes (under each unit)
  -

  **Tasks:**
  - [ ] a. Populate drop down search box (unit_search) with unit names and a 'show all option'
  - [ ] b. Populate drop down search box (location_search) with unit locations (by zip or area?)
  - [ ] c. Build on_selection function to return/output single unit or multiple units based on unit_search
  - [ ] d. Build on_selection function to return/output all units when location_search called ()
  - [ ] e. Format output from both unit_search and location_search to include crime_index (safety_rank?)
  - [ ] f. Ensure all output is returned based on crime_index in descending order.  
  - [ ] g. Format output to include a Save option_box
  - [ ] h. Dynamically provide user_notes text box on selection
  - [ ] i. <blank placeholder for more tasks>

### S5. Formatting Display (UXI)

  **Tasks:**
  - [ ] a. Polish display for professional appearance
  - [ ] b. Ensure compatibility with mobile devices (**PRIORITY**)

### S6. Testing/Rollout

  **Tasks:**
  - [ ] a. Test on multiple individuals and multiple platforms
  - [ ] b. Debug and polish
  - [ ] c. Finish documentation

### S7. Future

**Future Development:**
  - Build project to utilize ARCgis to display maps and locations visually.  
  - Add Walkability index as a search parameter
