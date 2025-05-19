TX Configs
==========

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
your `API key and secret <api.html>`_. You'll need to grab the ``TRANSACTION_ENDPOINT_ID`` of the endpoint from the 1Shot dashboard.

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
replay protection and forward compatibility. 

When you configure a webhook, 1Shot will send a POST request to the URL you provide with a JSON payload that looks like this:

.. code:: json

    {
        "eventName": "TransactionExecutionSuccess",
        "data": {
            "businessId": "c7c34dd2-4068-45b3-b894-081bbe68944d",
            "chain": 11155111,
            "logs": [
                {
                    "args": [
                        "0x0000000000000000000000000000000000000000000000000000000000000000",
                        "0xD6AC871Ea68dD41774dA321B85e11D094b49aaa8",
                        "0xA1BfEd6c6F1C3A516590edDAc7A8e359C2189A61"
                    ],
                    "fragment": {
                        "anonymous": false,
                        "inputs": [
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "bytes32",
                                "components": null,
                                "indexed": true,
                                "name": "role",
                                "type": "bytes32"
                            },
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "address",
                                "components": null,
                                "indexed": true,
                                "name": "account",
                                "type": "address"
                            },
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "address",
                                "components": null,
                                "indexed": true,
                                "name": "sender",
                                "type": "address"
                            }
                        ],
                        "name": "RoleGranted",
                        "type": "event"
                    },
                    "name": "RoleGranted",
                    "signature": "RoleGranted(bytes32,address,address)",
                    "topic": "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d"
                },
                {
                    "args": [
                        "0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6",
                        "0xD6AC871Ea68dD41774dA321B85e11D094b49aaa8",
                        "0xA1BfEd6c6F1C3A516590edDAc7A8e359C2189A61"
                    ],
                    "fragment": {
                        "anonymous": false,
                        "inputs": [
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "bytes32",
                                "components": null,
                                "indexed": true,
                                "name": "role",
                                "type": "bytes32"
                            },
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "address",
                                "components": null,
                                "indexed": true,
                                "name": "account",
                                "type": "address"
                            },
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "address",
                                "components": null,
                                "indexed": true,
                                "name": "sender",
                                "type": "address"
                            }
                        ],
                        "name": "RoleGranted",
                        "type": "event"
                    },
                    "name": "RoleGranted",
                    "signature": "RoleGranted(bytes32,address,address)",
                    "topic": "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d"
                },
                {
                    "args": [
                        "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32"
                    ],
                    "fragment": {
                        "anonymous": false,
                        "inputs": [
                            {
                                "arrayChildren": null,
                                "arrayLength": null,
                                "baseType": "address",
                                "components": null,
                                "indexed": false,
                                "name": "token",
                                "type": "address"
                            }
                        ],
                        "name": "TokenCreated",
                        "type": "event"
                    },
                    "name": "TokenCreated",
                    "signature": "TokenCreated(address)",
                    "topic": "0x2e2b3f61b70d2d131b2a807371103cc98d51adcaa5e9a8f9c32658ad8426e74e"
                }
            ],
            "transactionExecutionId": "57335f5e-7fc4-406f-ae9e-670b561ff7d9",
            "transactionExecutionMemo": "{\"tx_type\":0,\"associated_user_id\":5034284669,\"note_to_user\":\"{\\\"name\\\":\\\"Test\\\",\\\"ticker\\\":\\\"TES\\\",\\\"description\\\":\\\"test token\\\",\\\"image_file_id\\\":\\\"AgACAgEAAxkBAAIDfWgiPNEzB-K22SSCR1JSs-i7gjb7AALgrTEbgroQRVyOzOUCHxPMAQADAgADeQADNgQ\\\"}\"}",
            "transactionId": "528c4ba0-e288-47d5-a78b-908cd882d3df",
            "transactionReceipt": {
                "_type": "TransactionReceipt",
                "blobGasPrice": null,
                "blobGasUsed": null,
                "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                "blockNumber": 8312770,
                "contractAddress": null,
                "cumulativeGasUsed": "41935874",
                "from": "0xD6AC871Ea68dD41774dA321B85e11D094b49aaa8",
                "gasPrice": "1000017",
                "gasUsed": "324143",
                "hash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                "index": 337,
                "logs": [
                    {
                        "_type": "log",
                        "address": "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x",
                        "index": 657,
                        "topics": [
                            "0x1cf3b03a6cf19fa2baba4df148e9dcabedea7f8a5c07840e207e5c089be95d3e",
                            "0x000000000000000000000000248c1e059619791d4743ebf84374edb311dc0306"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    },
                    {
                        "_type": "log",
                        "address": "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000",
                        "index": 658,
                        "topics": [
                            "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                            "0x0000000000000000000000000000000000000000000000000000000000000000",
                            "0x000000000000000000000000d6ac871ea68dd41774da321b85e11d094b49aaa8"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    },
                    {
                        "_type": "log",
                        "address": "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x",
                        "index": 659,
                        "topics": [
                            "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
                            "0x0000000000000000000000000000000000000000000000000000000000000000",
                            "0x000000000000000000000000d6ac871ea68dd41774da321b85e11d094b49aaa8",
                            "0x000000000000000000000000a1bfed6c6f1c3a516590eddac7a8e359c2189a61"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    },
                    {
                        "_type": "log",
                        "address": "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x",
                        "index": 660,
                        "topics": [
                            "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
                            "0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6",
                            "0x000000000000000000000000d6ac871ea68dd41774da321b85e11d094b49aaa8",
                            "0x000000000000000000000000a1bfed6c6f1c3a516590eddac7a8e359c2189a61"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    },
                    {
                        "_type": "log",
                        "address": "0xb4FC5Efab498Ce8b60D0Ad1fc780B871D1199C32",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x0000000000000000000000000000000000000000000000000000000000000001",
                        "index": 661,
                        "topics": [
                            "0xc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    },
                    {
                        "_type": "log",
                        "address": "0xA1BfEd6c6F1C3A516590edDAc7A8e359C2189A61",
                        "blockHash": "0x1f3c257e72f364ea993ca69da45f34e22b550b097655bb248a3ad3556a246a54",
                        "blockNumber": 8312770,
                        "data": "0x000000000000000000000000b4fc5efab498ce8b60d0ad1fc780b871d1199c32",
                        "index": 662,
                        "topics": [
                            "0x2e2b3f61b70d2d131b2a807371103cc98d51adcaa5e9a8f9c32658ad8426e74e"
                        ],
                        "transactionHash": "0xbef4c293fa9ed89080bbf80ff960a1625182d0077b1d0dfe1699733588494cca",
                        "transactionIndex": 337
                    }
                ],
                "logsBloom": "0x00020004000000000000000000000000000000000008000000000000000000000000000000000000000000000000004000000800000000000004100040000000000000000000000000000008001000000000000200000000000000000000000000000000020000000000008000000800000000000000000000000010001000000000000010000000000800000000080000000000000080000040000000000400000000000000000000000000000000400000000000000000001000000010000000000002000000000200000000000000001000000004000100800000480020000000000000000000002000000000000000000000000000001000000000000000",
                "status": 1,
                "to": "0xA1BfEd6c6F1C3A516590edDAc7A8e359C2189A61"
            },
            "userId": null
        },
        "timestamp": 1747074278,
        "apiVersion": 0,
        "signature": "AacvQXGjpCLG/zu8JHhMwbFdHRx/BsOEt+wpVI4cwEiOvN8rzVD+i1IIWYlNgeHRV914giGkoWKsNRVhLV6PAA=="
    }

Webhook Signatures
~~~~~~~~~~~~~~~~~~

1Shot API signs the webhook payload using the `ed25519 <https://en.wikipedia.org/wiki/EdDSA#Ed25519>`_ signature scheme. Each transaction
endpoint generates its own public-private keypair. As shown in the example above, the signature is included in the JSON payload under the 
key ``signature``. You should verify the signature using the public key provided in the transaction details page. The public key is a 
base64 encoded ed25519 public key that you can use to verify the signature.

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