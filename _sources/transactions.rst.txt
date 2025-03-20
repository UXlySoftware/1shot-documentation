Transaction Configuration
==========================

.. note::

    Before you can configure a transaction endpoint, you'll need to provision and fund an `escrow wallet <escrow-wallets.html>`_. 

Transaction endpoints are the core of the 1Shot API. They are the RESTful endpoints you configure to call smart contract functions on the blockchain. 
Each transaction endpoint is linked to a single escrow wallet and can be configured to accept a specific set of input parameters. In order to 
configure a transaction endpoint, you'll need to provide the following information:

1. A target blockchain network (Ethereum mainnet, Binance Smart Chain, Avalanche, etc.)
2. The contract address of the smart contract you want to interact with
3. The name of the function you want to call on the contract
4. Input parameters the function expects
5. (optional) A webhook URL to receive real-time feedback on the transaction status

Once you've configured a transaction endpoint, you can trigger the transaction by making a POST request to the 1Shot API with 
your `API key and secret <api.html>`_. You'll need to graph the ``TRANSACTION_ENDPOINT_ID`` of the endpoint from the 1Shot dashboard.

Example: Base USDC Transfer
---------------------------

.. image:: ./_static/transactions/usdc-example.gif
   :alt: USDC Transfer Example
   :align: center

.. raw:: html

   <br />

In this example, we'll configure a transaction endpoint to transfer USDC tokens from our escrow wallet to a recipient. We'll assume you've 
already created and funded an `escrow wallet <escrow-wallets.html>`_ for the Base L2 network with BaseETH and that it contains some USDC tokens. 

We'll start by clicking the "Create a New Endpoint" button on the Transactions page. Give the endpoint a name and description, then select the
Base L2 network from the dropdown. Fill in the webhook URL if you want to receive real-time feedback on the transaction status.

On the next page, we will enter ``transfer`` as the function name we want to call on the USDC contract address `0x833589fcd6edb6e08f4c7c32d4f71b54bda02913 <https://basescan.org/token/0x833589fcd6edb6e08f4c7c32d4f71b54bda02913>`_.

The ``transfer`` function on the USDC contract expects the following input parameters:

- ``to``: The address to transfer the tokens to which is a primitive type ``address``
- ``value``: The amount of tokens to transfer (USDC has 18 decimal places) which is a primitive type ``uint256``

We'll set both of these parameters to be ``Dynamic`` so because we will pass both of them as input parameters when we call the API endpoit. 

.. hint::

    You can also set parameters to be ``Static`` if you want to hardcode them in the transaction endpoint configuration. This is useful, for example, 
    if you always want to transfer the same amount of tokens every time but to different addresses.

Transaction Parameters
----------------------

At the highest configuration level, input paramerters can be either ``primitive``, ``array``, or ``struct`` types. A ``primitive`` is a type like
``uint`` or ``bool`` that is not composed of other types and is likely the most common input type. An ``array`` is a collection 
of the same type of elements, and a ``struct`` is a collection of different types of elements.

Static vs Dynamic Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuring a transaction endpoint, input parameters can be either ``Static`` or ``Dynamic``. Parameters set to ``Static`` will be hardcoded in the
transaction endpoint configuration and are not specified in the request payload when calling the API. Parameters set to ``Dynamic`` will be passed as 
input parameters when calling the API and can be different for each transaction. See `Calling the 1Shot API <api.html>`_ for more information on how 
to trigger a transaction.

.. important::

    Only primitive types are supported for static parameters. Dynamic parameters can be primitive types or compound types like structs and arrays.
    If your function takes a compound type, you'll need to pass it as a JSON object in the request payload.

Struct and Array Inputs
~~~~~~~~~~~~~~~~~~~~~~~

If the function you want to call takes a struct or array as an input parameter, you'll need to define the structure of the input in the transaction
endpoint builder. Take the following example in which the input parameter is a struct which itself contains a ``uint128``, ``string``, and ``array`` of booleans:

.. code-block:: solidity

    struct Foo {
        uint128 fooUint128;
        string fooString;
        bool[] fooBoolArray;
    }

    function callFooBar(Foo calldata foo) public {
        emit CalledFoo(foo.fooUint128, foo.fooString, foo.fooBoolArray[0]);
    }

The configuration for the input struct parameter, ``foo``, would look like this:

.. image:: ./_static/transactions/struct-example.png
   :alt: Struct configuration example
   :align: center

.. raw:: html

   <br />

The payload used to `call the API <api.html#triggering-a-transaction>`_ endpoint would look like this:

.. code:: json

    {
        "params": {
            "foo": {
                "fooUint128": 123,
                "fooString": "Hello, World!",
                "fooBoolArray": [true, false, true]
            }
        }
    }

Webhooks
---------

Webhooks are an optional configuration for your transaction endpoints but are highly recommended as they provide immediate feedback to your application once a transaction
has been confirmed on the blockchain network. 1Shot API implements best practices for webhooks are discussed at `webhooks.fyi <https://webhooks.fyi/>`_, which includes
replay protection and forward compatibility. , 

When you configure a webhook, 1Shot will send a POST request to the URL you provide with a JSON payload that looks like this:

.. code:: json

    {
      "eventName": "BusinessCreated",
      "data": {
        "businessId": "c7c34dd2-4068-45b3-b894-081bbe68944d",
        "chain": 11155111,
        "transactionExecutionId": "aefe1058-6a0f-4271-b99c-4753779f9bb1",
        "transactionReceipt": {
          "_type": "TransactionReceipt",
          "blobGasPrice": null,
          "blobGasUsed": null,
          "blockHash": "0xb5e0dec517a6498917c951323cc24ac66d179e9408b84abedc59d203eb0789d7",
          "blockNumber": 7939928,
          "contractAddress": null,
          "cumulativeGasUsed": "9783249",
          "from": "0xD6AC871Ea68dD41774dA321B85e11D094b49aaa8",
          "gasPrice": "4200820",
          "gasUsed": "34770",
          "hash": "0x5a197c403feaf9d923751810e3927f3e73b3c64775a403728c0ffec3e332a497",
          "index": 108,
          "logs": [
            {
              "_type": "log",
              "address": "0x17Ed2c50596E1C74175F905918dEd2d2042b87f3",
              "blockHash": "0xb5e0dec517a6498917c951323cc24ac66d179e9408b84abedc59d203eb0789d7",
              "blockNumber": 7939928,
              "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000",
              "index": 149,
              "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x0000000000000000000000000000000000000000000000000000000000000000",
                "0x00000000000000000000000032dcd6af330461788c378a7204fb72ad83a0e250"
              ],
              "transactionHash": "0x5a197c403feaf9d923751810e3927f3e73b3c64775a403728c0ffec3e332a497",
              "transactionIndex": 108
            }
          ],
          "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000020000000002000000000800000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000800000000000000000000000000000000000000000040002000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000001000000000000000",
          "status": 1,
          "to": "0x17Ed2c50596E1C74175F905918dEd2d2042b87f3"
        },
        "userId": null
      },
      "timestamp": 1742445849,
      "apiVersion": 0,
      "signature": "EAyg4CA2OqpWR/IlklQmYI9QZk7tJK4o4Egfh0kvCP3VwZSD6n2kpJLxrqcPqB59gtE6a6N3zMmfAKevnaDfCQ=="
    }

Webhook Signatures
~~~~~~~~~~~~~~~~~~

1Shot API signs the webhook payload using the `ed25519 <https://en.wikipedia.org/wiki/EdDSA#Ed25519>`_ signature scheme. As shown 
in the example above, signature is included in the JSON payload under the key ``signature``. You should verify the signature using the
public key provided in the transaction details page. The public key is a base64 encoded ed25519 public key that you can use to verify 
the signature.

Here is an example of a `FastAPI <https://fastapi.tiangolo.com/tutorial/>`_ server that verifies authenticates callbacks from 1Shot API:

.. code:: python
    
    from fastapi import FastAPI, Request, HTTPException, Depends
    import json
    import base64
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    from cryptography.exceptions import InvalidSignature

    app = FastAPI()

    async def verify_signature_decorator(request: Request):
        try:
            # Extract the required fields from the request
            body = await request.json()  # Raw request body
            signature = body.pop("signature", None)  # Example header name

            if not signature:
                raise HTTPException(status_code=400, detail="Signature field missing")

            # Decode the signature
            signature_bytes = base64.b64decode(signature)

            # Public key in base64 format from the Transaction Details Page
            pubkey_b64 = "1N7gklNt5gpfMIHhIUR+csMIb7oO4JX7Q7QTdqj7+Qw="
            # Load the public key
            public_key = Ed25519PublicKey.from_public_bytes(
                base64.b64decode(pubkey_b64)
            )
            # Verify the signature
            public_key.verify(signature_bytes, json.dumps(body, separators=(',', ':'), sort_keys=True).encode('utf-8'))
        except InvalidSignature:
            raise HTTPException(status_code=403, detail="Invalid signature")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal error: {e}")

    @app.post("/python", dependencies=[Depends(verify_signature_decorator)])
    async def handle_python_webhook(request: Request):
        return {"message": "Webhook received and signature verified"}

    @app.get('/healthcheck-python')
    async def root():
        return {'message': 'webhook sinker is up!'}

A complete example you can run from your local machine using `ngrok <https://ngrok.com/>`_ tunnels can be 
found `here <https://github.com/UXlySoftware/webhook-sinker>`_. 