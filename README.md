#pyak

Pyak is a simple python wrapper for Yik Yak's API.

##Installation

No installation is needed. Simply download pyak.py and place it in the same director as your program, then import pyak in your program.

##Basic Usage


####Creating a Yakker

The Yakker class takes a single optional parameter, a user ID. User IDs are the unique identifier used by Yik-Yak to track individual users. The following will initialize a yakker with the given user ID:

```python
yakker = pyak.Yakker(user_id)
```

If no argument is given, a new yakker will automatically be registered and assigned an ID by the server. You can easily fetch the assigned ID for storage and re-use through Yakker's id property:

```python
yakker = pyak.Yakker()
print "New yakker registered with ID: %s" % yakker.id
```

####Setting Location

You must set a location before most operations:

```python
location = pyak.Location(latitude, longitude)
yakker.update_location(location)
```

Where latitude and longitude are strings represetning the location on Earth.

####Fetching Yaks

The get_yaks() function will fetch a list of the most recent yaks in your area:

```python
yaks = yakker.get_yaks()
for yak in yaks:
  print yak.message
```

####Posting

Posting is simple:

```python
#Note that you must wait a fair amount of time (around a minute) after registering
#before you are allowed to post
yakker.post_yak("Hello World!")
```

##Complete Documentation

A more complete documentation is coming soon.
