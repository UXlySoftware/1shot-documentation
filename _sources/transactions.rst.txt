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
your `API key and secret <api.html>`_.

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

- ``to``: The address to transfer the tokens to
- ``value``: The amount of tokens to transfer (USDC has 18 decimal places)

We'll set both of these parameters to be ``Dynamic`` so because we will pass both of them as input parameters when we call the API endpoit. 

.. hint::

    You can also set parameters to be ``Static`` if you want to hardcode them in the transaction endpoint configuration. This is useful, for example, 
    if you always want to transfer the same amount of tokens every time but to different addresses.

Static vs Dynamic Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuring a transaction endpoint, input parameters can be either ``Static`` or ``Dynamic``. Parameters set to ``Static`` will be hardcoded in the
transaction endpoint configuration and cannot be changed when calling the API. Parameters set to ``Dynamic`` will be passed as input parameters when calling
the API and can be different for each transaction. See `Calling the 1Shot API <api.html>`_ for more information on how to trigger a transaction.

Webhooks
---------

Webhooks are an optional configuration for you transaction endpoint but are highly recommended as they provide immediate feedback to your application once your transaction
has been confirmed on the blochchain network. 

