# WolfLease

An application to help people find apartments/flats offering rooms on sublease

<a href="https://github.com/subodh30/WolfLease/actions">![GitHub Workflow Status](https://img.shields.io/github/workflow/status/subodh30/WolfLease/Django%20CI)</a>&nbsp;&nbsp; ![GitHub](https://img.shields.io/github/license/subodh30/WolfLease)&nbsp;&nbsp; ![GitHub top language](https://img.shields.io/github/languages/top/subodh30/WolfLease)&nbsp;&nbsp; ![GitHub issues](https://img.shields.io/github/issues/subodh30/WolfLease) ![GitHub closed issues](https://img.shields.io/github/issues-closed/subodh30/WolfLease)&nbsp;&nbsp; [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7178274.svg)](https://doi.org/10.5281/zenodo.7178274)&nbsp;&nbsp; [![codecov](https://codecov.io/gh/subodh30/WolfLease/branch/master/graph/badge.svg?token=65T3AK0FVG)](https://codecov.io/gh/subodh30/WolfLease)
 

## Getting started:

  - ### Prerequisite:
      - Download [Python3.8](https://www.python.org/downloads/) on your system.

  - ### Run Instructions

     **To run the site locally:**

     - Clone [this (Wolflease) github repo](https://github.com/subodh30/WolfLease).

     - Navigate to project directory.

     - Create a virtual environment:

        `python -m venv project_env`
    
     - Activate the virtual environment: 

        `source project_env/bin/activate`
    
     - Build the virtual environment:

        `pip install -r requirements.txt`

        
  
     - Run:
     
        `python manage.py runserver`

     - Site will be hosted at:
       `http://127.0.0.1:8000/`

### Endpoints

#### Admin page

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/admin/ | Admin page |

#### Owner

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/owners | Create new Owner |
|`PUT`|http://localhost:8000/owners/{ownerId} | Update Owner by ID |
|`GET`|http://localhost:8000/owners/ | Get all Owners |
|`DELETE`|http://localhost:8000/owners/{ownerId} | Delete Owner by ID |

#### Apartment

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/apartments | Create a new Apartment |
|`PUT`|http://localhost:8000/apartments/{apartmentID} | Update Apartment by ID |
|`GET`|http://localhost:8000/apartments/ | Get all Apartments |
|`DELETE`|http://localhost:8000/apartments/{apartmentID} | Delete Apartment by ID |

#### Lease

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/lease | Create a new Lease |
|`PUT`|http://localhost:8000/lease/{LeaseID} | Update Lease by ID |
|`GET`|http://localhost:8000/lease/ | Get all lease |
|`DELETE`|http://localhost:8000/lease/{LeaseID} | Delete Lease by ID |

#### Flat

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/flats | Create a new Flat |
|`PUT`|http://localhost:8000/flats/{flatID} | Update Flat by ID |
|`GET`|http://localhost:8000/flats/ | Get all Flats |
|`DELETE`|http://localhost:8000/flats/{flatID} | Delete Flat by ID |


#### User

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/users | Create a new User |
|`PUT`|http://localhost:8000/users/{userID} | Update User by ID |
|`GET`|http://localhost:8000/users/ | Get all Users |
|`DELETE`|http://localhost:8000/users/{userID} | Delete User by ID |

#### Interested

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/interests | Create a new Interest |
|`PUT`|http://localhost:8000/interests/{interestID} | Update Interest by ID |
|`GET`|http://localhost:8000/interests/ | Get all Interests |
|`DELETE`|http://localhost:8000/interests/{interestID} | Delete Interest by ID |

## Team Members
[Subodh Gujar](https://github.com/subodh30)

[Ameya Vaichalkar](https://github.com/ameyagv)

[Rohan Shiveshwarkar](https://github.com/RoninS28)

[Kunal Patil](https://github.com/kunalpatil1810)

[Yash Sonar](https://github.com/Yash-567)
