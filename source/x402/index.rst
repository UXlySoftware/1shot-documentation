..  youtube:: YxydlAkSZmU
   :align: center

.. raw:: html

   <br />

x402 Facilitator
=================

1Shot API offers special API endpoints for facilitating `x402 <https://x402.org>`_ payments, check out the `OpenAPI specification </api/openapi.html#operations-tag-x402>`_ for the x402 tag. 

1Shot API can process x402 payments for any EIP-3009 compatible token on any of the supported EVM networks you have a provisioned `server wallet </basics/wallets.html>`_ on. Be sure to deposit sufficient gas funds into your server wallet to cover the transaction costs of the payment transactions (the `1Shot API gas station <https://1shotapi.com/gas-station>`_ is an easy way to convert USDC into gas on any chain you might have a server wallet on).

Configuring x402 Payment Tokens
--------------------------------

.. image:: /_static/x402/x402-token-import.gif
   :alt: Importing an x402 token
   :align: center

.. raw:: html

   <br />

Before you can import a payment token, you must first provision a `server wallet <https://app.1shotapi.com/walletst>`_ on your target network. Then you can import any `EIP-3009 <https://eips.ethereum.org/EIPS/eip-3009>`_ compatible token into your 1Shot API account to process payments. The token must expose a ``transferWithAuthorization`` method. This can be done by searching for your desired token in the `1Shot Prompts <https://app.1shotapi.com/1shot-prompts>`_ directory, filtering on the ``x402`` category. Click on the token you want, then in the "Write Functions" column, select ``transferWIthAuthorization`` and click "Add to My Contract Methods". Alternatively, simply click the "Create Contract Methods for All Functions" in the top right hand corner. 

.. important::

    The original EIP-3009 specification describes a ``transferWithAuthorization`` method that takes a user signature in the form of ``v``, ``r``, and ``s``. However, some tokens like USDC have an overloaded version that takes a single ``signature`` bytes string. 1Shot API expects the ``v``, ``r``, and ``s`` version of the method to be present in the token's contract ABI. The ``/verify`` and ``/settle`` endpoints take a ``signature`` as described in the x402 standard specification; 1Shot API will split the signature into its ``v``, ``r``, and ``s`` components before calling the ``transferWithAuthorization`` method automatically. This allows for support for tokens like PYUSD.

Using 1Shot API to Facilitate x402 Payments
-------------------------------------------

1Shot API provides a simple npm package for integrating x402 payments into your node server application that is compatible with the `Coinbase x402 <https://github.com/coinbase/x402>`_ npm package suite. 

You can install the facilitator package for node with your package manager of choice:

.. code-block:: bash

    npm install @1shotapi/x402-facilitator

.. note::

    The canonical `x402 package <https://www.npmjs.com/package/x402>`_ from Coinbase Developer Platform is a dependency of middleware packages like `x402-express <https://www.npmjs.com/package/x402-express>`_ and may not currently support the chain you want to use for payments. 1Shot API publishes a shim package, `@1shotapi/x402 <https://www.npmjs.com/package/@1shotapi/x402>`_, that can be used as an override to add support for additional chains. Install it in your project, ``pnpm add x402@npm:@1shotapi/x402``, then add the override to your ``package.json``:

    .. code-block:: json

        "pnpm": {
          "overrides": {
            "x402": "@1shotapi/x402@^0.1.1"
          }
        }


This package exports two components: 

* ``facilitator``: A ``FacilitatorConfig`` object used by x402 middleware packages; reads 1Shot API credentials from environment variables.
* ``createFacilitatorConfig``: A helper function which creates a ``FacilitatorConfig`` object and takes 1Shot API credentials as parameters.

Try running our `x402-express demo <https://github.com/1Shot-API/1Shot-API-Examples/tree/main/typescript/x402-server>`_ or check out the code example below:

.. code-block:: javascript

   import { config } from "dotenv";
   import express from "express";
   import { paymentMiddleware } from "x402-express";
   import { facilitator, createFacilitatorConfig } from "@1shotapi/x402-facilitator";
   config();

   const facilitatorConfig = createFacilitatorConfig(
     process.env.ONESHOT_API_KEY!,
     process.env.ONESHOT_API_SECRET!,
   );

   // Or use environment variables implicitly
   // const facilitatorConfig = facilitator;

   app.use(
     paymentMiddleware(
      payTo,
       {
         "GET /weather": {
           // USDC amount in dollars
           price: "$0.001",
           // network: "base" // uncomment for Base mainnet
           network: "base-sepolia",
           config: {
             description: "Access to weather data",
             mimeType: "application/json",
          },
         },
           config: {
             description: "Access to premium content",
             mimeType: "application/json",
           },
           // network: "base" // uncomment for Base mainnet
           network: "base-sepolia",
         },
       },
       facilitatorConfig,
     ),
   );