import os
import sys
import ollama
import praw

def hasNotCommented(submission):
    comments = submission.comments.list()
    for comment in comments:
        if comment.author == os.environ["REDDIT_USERNAME"]:
            return False
    return True

def createComment(model, prompt, title, text):
    content = f"""
    {prompt}
    
    This is the title: {title}

    This is the text below:
    {text}
    """
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
    )
    return response["message"]["content"]

def useSubmission(model, prompt, submission):
    title = submission.title
    text = submission.selftext
    if hasNotCommented(submission):
        print(title)
        comment = createComment(model, prompt, title, text)
        submission.reply(comment)

def main():

    model = sys.argv[1]
    subreddit = sys.argv[2]
    prompt = sys.argv[3]

    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent="llm-script",
        username=os.environ["REDDIT_USERNAME"],
    )
    for submission in reddit.subreddit(subreddit).new(limit=1):
        useSubmission(model, prompt, submission)

if __name__ == "__main__":
    main()
