..  youtube:: WLkwqC4B2r4
   :align: center

n8n
===

`n8n <https://n8n.io/>`_ is a workflow automation platform designed to empower users to create complex, agentic workflows with minimal technical knowledge. Its intuitive drag-and-drop interface and robust functionality have made it a favorite among developers, businesses, and tech enthusiasts alike. With an ever-expanding library of official and community-built nodes, n8n enables seamless integrations across countless tools and platforms.

n8n Nodes
---------

Worklows in n8n are built using nodes which allow n8n to make api calls to external services. The 1Shot API n8n node lets your read from and write to smart contracts on any EVM-compatible blockchain in your n8n workflows. You can find our node implementation on `github <https://github.com/uxlySoftware/n8n-nodes-1shot>`_. 

Installing the 1Shot API n8n Node
--------------------------------------

You can install the 1Shot API n8n node by searching for `n8n-nodes-1shot` in the community nodes package manager. Click install, then you should be able to find the 1Shot API node in your n8n workflow search bar.

The first time you import a 1Shot API node into your workflow, you will need to create a credential to authenticate against your 1Shot API account. Click on the node, then click "Create new credential" under "Credential to connect with" at the top of the view. You will enter an `API key and and secret <https://app.1shotapi.com/api-keys>`_ as well as your business ID (located at the top right corner of your 1Shot API dashboard) and then click "Save".

Node Types 
----------

The 1Shot API n8n node supports three node types:

- **1Shot API**: This is the primary node you'll likely use. It contains functions for reading and writing to smart contracts, as well as reading your transaction history and wallet states. 
- **1Shot API Webhook**: This is an entrypoint node; it can trigger workflows in n8n. This node requires you input a `webhook public key </basics/contract-methods.html#webhook-signatures>`_ so that callbacks can be authenticated. 
- **1Shot API Sumbit & Wait**: This is a specialized instance of the 1Shot API node that can execute contract methods and block the workflow until the transaction is either confirmed or fails. This node will fork into *success* and *error* branches, allowing you to handle the outcome of the transaction in your workflow.

Monetize n8n Workflows with x402
---------------------------------

..  youtube:: m3ThthLtj3g
   :align: center

Using the *1Shot API* node in series with the *1Shot API Submit & Wait* node, you can monetize any workflow that you can build in n8n using the x402 payment protocol. 

The workflow template is available `here <https://n8n.io/workflows/5389-monetize-workflows-with-x402-payment-protocol-and-1shot-api/>`_. Copy the JSON file and import it into your n8n workflow instance. 

x402 Workflow Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can import the x402 template into your n8n instance by copying the JSON from the published `x402 <https://n8n.io/workflows/5389-monetize-workflows-with-x402-payment-protocol-and-1shot-api/>`_ workflow and clicking `import` in the n8n workflow editor.

Once you have imported the workflow, be sure to configure a credential so that the 1Shot API nodes can communicate with your 1Shot API account.

Payment Configuration
~~~~~~~~~~~~~~~~~~~~~

.. important::

    Don't forget to provision a `1Shot API wallet </basics/wallets.html>`_ on the target blockchain network where you want to accept payments. Put sufficient gas funds into the wallet to cover the transaction costs of your payment transactions.

You will need to click on both the *Simulate Payment* and the *1Shot API Submit & Wait* nodes in the workflow and point them at the `transferWithAuthorization` method belonging to the token you want to accept as payment. The ERC-20 token you choose **must** expose a `**transferWithAuthorization** <https://eips.ethereum.org/EIPS/eip-3009>`_ method (as is the case for the USDC token) to be compatible with x402. Import the appropriate smart contract method in "My Smart Contracts" in the 1Shot API dashboard, and then select it in both of the 1Shot API nodes. 