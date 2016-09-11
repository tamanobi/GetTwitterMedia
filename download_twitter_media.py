#coding: UTF-8
import urllib2

def dl(source, output):
  # print source, output
  try:
    response = urllib2.urlopen(source)
    with open(output, "wb") as fout:
      fout.write(response.read())
      return 1
  except Exception:
    import traceback
    traceback.print_exc()

def retrieve(obj):
    print 'retrieving'
    urls = []
    entities = []
    if obj.has_key('extended_entities'):
        entities = obj['extended_entities']
    else:
        entities = obj['entities']
    if not entities.has_key('media'):
        print 'no media found.'
        return []
    for media in entities['media']:
        if media['type'] == 'video':
            for variant in media['video_info']['variants']:
                if variant['content_type'] == 'video/mp4':
                    urls.append([media['id_str'], 'video', variant['url']])
                    break
        elif media['type'] == 'photo':
            urls.append([media['id_str'], 'photo', media['media_url_https']])
    print 'retrieved'
    print urls
    return urls
