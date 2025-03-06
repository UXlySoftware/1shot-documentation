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

You can generate a bearer token by making a POST request to ``api.1shotapi.com/v0/token`` with your API key and secret in the request body:

.. code-block:: bash

    curl -X POST https://api.1shotapi.com/v0/token \
        -H "Content-Type: application/json" \
        -d '{"key": "my-key", "secret": "secret-key"}'

This will return a JWT token that you can use to authenticate your requests to the 1Shot API. You can drop it into `JWT.io <https://jwt.io>`_ to inspect 
the payload.

Triggering a Transaction
========================

It is now time to hit the chain! You will trigger a transaction by making a POST request to ``api.1shotapi.com/v0/{transaction-endpoint-id}/execute`` with your JWT. 
The call will look like this:

.. code-block:: bash

    curl -X POST api.1shotapi.com/v0/{TRANSACTION_ENDPOINT_ID}/execute \
        -H "Authorization: Bearer YOUR_BEARER_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"params": {"to": "address", "amount": "1"}}'

Where the JSON object under ``params`` is the input data you configured your transaction endpoint to accept. 
