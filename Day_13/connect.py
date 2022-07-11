import pandas as pd
import requests
import pprint
import pandas

api_key ="d4112166a4ae329db18162df3ac2d31f"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNDExMjE2NmE0YWUzMjlkYjE4MTYyZGYzYWMyZDMxZiIsInN1YiI6IjYyY2I0OGM3NTk1YTU2MTJiYTEwOWNiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._vz0teilmM5CnpvwUJIHR9rnlHJw3eOwtLdT1Ja8EGY"
# HTTP requests

# What's my endpoint (or url)

# What is the HTTP method I need

"""

endpoint
Get: /movie/{movie_id}
example: https://api.themoviedb.org/3/movie/550?api_key=d4112166a4ae329db18162df3ac2d31f
"""

#Version 3
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
# pprint.pprint(endpoint)
# r= requests.get(endpoint) # data={"api_key":api_key})
# print(r.status_code)
# print(r.text)


# Version 4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers= {
    'Authorization': f"Bearer {api_key_v4}",
     'Content-Type': 'application/json;charset=utf-8'

}
# r= requests.get(endpoint, headers=headers)
#
# print(r.status_code)
# print(r.text)


api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        #print(results[0].keys())
        movie_ids=set()
        for result in results:
            _id = result['id']
            # print(result["title"], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = 'movies.csv'
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)
df=pd.DataFrame(movie_data)
print(df.head)
df.to_csv(output, index=False)