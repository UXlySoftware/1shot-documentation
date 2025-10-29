Calling the 1Shot API
----------------------

Once you have funded a `wallet </basics/wallets.html>`_ and configured a `contract method </basics/contract-methods.html>`_, you can create an onchain transaction from it by making a POST request to the 1Shot API. To do this you'll first need to generate a bearer token using your API key and secret.

Create an API key and secret by clicking the "API Keys" tab on the left-hand navigation bar in the 1Shot API console. Click "Create New Key" and give it a name.
The API key & secret will be active immediately and can be used to generate a bearer token. If you delete it, it will be immediately and permanently deactivated. 

Generating a Bearer Token
=========================

1Shot API uses the `machine-to-machine <https://auth0.com/blog/using-m2m-authorization/>`_ (M2M) flow for authentication. This means you'll need to 
generate a bearer token to authenticate your requests.

.. image:: ../_static/api/api-key-creation.gif
   :alt: Creating an API key
   :align: center

.. raw:: html

   <br />

You can generate a bearer token by making a POST request to ``api.1shotapi.com/v0/token`` with your API ``key`` and ``secret`` in the request body:

.. code-block:: bash

    curl -X POST https://api.1shotapi.com/v0/token \
        -H "Content-Type: application/json" \
        -d '{"grant_type": "client_credentials", "client_id":"{YOUR_API_CLIENT_ID}", "client_secret": "{YOUR_API_CLIENT_SECRET}"}'

This will return with a code 200 and a JSON payload with your access token:

.. code-block:: bash

    {
        "access_token": "string",
        "token_type": "Bearer",
        "expires_in": 0,
        "scope": "string"
    }

You can drop your access token into `JWT.io <https://jwt.io>`_ to inspect its properties. 

The bearer token expires after 1 hour, after which you'll need to generate a new one.

Triggering a Transaction
========================

It is now time to hit the chain! You will trigger a transaction by making a POST request to ``https://api.1shotapi.com/v0/methods/{CONTRACT_METHOD_ID}/execute`` with your JWT. 
The call will look like this:

.. code-block:: bash

    # Transfer 1 ERC-20 token to address 0xE936e8FAf4A5655469182A49a505055B71C17604 would look something like this
    curl -X POST https://api.1shotapi.com/v0/methods/{CONTRACT_METHOD_ID}/execute \
        -H "Authorization: Bearer YOUR_BEARER_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"params": {"to": "0xE936e8FAf4A5655469182A49a505055B71C17604", "value": "1000000000000000000"}}' | jq .

where the JSON object under ``params`` is the input data you configured your `contract method </basics/contract-methods.html>`_ endpoint to accept and ``CONTRACT_METHOD_ID`` is the ID of the contract method endpoint you want to call. The `USDC example </basics/contract-methods.html#example-base-usdc-transfer>`_ from the 
transactions page would have the same payload structure as this.  

List Available Contract Methods
====================================

Get a JSON list of all transactions currently configured under your organization.

.. code-block:: bash

    curl -X GET https://api.1shotapi.com/v0/business/{BUSINESS_ID}/methods \
        -H "Authorization: Bearer YOUR_BEARER_TOKEN" | jq .

See our `OpenAPI specification </api/openapi.html>`_ for a complete reference of all 1Shot API endpoints.

Client SDKs
===========

You can use the official 1Shot API client SDKs to interact with the API rather than making raw HTTP requests:

- `Python <https://pypi.org/project/uxly-1shot-client/>`_
- `Typescript <https://www.npmjs.com/package/@uxly/1shot-client>`_