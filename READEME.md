# Live Site 
[Live AWS Site](https://main.d34w62a2yjwt5r.amplifyapp.com/)

# General 
This website and web app features a functional CRM for tracking real estate leads for real estate investors or wholesalers.

The website features information about the company and their acquisition process. This serves as a funnel in marketing the business and features a submission form for potential sellers to provide contact information and basic information on their property.

The administration has a seperate web app that allows them to track and document leads through the process of speaking with the potential sellers.

The initial deployment will be solely a frontend user website that allows them to submit leads to be added to our database. Future deployments will include the admin user interface for more advanced features and functionality.

## Frontend Logic 
[Frontend Repo](https://github.com/la-flor/RE_CRM_frontend)

## Sneak Peak
Here's a link to check out a mockup of the admin web app interface that is yet to come.
[Figma Mockup](https://www.figma.com/file/Fg7EdGPna0HIXhIKU7hh01/RE_CRM?node-id=0%3A1)
> Hold cmd while scrolling to zoom in and out. 

> Use a click and drag method (or use your scroll wheel alone) to move along the x and y axis.

# Local Viewing
While in the frontend directory in your terminal interface:

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask run
```

Server will run on [http://localhost:3001](http://localhost:3001) to prevent conflicting running of ports with frontend.

# Database
In order for our application to properly store our data, a Postgres database must be created, properly seeded, and running.

```bash
createdb RE_CRM
python seed.py
```