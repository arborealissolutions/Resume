"""
Made by Andrew Freund
This script is being utilized to generate a resume using Python
"""
from reportlab.pdfgen import canvas
import os


def create_features(typing, string, x, y, x1=0, x2=0, font_type='', font_size=0):
    """
    Used to create the various graphic elements on the page by provding a template.
    :param typing: What type of graphic element; Center, String (single line), Line, or Multi (longer text)
    :param string: What is the text being added, if applicable\
    :param x: x axis
    :param y: y axis
    :param x1: x axis 2
    :param x2: y axis 2
    :param font_type:
    :param font_size:
    :return:
    """

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

# fileName = r'C:\Users' + chr(92) + os.environ["USERNAME"] + r'\Downloads\FreundAndrew_Resume.pdf'
fileName = r'C:\Users\andre\Downloads\FreundAndrew_Resume.pdf'
documentTitle = 'FreundAndrew_Resume'
fullName = 'Andrew Freund'
contactInformation = [
    'REDACTED',
    'REDACTED',
]
education = [
    'Miami University, Oxford OH',
    'Bachelor of Arts',
]
metaData = [
    'Created using Python, Reportlab',
    'For source code, go to GitHub:',
    'https://tinyurl.com/freundresume'
]
latestJob = 'Reporting and Data Science Analyst'
latestEmployer = 'Independent Contractor, Fully Remote'
latestTime = 'January 2023 - Present'
latestDesc = [
    'Created, updated, and maintained Stored Procedures in Microsoft SQL to ensure proper reporting and data analytics. Updated PowerBI interfaces and ',
    'adjusted DAX and visual compontents. Utilized Windward reporting to generate reports for internal and external clients. Participated in SCRUM ',
    'and utliized Sprints to ensure workflows and business logic were in place in a timely manner. Attened daily stand ups and one-on-ones with ',
    'the data and reporting team. Created a database diagram to understand the system and how it interconnects as a late-arrival in a fast-paced ',
    'start up environment.'
]
previousJob = 'Database Administrator and Developer (Database Specialist)'
previousEmployer = 'Hamilton County Public Health, Cincinnati OH'
previousTime = 'November 2019 - January 2023'
previousDesc = [
    'Responsible for creating, maintaining, and updating production level relational databases (Microsoft SQL, '
    'POSTGRESQL, and Microsoft Access ',
    'databases for agency-wide programs and projects. Utilized SQL, Python, PowerShell, VBA, and C# to '
    'create tools and procedures to improve IT ',
    'efficiency and response rate. Used Python scripting to automate the creation and maintenance of GIS data layers '
    'through ArcPY, both locally and on ',
    'the web. Developed various data cleaning and verification tools to improve reliability of in agency-wide tools.'
]
job1 = 'GIS Specialist (Public Health Sanitarian I)'
employer1 = 'Hamilton County Public Health, Cincinnati OH'
time1 = 'October 2018 - November 2019'
desc1 = [
    'Developed and maintained department GIS data, including managing, updating, and processing data for hosting on '
    'ArcGIS Online. Utilized Python ',
    'scripts to manage routine updates, query non-GIS data, and join existing layers with databases. Represented '
    'organization by attending inter-governmental ',
    'advisory committee and bringing back relevant information to superiors. Created field data collection '
    'applications tied to existing ESRI products.',
    'Followed and applied State code during routine inspections on septic systems',
]
job2 = 'AmeriCorps VISTA Member'
employer2 = 'Calhoun County Land Bank Authority, Marshall MI'
time2 = 'July 2017 - July 2018'
desc2 = [
    'Built capacity at host organization, which included streamlining program review processes, '
    'grant funded project tracking, and creating ',
    'a Neighborhood Health Index for the City of Albion through the data collection and cleaning followed by the '
    'application of ArcGIS methodologies',
]
job3 = 'GIS Associate'
employer3 = 'Miami University, Oxford OH (Contract with Butler County Board of Developmental Disabilities)'
time3 = 'February 2017 - May 2017'
desc3 = 'Responsible for repopulating and verifying data in databases and ArcGIS layers, in addition to generating ' \
        'more in-depth and functional maps utilizing ArcGIS'
job4 = 'Researcher'
employer4 = 'Miami University, Oxford OH'
time4 = 'February 2016 - May 2017'
desc4 = [
    'Began research on ecosystem service provision in exurban parcels containing at least one pond, including '
    'creating a raster land use map and training ',
    'remote sensing analysis, identifying uses and desires of individuals living in isolated rural parcels that lead '
    'to publication ',
    '(https://www.mdpi.com/2073-445X/10/5/448)',
]
job5 = 'GIS Associate'
employer5 = 'Miami University, Oxford OH (Contract with Miami University Police Department, Parking Services)'
time5 = 'February 2015 - May 2015'
desc5 = 'Assisting in creating a web map, gathering data, and digitizing parking locations, both individually and in ' \
        'a team, required time management skills'
skillHeader1 = 'Technology and Communication'
skillSet1 = [
    'Assisted in managing grant funded project management (physical and electronic) and intra-team communication',
    'Utilized knowledge of scripting to create queries for contractor reports to allow for analysis and quality '
    'improvement of processes',
    'Interacted with internal and external customers over the phone, through email, or in person, providing'
    'information and assistance',
    'Successfully maintained productivity while working remotely and kept superiors up to date on the status of '
    'projects',
    'Developed the remote work scripts that allowed staff to effectively work remotely due to the COVID-19 Pandemic',
    'Used best practices (ETL) to parse data from various sources into a database structure, and then into various '
    'applications and functions',
    'Produced various processes and applications that allowed staff to interact with various data sources '
    'at a production level',
    'Moved manual services into automated processes that freed up staff time and increased reliability',
    'Developed, updated, and tested Stored Procedures for various purposes; reporting, platform widgets, and other analytic functions',
    'Leveraged PowerBI to display business data and to drill into summary data from platform widgets; providing an in-depth look at the data on request'
]
skillHeader2 = 'Geospatial Analysis (ArcGIS 10.X, ENVI 5.X, ArcPY)'
skillSet2 = [
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
    'and public were up-to-date',
    'Generated weekly reports, including heat maps, of COVID-19 cases in Hamilton County, OH',
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
    'Participatated in SCRUM and AGILE workflows'
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
create_features('Center', fullName, 100, 780,
                font_type=fontTypeBase, font_size=titleSize)
# Contact Information
create_features('Multi', contactInformation, 200, 788,
                font_type=fontTypeBase, font_size=textSize)

# Create Guide/Formatting Lines
create_features('Line', '', 0, 770, 550, 770)
create_features('Line', '', 550, 770, 550, 50)
create_features('Line', '', 0, 50, 550, 50)

# Education Header and Line
create_features('String', 'Education', 40, 748,
                font_type=fontTypeBold, font_size=14)
# Education String
create_features('Multi', education, 110, 754,
                font_type=fontTypeBase, font_size=textSize)

# Separator Line between Education and Experience
create_features('Line', '', 0, 730, 550, 730)
create_features('Line', '', 400, 770, 400, 730)
create_features('Multi', metaData, 405, 758,
                font_type=fontTypeBase, font_size=textSize)

# Experience Header
create_features('String', 'Experience', 40, 714,
                font_type=fontTypeBold, font_size=14)

# Current Job
create_features('String', latestJob, 40, 700,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', latestEmployer, 40, 688,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', latestTime, 325, 695,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', latestDesc, 50, 678,
                font_type=fontTypeBase, font_size=textSize)

# Previous Job
create_features('String', previousJob, 40, 620,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', previousEmployer, 40, 608,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', previousTime, 325, 615,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', previousDesc, 50, 596,
                font_type=fontTypeBase, font_size=textSize)

# Job 1
create_features('String', job1, 40, 550,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', employer1, 40, 538,
                font_type=fontTypeBase, font_size=headerSize)
create_features('String', time1, 325, 545,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', desc1, 50, 526,
                font_type=fontTypeBase, font_size=textSize)

# Job 4
# create_features('String', job4, 40, 520,
#                 font_type=fontTypeBase, font_size=headerSize)
# create_features('String', employer4, 40, 508,
#                 font_type=fontTypeBase, font_size=headerSize)
# create_features('String', time4, 325, 515,
#                 font_type=fontTypeBase, font_size=headerSize)
# create_features('Multi', desc4, 50, 496,
#                 font_type=fontTypeBase, font_size=textSize)

# Skills and Qualifications Header
create_features('String', 'Skills and Qualifications', 40,
                478, font_type=fontTypeBold, font_size=14)

# Technology and Communication
create_features('String', skillHeader1, 40, 462,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet1, 50, 450,
                font_type=fontTypeBase, font_size=textSize)

# GIS
create_features('String', skillHeader2, 40, 350,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet2, 50, 338,
                font_type=fontTypeBase, font_size=textSize)

# Research and Analysis
create_features('String', skillHeader3, 40, 230,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet3, 50, 218,
                font_type=fontTypeBase, font_size=textSize)

# Leadership, Collaboration, and Teamwork
create_features('String', skillHeader4, 40, 146,
                font_type=fontTypeBase, font_size=headerSize)
create_features('Multi', skillSet4, 50, 134,
                font_type=fontTypeBase, font_size=textSize)

# save the pdf
pdf.save()
os.system(fileName)
