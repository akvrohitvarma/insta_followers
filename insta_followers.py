import requests

def followers(username):
    url = 'https://www.instagram.com/' + username
    r = requests.get(url).text
    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'
    followers = str(r[r.find(start)+len(start):r.rfind(end)])
    result = f"{username} currently has {int(followers):,} followers."
    return result

if __name__ == "__main__":
    username = input("Please enter Instagram id: ")
    print(followers(username))
else:
    print("Enter correct id, you've entered an incorrect one!!")