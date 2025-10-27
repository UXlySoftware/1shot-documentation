..  youtube:: WLkwqC4B2r4
   :align: center

.. raw:: html

   <br />
   
n8n
===

`n8n <https://n8n.io/>`_ is a workflow automation platform designed to empower users to create complex, agentic workflows with minimal technical knowledge. Its intuitive drag-and-drop interface and robust functionality have made it a favorite among developers, businesses, and tech enthusiasts alike. With an ever-expanding library of official and community-built nodes, n8n enables seamless integrations across countless tools and platforms.

n8n Nodes
---------

Worklows in n8n are built using nodes which allow n8n to make api calls to external services. The 1Shot API n8n node lets your read from and write to smart contracts on any EVM-compatible blockchain in your n8n workflows. You can find the source code for our node implementation on `github <https://github.com/uxlySoftware/n8n-nodes-1shot>`_. 

The 1Shot API community node is currently `verified <https://n8n.io/integrations/1shot-api/>`_ and can be used in n8n Cloud workflows. 

Installing the 1Shot API n8n Node
--------------------------------------

You can install the 1Shot API n8n node by searching for `n8n-nodes-1shot` in the community nodes package manager. Click install, then you should be able to find the 1Shot API node in your n8n workflow search bar.

The first time you import a 1Shot API node into your workflow, you will need to create a credential to authenticate against your 1Shot API account. Click on the node, then click "Create new credential" under "Credential to connect with" at the top of the view. You will enter an `API key and and secret <https://app.1shotapi.com/api-keys>`_ as well as your business ID (located at the top right corner of your 1Shot API dashboard) and then click "Save".

Node Types 
----------

The 1Shot API n8n node supports three node types:

- **1Shot API**: This is the primary node you'll likely use. It contains functions for reading and writing to smart contracts, as well as reading your transaction history and wallet states. 
- **1Shot API Webhook**: This is an entrypoint node; it can trigger workflows in n8n. There are two options: an x402 gateway which lets you monetize n8n workflows, and a 1Shot API webhook receiver which handles webhooks coming from 1Shot API & requires you input a `webhook public key </basics/contract-methods.html#webhook-signatures>`_ so that callbacks can be authenticated. 
- **1Shot API Sumbit & Wait**: This is a specialized instance of the 1Shot API node that can execute contract methods and block the workflow until the transaction is either confirmed or fails. This node will fork into *success* and *error* branches, allowing you to handle the outcome of the transaction in your workflow.

1Shot API Workflow Templates
----------------------------

You can find a library of pre-created, verified templates from 1Shot API on our `n8n verified creators page <https://n8n.io/creators/oneshotapi/>`_. 

Monetize n8n Workflows with x402
---------------------------------

..  youtube:: SzuSpIWLy5k
   :align: center

Using the *1Shot API* x402 webhook trigger, you can monetize any workflow that you can build in n8n using the x402 payment protocol. It automatically handles returning proper x402 error response to the client as well as calling the `1Shot API facilitator API </x402/index.html>`_. See the tutorial video above for a walkthrough setup procedure.

Payment Configuration
~~~~~~~~~~~~~~~~~~~~~

.. important::

    Don't forget to provision a `1Shot API wallet </basics/wallets.html>`_ on the target blockchain network where you want to accept payments. Put sufficient gas funds into the wallet to cover the transaction costs of your payment transactions.

You will need to import the ERC-20 tokens you want to accept as payments into your 1Shot API account. The selected tokens **must** expose a `transferWithAuthorization <https://eips.ethereum.org/EIPS/eip-3009>`_ method (as is the case for the USDC, PYUSD or mUSD tokens) that take `r`, `s`, and `v` signature components to be compatible with x402. You can find x402-compatible tokens by filtering on the `x402` tag in the `1Shot Prompts <https://app.1shotapi.com/1shot-prompts>`_ directory. Once imported, the token will appear as an option when you configure the x402 webhook node in your n8n workflow.

Popular Stablecoins that Support x402
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find x402-compatible tokens to facilitate payments for by filtering on the `x402` tag category in the `1Shot Prompts <https://app.1shotapi.com/1shot-prompts>`_ directory. Find the `transferWithAuthorization` method on the smart contract that takes `r`, `s`, and `v` parameters and click "Add to My Contract Methods" to import the method into your account. Once you've imported the method for your target token, go to the method's details page and copy the `Contract Method ID` to use in your n8n workflow configuration.