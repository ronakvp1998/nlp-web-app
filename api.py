import paralleldots

paralleldots.set_api_key('YW8XAPnCh2gk5NPSDQ4NwJ7JIluoqJ6KIC2vc8omTAE')

def ner(text):
    ner = paralleldots.ner(text)
    return ner