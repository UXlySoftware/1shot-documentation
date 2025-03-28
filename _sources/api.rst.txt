Calling the 1Shot API
----------------------

Once you have funded an `escrow wallet <escrow-wallets.html>`_ and configured a `transaction <transactions.html>`_, you can trigger the transaction 
by making a POST request to the 1Shot API. To do this you'll need to generate a bearer token using your API key and secret.

Create an API key and secret by clicking the "API Keys" on the left-hand navigation bar in the 1Shot console. Click "Create New Key" and give it a name.
This key will be active immediately and can be used to generate a bearer token. If you delete it, it will be permanently deactivated. 

Generating a Bearer Token
=========================

1Shot API uses the `machine-to-machine <https://auth0.com/blog/using-m2m-authorization/>`_ (M2M) flow for authentication. This means you'll need to 
generate a bearer token to authenticate your requests.

.. image:: ./_static/api/api-key-creation.gif
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

It is now time to hit the chain! You will trigger a transaction by making a POST request to ``https://api.1shotapi.com/v0/transactions/{TRANSACTION_ENDPOINT_ID}/execute`` with your JWT. 
The call will look like this:

.. code-block:: bash

    # Transfer 1 ERC-20 token to address 0xE936e8FAf4A5655469182A49a505055B71C17604 would look something like this
    curl -X POST https://api.1shotapi.com/v0/transactions/{TRANSACTION_ENDPOINT_ID}/execute \
        -H "Authorization: Bearer YOUR_BEARER_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"params": {"to": "0xE936e8FAf4A5655469182A49a505055B71C17604", "value": "1000000000000000000"}}' | jq .

where the JSON object under ``params`` is the input data you configured your `transaction <transactions.html>`_ endpoint to accept and ``TRANSACTION_ENDPOINT_ID`` 
is the ID of the transaction endpoint you want to call. The `USDC example <transactions.html#example-base-usdc-transfer>`_ from the 
transactions page would have the same payload structure as this. 

List Available Transaction Endpoints
====================================

Get a JSON list of all transactions currently configured under your organization.

.. code-block:: bash

    curl -X GET https://api.1shotapi.com/v0/business/{ORGANIZATION_ID}/transactions \
        -H "Authorization: Bearer YOUR_BEARER_TOKEN" | jq .