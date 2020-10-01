import yaml

slogan = ['welcome', 'to', 'here']
website = {'url': 'www.51zxw.net'}

print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))