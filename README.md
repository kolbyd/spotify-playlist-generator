# Spotify Playlist Converter
### Developed by [Kolby Dunning](https://kolbyd.ca) (kolbyd)

## Setup
### Spotify
If you do not have a Spotify account, ensure that you have that first.

Go to [developer.spotify.com](https://developer.spotify.com/) and log in with your account. Create a new
app, and go into it. Click 'edit settings', add `http://localhost:8080/callback/` as your redirect URI.

Copy the client ID and secret to add to the `.env` file.

The file should be the same as the one shown below:
```
# .env
SPOTIFY_CLIENT_ID={your client ID}
SPOTIFY_CLIENT_SECRET={your client secret}
```

If you run `Main.py` and you don't have the variables set or the file doesn't exist, you will told by the
CLI.

### Python
This project was built in Python 3.8. If you don't currently have Python, please visit 
[python.org/downloads](https://www.python.org/downloads/).

1. Run `pip install -r requirements.txt` to install the dependencies.
1. Fill in the required fields in `.env` (if you haven't already)
1. Run `python Main.py`
1. Follow the steps from the CLI.

## Contribution Guide
I always appreciate contributions to my work. I prefer pull requests over issues, but both work.

### Pull Request
- Please document your code when required
- Explain the modifications you made in the description
- What did you solve? Why is this a good addition?

### Issues
Even though it is labeled issues, feel free to add new feature requests as well.

- Say what the issue/feature is.
- Why does this need to be fixed/why is it a good addition?
- How would you reproduce (if it's an issue)?

## Help/Questions?
Please email me at [kolby[at]kolbyd.ca](mailto:kolby@kolbyd.ca).