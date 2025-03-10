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

Webhooks are an optional configuration for you transaction endpoint but are highly recommended as they provide immediate feedback to your application once your transaction
has been confirmed on the blochchain network. 1Shot implements best practices for webhooks are discussed at `webhooks.fyi <https://webhooks.fyi/>`_, which includes
consumer verification, replay protection and forward compatibility. , 

When you configure a webhook, 1Shot will send a POST request to the URL you provide with a JSON payload containing the following fields:

- ``transactionHash``: The hash of the transaction that was submitted to the blockchain
- ``status``: The status of the transaction (``pending``, ``success``, or ``failure``)
- ``blockNumber``: The block number the transaction was included in

One time verification challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you configure a webhook, 1Shot will send a one-time verification challenge to the URL you provide. This challenge is a POST request with a JSON payload containing a 
random string. Your application should respond with a 200 status code and replay the same random string in the response body. This verifies that the webhook URL is under your 
control and can receive POST requests from 1Shot.

Webhook Signatures
~~~~~~~~~~~~~~~~~~

1Shot signs the webhook payload using `ed25519 <https://en.wikipedia.org/wiki/EdDSA#Ed25519>`_ signature scheme. The signature is included in the ``X-1Shot-Signature`` header of the POST request. You can verify the signature using the
public key provided in the webhook configuration. The public key is a base64 encoded ed25519 public key that you can use to verify the signature.