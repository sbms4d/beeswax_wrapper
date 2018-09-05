# Beeswax Wrapper

The beeswax wrapper is a python API for the beeswax DSP

## Imports
```python
>>> from beeswax_wrapper import BeeswaxAPI, configure_endpoint
```
`BeeswaxAPI` is the main interface to the package. 
It allows for seamless communication with the true beeswax API.
The API lazily loads a `BeeswaxDAL` to access the API and manage authentication state. 
The `BeeswaxDAL` is shared among all BeeswaxAPI classes.

`get_beeswax_dal()` returns the single `BeeswaxDAL` object used by the apis. 
Modifying the `BeeswaxDAL` object returned by this function affects all `BeeswaxAPI` classes. 
Updates should be made to this dal using the `configure_endpoint` function as follows:
```python
>>> from beeswax_wrapper import BeeswaxAPI, configure_endpoint
>>> api = BeeswaxAPI()
>>> configure_endpoint('http://endpoint.api.beeswax.com/rest/')
>>> api.dal.endpoint_url
'http://endpoint.api.beeswax.com/rest/'
```

## Methods
The `BeeswaxAPI` operates with an object restful structure. 
The basic method calls are organised as `api.<object>.<restful_method>` where the restful methods are:
- retrieve
- list
- create
- update
- delete

Some keywords that are specific to each restful endpoint are supplied but the full list of keywords is available here: 
https://docs.beeswax.com/docs/getting-started

### Examples
```python
>>> from beeswax_wrapper import BeeswaxAPI
>>> api = BeeswaxAPI()

>>> # get account information for an id
>>> api.accounts.retrieve(account_id=4)

>>> # get a list of campaigns
>>> api.campaigns.list()

>>> # delete a lineitem by id
>>> api.line_items.delete(line_item_id=62)

>>> # change user
>>> api.change_user('<username>', '<password>')
>>> # cookies are preserved per class
```

## Exceptions
The `BeeswaxAPI` is metaclassed to raise only a `BeeswaxRESTException`.

## Authentication
The `beeswax_wrapper` authenticates once per `BeeswaxDAL` instance. The authentication is for short connection durations only. 
In the event that a connection times out or is unavailable, the `BeeswaxDAL` will attempt to re-authenticate.
Credentials from the DAL are queried from the os keyring. 

### Adding credentials
```python
$ python beeswax_wrapper/credentials/credential_manager.py
Beeswax Username:
Beeswax Password:
$
```