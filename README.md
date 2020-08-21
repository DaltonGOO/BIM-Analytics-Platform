![Image Alien](https://github.com/DaltonGOO/BIM-Analytics-Platform/blob/master/06_Images/Logo%20v3%20WIth%20just%20the%20Alien_25.png)

# BIM-Analytics-Platform
Open Source BIM Analytics Platform. 

## Functional Requirements
- Allow users to change the interface and pick what data is shown
- Have multiple options for viewing the data
- monitor data | such as Revit warnings, large models, large amount of clashes
- track data when users are not online
- data security | an option to share the data


## Tools to track / ever-increasing
- Revit_log and journal files
  - Revit Clinic Journal File Parser 2011 
    https://revitclinic.typepad.com/my_weblog/2011/11/journal-file-parser.html
  - Visualizing Revit Journals
    https://insidethefactory.typepad.com/my_weblog/2012/02/visualizing-journals.html
  - Revit Journal file
    %LOCALAPPDATA%\Autodesk\Revit\Autodesk Revit ####\Journals
  - Revit Log file
- Navisworks_log and clashes
- Dynamo log file - checkout the data tracking tool Autodesk is using for Dynamo
  - Dynamo log file
    C:\Users\\%USERNAME%\AppData\Roaming\Dynamo\Dynamo Revit\2.5\Logs
- Hypar
- BIM360
- AutoCAD
- SketchUp
- Enscape
  - Enscape main plugin log files:
    C:\Users\\%USERNAME%\AppData\Roaming\Enscape\Data\Logs

  - Revit plugin log files:
    C:\Users\\%USERNAME%\AppData\Local\Temp\Enscape\Logs\EnscapeRevitPlugin



## Database
### Requirements
- Data integrity
- Supported operations
- Modeling relationships
- Supported data types
- Transaction support
- Scalability
- Redundancy
- Schema flexibility
- Performance
- Integrations
  
  
### HDFS 

#### Characteristics
- Files and directories
- Distributed file system
- Any type of file
- Commodity hardware
- Streaming access
- Query support with Hive and Impala

#### Assessment 
- Strengths
  - Linear scaling
  - Redundancy
  - Security
  - High availability
  
- Shortcomings
  - No updates 
  - Limited querying
  - Queries_very slow_bad for live dashboards
  - Not for small data
  
- Applications
  - Raw dumps
  - Media storage
  - Data backups
  
#### Platforms


### RDBMS - Oracle

#### Characteristics
- Tables, rows, columns
- Schema driven
- SQL-based queries
- Number crunching

#### Assessment

- Strenths
  - Transactions
  - Speed
  - Data integrity
  - Security
- Shortcomings
  - Linear scaling
  - Text/media
  - Complex data types
  - Cost
- Applications
  - Master data
  - OLTP
  - Update intensive data
  - Data Warehouse
 


#### Other Platforms
- Microsoft SQL Server
- MySQL
- MariaDB
- PostgreSQL


### Document Databases - MongoDB

#### Characteristics
- JSON documents
- Flexible structures
- Document key
- Indexing
- Sharded clusters

#### Assessment
- Strengths
  - Complex data types
  - Rich querying
  - Full text search
  - Scalability
- Shortcomings
  - No transactions
  - No media storage
  - Joins not optimal
  - No attribute-based security
- Applications
  - Blogs
  - Catalogs
  - RDBMS alternative
  
#### Other Platforms
- Elasticsearch
- Couchbase
  
  
### Research 
- Identify tools - APACHE tools?
  - Apache logs parser with Python for absolute beginners | Projects
    https://www.youtube.com/watch?v=4DdueeIE8Rs&feature=youtu.be
- Build ecosystems


### Review Project Kanban for task
