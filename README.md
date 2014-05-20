#pyak
--------

Pyak is a simple python wrapper for Yik Yak's API.

##Basic Usage


####Creating a Yakker

The Yakker class takes a single optional parameter, a user ID. User IDs are the unique identifier used by Yik-Yak to track individual users. The following will initialize a yakker with the given user ID:

```python
yakker = Yakker(user_id)
```

If no argument is given, a new yakker will automatically be registered and assigned an ID by the server. You can easily fetch the assigned ID for storage and re-use through Yakker's id property:

```python
yakker = Yakker()
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
