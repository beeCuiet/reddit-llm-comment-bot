# Reddit LLM Comment Bot
This simple python script allows users to programatically comment on the most recent post of a desired subreddit using a Large Language Model to generate the contents of the comment.

## Setup
### Dependencies
You must have the following dependencies on your local machine. The versions are not strictly required but the versions listed below have been tested for compatibility.
- **ollama** v0.1.22
    - This package is not the same as the package that's needed for the Python script!
- **Python** v3.11.6


You must also run the following command in the project directory
`pip install -r requirements.txt`

### Credentials
You must set the following environment variables with your credentials after creating credentials to access the [Reddit API](https://old.reddit.com/prefs/apps/). The environment variables will be used by the Python Reddit API Wrapper (praw) for authentication with the Reddit API.
- `REDDIT_CLIENT_ID`: Reddit API Client ID
- `REDDIT_CLIENT_SECRET`: Reddit API Client Secret
- `REDDIT_USERNAME`: The username for your Reddit account
- `REDDIT_PASSWORD`: The password for your Reddit account

## Run
```bash
python main.py $model $subreddit $prompt
```

- `$model` is a string that represents an [ollama model](https://ollama.ai/library). This script has been tested with llama2 and llama2-uncensored. Compatibility with other models may require slight tweaks to the script. The model must be installed on your local machine.
- `$subreddit` is a string that represents the Subreddit that the script should fetch the latest posts for.
- `$prompt` is a string that will be used when providing context to the model. The script will add the title and text at the end of the supplied prompt.

The script will only post a comment if the authenticated user has not previously commented on the same post.