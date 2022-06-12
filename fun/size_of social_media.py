from concurrent.futures import ProcessPoolExecutor as Executor

urls = """google twitter facebook youtube pinterest tumblr
instagram reddit flickr meetup classmates microsoft apple
linkedin xing renren disqus snapchat twoo whatsapp""".split()


def fetch(url):
  from urllib import request, error
  try:
    data = request.urlopen(url).read()
    return "{} : len {}".format(url, len(data))
  except Exception as e:
    return "{} : exception {}".format(url, e)

with Executor(max_workers=5) as ex:
  temp = 'https://www.{}.com'
  jobs = [ex.submit(fetch, temp.format(u)) for u in urls]
  result = [job.result() for job in jobs]


print('\n'.join(result))