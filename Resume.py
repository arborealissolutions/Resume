# Made by Andrew Freund
from reportlab.pdfgen import canvas
import os


def create_features(typing, string, x, y, x1=0, x2=0, font_type='', font_size=0):
    if typing == 'Center':
        pdf.setFont(font_type, font_size)
        pdf.drawCentredString(x, y, string)

    elif typing == 'String':
        pdf.setFont(font_type, font_size)
        pdf.drawString(x, y, string)

    elif typing == 'Line':
        # pdf.line(0, 750, 600, 750)
        # pdf.line(400, 750, 400, 0)
        pdf.line(x, y, x1, x2)

    elif typing == 'Multi':
        text = pdf.beginText(x, y)
        text.setFont(font_type, font_size)

        for line in string:
            text.textLine(line)

        pdf.drawText(text)
        # text = pdf.beginText(200, 770)
        # text.setFont(fontTypeBase, textSize)
        #
        # for line in contactInformation:
        #     text.textLine(line)

        # pdf.drawText(text)

    else:
        return print('Nothing Selected')


# Creating a resume using Python
# Initializing initial variables
titleSize = 20
headerSize = 11
textSize = 8
fontTypeBase = 'Times-Roman'
fontTypeBold = 'Times-Bold'


fileName = r'C:\Users' + chr(92) + os.environ["USERNAME"] + r'\Downloads\FreundAndrew_Resume.pdf'
documentTitle = 'FreundAndrew_Resume'
fullName = 'Andrew Freund'
contactInformation = [
    'Cincinnati, OH',
    'Redacted for Internet Safety',
]
education = [
    'Miami University, Oxford OH',
    'Bachelor of Arts',
    'Urban and Regional Planning, Sustainability, GISci Certificate',
]
metaData = [
    'Created using Python, Reportlab',
    'For source code, go to GitHub:',
    'https://tinyurl.com/freundresume'
]
latestJob = 'Database Administrator and Developer (Database Specialist)'
latestEmployer = 'Hamilton County Public Health, Cincinnati OH'
latestTime = 'November 2019 - Present'
latestDesc = [
    'Responsible for creating, maintaining, and updating production level relational databases (Microsoft SQL, '
    'POSTGRESQL, and Microsoft Access ',
    'databases for agency-wide programs and projects. Utilized T-SQL, Python, PowerShell, VBA, and C# to create tools '
    'and procedures to improve IT ',
    'efficiency and response rate. Used Python scripting to automate the creation and maintenance of GIS data layers '
    'through ArcPY, both locally and on ',
    'the web. Developed various data cleaning and verification tools to improve reliability of in agency-wide tools.'
]
previousJob = 'GIS Specialist (Public Health Sanitarian I)'
previousEmployer = 'Hamilton County Public Health, Cincinnati OH'
previousTime = 'October 2018 - November 2019'
previousDesc = [
    'Developed and maintained department GIS data, including managing, updating, and processing data for hosting on '
    'ArcGIS Online. Utilized Python ',
    'scripts to manage routine updates, query non-GIS data, and join existing layers with databases. Represented '
    'organization by attending inter-governmental ',
    'advisory committee and bringing back relevant information to superiors. Created field data collection '
    'applications tied to existing ESRI products.',
    'Followed and applied State code during routine inspections on septic systems',
    ]
job1 = 'AmeriCorps VISTA Member'
employer1 = 'Calhoun County Land Bank Authority, Marshall MI'
time1 = 'July 2017 - July 2018'
desc1 = [
    'Built capacity at host organization, which included streamlining program review processes, '
    'grant funded project tracking, and creating ',
    'a Neighborhood Health Index for the City of Albion through the data collection and cleaning followed by the '
    'application of ArcGIS methodologies',
    ]
job2 = 'GIS Associate'
employer2 = 'Miami University, Oxford OH (Contract with Butler County Board of Developmental Disabilities)'
time2 = 'February 2017 - May 2017'
desc2 = 'Responsible for repopulating and verifying data in databases and ArcGIS layers, in addition to generating ' \
        'more in-depth and functional maps utilizing ArcGIS'
job3 = 'Researcher'
employer3 = 'Miami University, Oxford OH'
time3 = 'February 2016 - May 2017'
desc3 = [
    'Began research on ecosystem service provision in exurban parcels containing at least one pond, including '
    'creating a raster land use map and training ',
    'remote sensing analysis, identifying uses and desires of individuals living in isolated rural parcels that lead '
    'to publication ',
    '(https://www.mdpi.com/2073-445X/10/5/448)',
    ]
job4 = 'GIS Associate'
employer4 = 'Miami University, Oxford OH (Contract with Miami University Police Department, Parking Services)'
time4 = 'February 2015 - May 2015'
desc4 = 'Assisting in creating a web map, gathering data, and digitizing parking locations, both individually and in ' \
        'a team, required time management skills'
skillHeader1 = 'Geospatial Analysis (ArcGIS 10.X, ENVI 5.X, ArcPY)'
skillSet1 = [
    'Created a parking survey for Downtown Cleveland, Ohio, highlighting the location, type, and capacity, '
    'and street signage',
    'Created a land cover image of Butler County, Ohio',
    'Designed a Neighborhood Health Index of the City of Albion, Michigan',
    'Created Python scripts to backup, update, and manage datasets with ArcGIS and external databases.',
    'Built ArcGIS Online web maps and tied them to ArcGIS Explorer and Collector for increasing the effectiveness '
    'of field staff',
    'Prepared data and maps for internal projects throughout the organization',
    'Gathered data from member jurisdictions for internal quality improvement measures',
    'Used widgets in ArcGIS Online to improve the quality and effectiveness of programs within the organization',
    'Utilized the ArcPY framework to create various data cleaning, preparation, and management processes to ensure '
    'datasets used by staff',
    'and public were accurate and up-to-date',
    'Generated weekly reports, including heat maps, of COVID-19 cases in Hamilton County, OH',
]
skillHeader2 = 'Communication and Technology'
skillSet2 = [
    'Conducted in-class and client-public presentations, while maintaining clear communication both before and after',
    'Improved upon visual communication skills with Adobe Photoshop, Illustrator, InDesign, and SketchUp',
    'Assisted in managing grant funded project management (physical and electronic) and intra-team communication',
    'Utilized knowledge of scripting to create queries for contractor reports to allow for analysis and quality '
    'improvement of processes',
    'Interacted with internal and external customers over the phone, through email, or in person, providing'
    'information and assistance',
    'Successfully maintained productivity while working remotely and kept superiors up to date on the status of '
    'projects',
    'Developed the remote work scripts that allowed staff to effectively work remotely due to the COVID-19 Pandemic',
    'Used best practices to parse data from various sources into a database structure, and then into various '
    'applications and functions',
]
skillHeader3 = 'Research and Analysis'
skillSet3 = [
    'Completed independent research with a faculty adviser on exurban growth patterns and their ecological effects',
    'Experience in both technical and legal reading, writing, and analysis',
    'Created an analytical framework for a Neighborhood Health Index for a rural small town',
    'Researched and evaluated potential contractors, companies, and programs for projects and/or agency-wide needs',
    'Analyzed various data sources, including contents, to ensure viability and usefulness of data',
    'Connected and integrated Microsoft SQL, PostgreSQL, MySQL, Geodatabases, and ArcGIS Server in a production '
    'environment',
    'Georeferenced GIS data to tabular data and vice-versa on a regular basis',
]
skillHeader4 = 'Leadership, Collaboration, and Teamwork'
skillSet4 = [
    'Served as president and corporate officer responsible for the Society for Creative Anachronism, '
    'a non-profit organization',
    'Facilitated classroom discussion with mixed masters and undergraduate classes',
    'Lead and coordinated various groups, maintaining clear communication with professor and group members',
    'Collaborated with other VISTA team members and leader to create events and programs',
    'Worked on a continuous quality improvement project within organization',
    'Implemented improvements based on feedback from leadership and users based on their usage of tools and '
    'functions',
]
skillHeader5 = ''
skillSet5 = [
    '',
]

# Creating a pdf object
pdf = canvas.Canvas(fileName)
# Setting the title of the document
pdf.setTitle(documentTitle)

# Name
create_features('Center', fullName, 100, 780, font_type=fontTypeBase, font_size=titleSize)
# Contact Information
create_features('Multi', contactInformation, 200, 788, font_type=fontTypeBase, font_size=textSize)

# Create Guide/Formatting Lines
create_features('Line', '', 0, 770, 550, 770)
create_features('Line', '', 550, 770, 550, 50)
create_features('Line', '', 0, 50, 550, 50)

# Education Header and Line
create_features('String', 'Education', 40, 748, font_type=fontTypeBold, font_size=14)
# Education String
create_features('Multi', education, 120, 758, font_type=fontTypeBase, font_size=textSize)

# Separator Line between Education and Experience
create_features('Line', '', 0, 730, 550, 730)
create_features('Line', '', 400, 770, 400, 730)
create_features('Multi', metaData, 405, 758, font_type=fontTypeBase, font_size=textSize)

# Experience Header
create_features('String', 'Experience', 40, 718, font_type=fontTypeBold, font_size=14)

# Current Job
create_features('String', latestJob, 40, 706, font_type=fontTypeBase, font_size=headerSize)
create_features('String', latestEmployer, 40, 694, font_type=fontTypeBase, font_size=headerSize)
create_features('String', latestTime, 325, 700, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', latestDesc, 50, 682, font_type=fontTypeBase, font_size=textSize)

# Previous Job
create_features('String', previousJob, 40, 640, font_type=fontTypeBase, font_size=headerSize)
create_features('String', previousEmployer, 40, 628, font_type=fontTypeBase, font_size=headerSize)
create_features('String', previousTime, 325, 635, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', previousDesc, 50, 616, font_type=fontTypeBase, font_size=textSize)

# Job 1
create_features('String', job1, 40, 570, font_type=fontTypeBase, font_size=headerSize)
create_features('String', employer1, 40, 558, font_type=fontTypeBase, font_size=headerSize)
create_features('String', time1, 325, 565, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', desc1, 50, 546, font_type=fontTypeBase, font_size=textSize)

# Job 3
create_features('String', job3, 40, 520, font_type=fontTypeBase, font_size=headerSize)
create_features('String', employer3, 40, 508, font_type=fontTypeBase, font_size=headerSize)
create_features('String', time3, 325, 515, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', desc3, 50, 496, font_type=fontTypeBase, font_size=textSize)

# Skills and Qualifications Header
create_features('String', 'Skills and Qualifications', 40, 462, font_type=fontTypeBold, font_size=14)

# GIS Skills
create_features('String', skillHeader1, 40, 450, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet1, 50, 438, font_type=fontTypeBase, font_size=textSize)

# Technology and Communication
create_features('String', skillHeader2, 40, 330, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet2, 50, 318, font_type=fontTypeBase, font_size=textSize)

# Research and Analysis
create_features('String', skillHeader3, 40, 238, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet3, 50, 226, font_type=fontTypeBase, font_size=textSize)

# Leadership, Collaboration, and Teamwork
create_features('String', skillHeader4, 40, 154, font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet4, 50, 142, font_type=fontTypeBase, font_size=textSize)

# save the pdf
pdf.save()
# os.system(fileName)
