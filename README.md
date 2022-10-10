# WolfLease

An application service to help people find apartments/flats offering rooms on sublease

<a href="https://github.com/subodh30/WolfLease/actions">![GitHub Workflow Status](https://img.shields.io/github/workflow/status/subodh30/WolfLease/Django%20CI)</a>&nbsp;&nbsp; <a href="https://opensource.org/licenses/MIT">![GitHub](https://img.shields.io/github/license/subodh30/WolfLease)</a>&nbsp;&nbsp; ![GitHub top language](https://img.shields.io/github/languages/top/subodh30/WolfLease)&nbsp;&nbsp; <a href="https://github.com/subodh30/WolfLease/issues">![GitHub issues](https://img.shields.io/github/issues/subodh30/WolfLease)</a>&nbsp;&nbsp; <a href="https://github.com/subodh30/WolfLease/issues?q=is%3Aissue+is%3Aclosed">![GitHub closed issues](https://img.shields.io/github/issues-closed/subodh30/WolfLease)</a>&nbsp;&nbsp; [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7178274.svg)](https://doi.org/10.5281/zenodo.7178274)&nbsp;&nbsp; [![codecov](https://codecov.io/gh/subodh30/WolfLease/branch/master/graph/badge.svg?token=65T3AK0FVG)](https://codecov.io/gh/subodh30/WolfLease)
 


- ## Built with
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="40" height="40"/>
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" width="40" height="40"/>

- **Language used:** Python
- **Libraries used:** Django


## Visual Walkthrough:
https://user-images.githubusercontent.com/65619749/134620802-5fac9f0e-d697-49df-876c-3f5ff7d86e38.mp4

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


## WolfLease Endpoints

#### Admin page

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/admin/ | Admin page |

#### Owner

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/owners | Create new Owner |
|`PUT`|http://localhost:8000/owners/{ownerId} | Update Owner by ID |
|`GET`|http://localhost:8000/owners | Get all Owners |
|`DELETE`|http://localhost:8000/owners/{ownerId} | Delete Owner by ID |

#### Apartment

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/apartments | Create a new Apartment |
|`PUT`|http://localhost:8000/apartments/{apartmentID} | Update Apartment by ID |
|`GET`|http://localhost:8000/apartments | Get all Apartments |
|`DELETE`|http://localhost:8000/apartments/{apartmentID} | Delete Apartment by ID |

#### Lease

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/lease | Create a new Lease |
|`PUT`|http://localhost:8000/lease/{LeaseID} | Update Lease by ID |
|`GET`|http://localhost:8000/lease | Get all lease |
|`DELETE`|http://localhost:8000/lease/{LeaseID} | Delete Lease by ID |

#### Flat

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/flats | Create a new Flat |
|`PUT`|http://localhost:8000/flats/{flatID} | Update Flat by ID |
|`GET`|http://localhost:8000/flats | Get all Flats |
|`DELETE`|http://localhost:8000/flats/{flatID} | Delete Flat by ID |


#### User

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/users | Create a new User |
|`PUT`|http://localhost:8000/users/{userID} | Update User by ID |
|`GET`|http://localhost:8000/users | Get all Users |
|`DELETE`|http://localhost:8000/users/{userID} | Delete User by ID |

#### Interested

|HTTP Method|URL|Description|
|---|---|---|
|`POST`|http://localhost:8000/interests | Create a new Interest |
|`PUT`|http://localhost:8000/interests/{interestID} | Update Interest by ID |
|`GET`|http://localhost:8000/interests | Get all Interests |
|`DELETE`|http://localhost:8000/interests/{interestID} | Delete Interest by ID |

## Searching through Owners, Apartments, Lease, Flats, User Models

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/owners?search={email} | Search for an Owner with given email |
|`GET`|http://localhost:8000/owners?search={contact_number} | Search for an Owner with given contact number |
|`GET`|http://localhost:8000/apartments?search={address} | Search for Apartments by address |
|`GET`|http://localhost:8000/apartments?search={facilities} | Search for Apartments with different facilities of your choice |
|`GET`|http://localhost:8000/apartments?search={owner} | Search for Apartments by owner |
|`GET`|http://localhost:8000/lease?search={lease_end_date} | Search for Lease by end date |
|`GET`|http://localhost:8000/lease?search={lease_start_date} | Search for Lease by start date |
|`GET`|http://localhost:8000/flats?search={availabilty} | Search for Flats that are available |
|`GET`|http://localhost:8000/flats?search={rent_per_room} | Search for Flats by rent amount |
|`GET`|http://localhost:8000/users?search={email} | Search for an User with given email |
|`GET`|http://localhost:8000/users?search={contact_number} | Search for a User with given contact number |

## Team Members
[Subodh Gujar](https://github.com/subodh30)

[Ameya Vaichalkar](https://github.com/ameyagv)

[Rohan Shiveshwarkar](https://github.com/RoninS28)

[Kunal Patil](https://github.com/kunalpatil1810)

[Yash Sonar](https://github.com/Yash-567)
