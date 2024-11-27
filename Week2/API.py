import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get(
    "https://itunes.apple.com"
)