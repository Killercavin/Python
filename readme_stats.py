import requests

def get_top_languages():
    # Make a GET request to the GitHub API for the list of trending repositories
    response = requests.get('https://api.github.com/search/repositories?q=stars:%3E1&sort=stars&order=desc')
    if response.status_code == 200:
        repositories = response.json()['items']
        languages = {}

        # Iterate over the repositories and count the occurrences of each language
        for repo in repositories:
            language = repo['language']
            if language:
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 1
        
        # Sort the languages based on the count
        sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        
        # Display the top languages
        for language, count in sorted_languages[:10]:
            print(f"{language}: {count} repositories")
    else:
        print(f"Failed to fetch repository data. Status code: {response.status_code}")

# Call the function to get the top languages
get_top_languages()
