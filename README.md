# IPFS Instagram Mirror

IPFS based protocol for mirroring/archiving instagram accounts

This project allows creation of an IPFS based mirror or archive for Instagram accounts. It contains to parts, separated into two respective folders. The first part (the `ipfs-mirror-local` folder) contains a script to format an Instagram information requests for an account into a mirror. The second part (the `ipfs-mirror-webview` folder) contains a simple React-based website which allows to explore said mirror.

## IPFS Mirror Local

In order to create a mirror for your instagram account, the steps are as follow:

1. From a Web Browser, log into your Instagram account and head into Settings -> Privacy and Security -> Data Download -> Request Download. It can also be found in the mobile app in a similar way.
2. Request the HTML version to your e-mail address, and once you have it download the zip file into the `ipfs-mirror-local` folder.
3. Unzip it and rename the resulting folder to `account_info_download`
4. Run the python script. In general, it should be `python3 createMirror.py` on Mac and Linux and `python createMirror.py` for Windows. Make sure you have Python installed as well as the `bs4` library (it can be installed with `python3 -m pip install bs4` or `python -m pip install bs4`). After running it, it should generate a `mirror-(username)` folder.
5. Upload this folder to IPFS. With the CLI installed, run:
```bash
ipfs add mirror-(username) -r
```
The CID should be displayed.

6. It might be a good idea to add a IPNS entry, which would look something like this:
```bash
ipfs name publish /ipfs/(your CID here)
```

## IPFS Mirror Webview

The website can be seen live [here](https://ipfs-instagram-mirror.vercel.app). After entering the IPFS address on the top input, wait for the content to load and display. Try `/ipfs/QmSDo1SuD4CT6kZyrKf2yXtfvLadQMyx5aRP2eVi8cojAp` for a sample.
