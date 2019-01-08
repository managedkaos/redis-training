import redis
import json

# connect to redis
r = redis.Redis(
    host='localhost',
    password='',
    decode_responses=True)

sampleObject = {
  'name': {
    'first': 'Salvatore'
  },
  'location': ['Campobello di Licata'],
  'github': 'https://github.com/',
  'age': 40
}
key = 'sal'
firstNameJsonPath = '.name.first'

# delete the key to start fresh.
r.delete(key)
# remember, values in ReJSON must be proper JSON as strings, thus `json.dumps`
r.execute_command('json.set',key,'.',json.dumps(sampleObject))

firstName = r.execute_command('json.get',key,firstNameJsonPath)
print("First name ({}): {}".format(firstNameJsonPath,firstName))

# write code to set the `last` field in the `name` object to "Sanfilippo"
# write code to append "Sicily" to the `location` array
# write code to increment `age` to 41

finalJSONStr = r.execute_command('json.get',key,'.')
finalDict = json.loads(finalJSONStr)
print('The entire object is:')
print(json.dumps(finalDict, indent=2))
print("- The last name should be set to 'Sanfilippo': {}".format(finalDict["name"]["last"] == 'Sanfilippo'))
print("- The location should have two elements and the 2nd one should be 'Sicily': {}".format(finalDict["location"][1] == 'Sicily'))
print("- The age should be 41: {}".format(finalDict["age"] == 41))
