import urllib2
import boto

print boto.Version
response = urllib2.Request('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
html = urllib2.urlopen(response)
the_k = html.read()

key1, key2 = the_k.split(':')
print(key1)
print(key2)
