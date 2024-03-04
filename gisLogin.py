from arcgis import GIS
import keyring
from getpass import getpass

# Purpose: Sample code for creating a Credential Manager entry for ArcGIS login

URL = "" # URL to ArcGIS Enterprise or AGOL environment

def gisLogin(): # Supporter function for retrieving GIS object via login with Windows Credential Manager
    username = input("Username:")
    credStore = keyring.get_password(service_name=f"{username}@arcgis_python_api_profile_passwords", username=username) # Check whether credentials already stored
    if credStore is None: # if credentials don't already exist, store via new CredManager entry
        print(f"Credential Manager entry for user {username} not found.\nCreating new entry...")
        gis = createCredstore(username)
    else: # If credentials already stored, proceed with login
        try:
            gis = GIS(profile=username)
        except: # If credentials are invalid, overwrite with new credentials
            print("Unable to log in with stored credentials, overwriting Credential Manager entry...")
            gis = createCredstore(username)
    return gis

def createCredstore(username): # Function for creating a CredManager entry for ArcGIS login
    success = False
    while success == False:
        password = getpass("Password:")            
        try:
            gis = GIS(url='', username=username, password=password, profile=username) # Create credential manager entry under username
            success = True
            print(f"Successfully created Credential Manager entry for {username}")
        except Exception as e:
            print(e)
    return gis
