.. 1shot-documentation documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:54:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. .. image:: ./_static/light-banner.png
..    :alt: 1Shot API
..    :align: center
..    :class: only-light

.. .. image:: ./_static/dark-banner.png
..    :alt: 1Shot API
..    :align: center
..    :class: only-dark

.. image:: ./_static/smart-tools-for-smart-contracts.jpg
   :alt: 1Shot API
   :align: center

.. raw:: html

   <br />

Welcome to 1Shot!
==================

The `1Shot API <https://1shotapi.com>`_ is the first fully managed, enterprise-grade hot wallet and transaction service for the Ethereum mainnet and L2 ecosystem 
(Binance and Avalanche supported as well). It provides a simple REST API to trigger state-changing smart contract transactions on a target blockchain network with 
a single POST call. 

1Shot is not an RPC provider, but an abstraction layer on top of typical RPC providers (like Infura or Alchemy). In fact, depending on your use case you may not even 
need an RPC provider as we handle the full transaction lifecycle with real-time webhook callbacks on the final state of your transactions. 1Shot API allows you to read from 
and write to smart contracts without the need of importing web3 clients like viem or ethers.js into your source code. This lets you focus on the logic specific to your application
while 1Shot API handles the complexities of data types, contract ABIs, signers and private key security, and nonce cohesion for you.

The 1Shot API service is designed to handle heavy user traffic. If your product has many users generating on-chain mechanics all at once, 1Shot API ensures all of your 
transactions will make it to the chain quickly and gas efficiently. 1Shot greatly simplifies the technical overhead of adding digital assets or on-chain logic to 
any application, bot, or agent, regardless of the language your application is written in.

Several helpful client sdks for popular languages like [Python](https://pypi.org/project/uxly-1shot-client/), [Typescript](https://www.npmjs.com/package/@uxly/1shot-client) 
are available so you can one shot your next app in no time, leaving the complexities of transaction submission and monitoring to us.

1Shot Prompts
-------------

The 1Shot API lets AI agent developers consume smart contracts and their functions as fully annotated tools that can be consumed by any agent programming framework. You can 
find and publish smart contract tool prompts to `1Shot Prompts <https://app.1shotapi.com/1shotprompts>`_. This provides detailed prompts for the contract, function,
input and output parameter level which allow LLMs to better reason about how to plan transaction execution chains and what to expect from the behavior of a transaction
before planning or execution.

Getting Started
----------------------------------

You can start using 1Shot by making an account at `app.1shotapi.com <https://app.1shotapi.com>`_. Here are the main features you can use to get started:

.. grid:: 2 2 2 2
    :gutter: 4

    .. grid-item-card:: 1. Organization Management 🏢
        :link: org-creation.html
        :link-alt: Organization Management 

        Create an organization, add team members, and manage billing.

    .. grid-item-card:: 2. Escrow Wallets 👛
        :link: escrow-wallets.html
        :link-alt: Escrow Wallets

        Provision and fund escrow wallets for submitting transactions.
   
    .. grid-item-card:: 3. Transaction Configuration 📝
        :link: transactions.html
        :link-alt: Transaction Configuration

        Build transaction endpoints to call smart contracts and configure webhooks.

    .. grid-item-card:: 4. Calling the 1Shot API 💻🐀
        :link: api/api.html
        :link-alt: Calling the 1Shot API

        Use your API key and secret to trigger transactions from your application.

.. toctree::
   :hidden:
   :maxdepth: 2

   org-creation
   escrow-wallets
   transactions
   api/index.rst
