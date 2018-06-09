---
layout: post
title: "Conectar Python con twitter"
date: "2018-06-09 00:50:39 -0400"
---

Primero que nada, debemos crear nuestra en app, twitter develop. Con esto
tendremos accesso a: consumer_key, consumer_secret, access_token, access_secret.

Segundo debemos instalar la libreria tweepy con el siguiente comando:

`pip install tweepy`

Nuestro código debe quedar así:

```Python
import tweepy
from tweepy import OAuthHandler
 
consumer_key    = '#########'
consumer_secret = '#########'
access_token    = '#########'
access_secret   = '#########'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
```

Con esto ya podemos comenzar a jugar con la api de twitter sin dramas.
