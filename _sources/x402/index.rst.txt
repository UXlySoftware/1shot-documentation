..  youtube:: YxydlAkSZmU
   :align: center

.. raw:: html

   <br />

x402 Facilitator
=================

1Shot API offers special API endpoints for facilitating `x402 <https://x402.org>`_ payments, check out the `OpenAPI specification </api/openapi.html#operations-tag-x402>`_ for the x402 tag. 

1Shot API can process x402 payments for any EIP-3009 compatible token on any of the supported EVM networks you have a provisioned server wallet on. Be sure to deposit sufficient gas funds into your server wallet to cover the transaction costs of the payment transactions.

Configuring x402 Payment Tokens
--------------------------------

You can import any `EIP-3009 <https://eips.ethereum.org/EIPS/eip-3009>`_ compatible token into your 1Shot API account to process payments. The token must expose a ``transferWithAuthorization`` method. This can be done by searching for your desired token in the `1Shot Prompts <https://app.1shotapi.com/1shot-prompts>`_ directory and clicking `import` on the ``transferWithAuthorization`` method or by manually adding the smart contract with its ``transferWithAuthorization`` method from the `My Smart Contracts <https://app.1shotapi.com/smart-contracts>`_ page in the 1Shot API dashboard.

.. important::

    The original EIP-3009 specification describes a ``transferWithAuthorization`` method that takes a user signature in the form of ``v``, ``r``, and ``s``. However, some tokens like USDC have an overloaded version that takes a single `signature` bytes string. 1Shot API expects the ``v``, ``r``, and ``s`` version of the method to be present in the contract ABI to be compatible with x402. But the ``/verify`` and ``/settle`` endpoints take a ``signature`` as described in the x402 standard; 1Shot API will split the signature into its ``v``, ``r``, and ``s`` components before calling the ``transferWithAuthorization`` method automatically. 

Using 1Shot API to Facilitate x402 Payments
-------------------------------------------

1Shot API provides a simple npm package for integrating x402 payments into your node server application that is compatible with the `Coinbase x402 <https://github.com/coinbase/x402>`_ npm package suite. 

You can install the facilitator package for node with your package manager of choice:

.. code-block:: bash

    npm install @1shotapi/x402-facilitator

This package exports two components: 

* ``facilitator``: A ``FacilitatorConfig`` object used by x402 middleware packages; reads 1Shot API credentials from environment variables.
* ``createFacilitatorConfig``: A helper function which creates a ``FacilitatorConfig`` object and takes 1Shot API credentials as parameters.

Here is an example:

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