import requests
#use API for random integers
response = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
r = response.text
comp_sequence = r.replace('b', '').replace('\n', '')
