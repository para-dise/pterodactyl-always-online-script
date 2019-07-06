# pterodactyl-always-online-script
A script to keep your servers running 24/7. Don't worry about downtimes anymore.

The script will be run every 2 minutes, it can be configured tho.


Installation Instructions:

- Make sure you have python installed. (Latest version as of now for Windows: https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
- Make sure you have pip installed.
- Make sure you have the requirements installed (py -m pip install -r requirements.txt) - the requirements.txt file is in this repo.
- Navigate to https://panel.your.host/account/api/new and create an API key.
- Go back to https://panel.your.host/account/api and click the little key icon under the API, and copy the API key.
- Open the downloaded script in Notepad or your prefered browser. Edit line 6, change "YOUR_API_KEhttps://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exeY" to the copied API key.
- Go to https://panel.your.host/ and copy your IDs and replace the IDs in line 10. If you only have 1 server, it will look like ["your_server_id"]. If you have more, add this to the IDs already there: ``, "your_other_api_key"`` so that it will look as such ``["0aa00000", "0aa00aaa", "aa000aa0"]``.
- Edit line 11 and change your host URL without adding a forward slash. Eg ``baseurl = "https://panel.freemc.host"``.
- Open CMD and type ``py [drag your script here]``
- Leave the script running 24/7.
