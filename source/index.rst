.. 1shot-documentation documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:54:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. image:: ./_static/light-banner.png
   :alt: 1Shot
   :align: center
   :class: only-light

.. image:: ./_static/dark-banner.png
   :alt: 1Shot
   :align: center
   :class: only-dark

Welcome to 1Shot!
=================================

The `1Shot API <https://1shotapi.com>`_ is the first fully managed transaction service for the Ethereum mainnet and L2 ecosystem. It provides a simple REST API
to trigger state-changing transactions on a target blockchain network with a single POST call. 

1Shot is designed to handle heavy user traffic. If your product has many users triggering on-chain mechanics all at once, 1Shot ensures all of your transactions will 
make it to the chain. 1Shot greatly simplifies the technical overhead of adding digital assets or on-chain logic to any application, and unlocks new possibilities 
for streamlined end-user experience, regardless of the language you application is written in.

Several helpful client sdks for popular languages like Python, Typescript, C#, and PHP are available so you can one shot your next app in no time,
leaving the complexities of transaction submission and monitoring to us.

Getting Started
----------------------------------

You can start using 1Shot by making an account at `app.1shotapi.com <https://app.1shotapi.com>`_. You'll need to:

1. Create an organization and add team members.
2. Select the target blockchain network where you wish to trigger transactions, generate an escrow wallet and fund with gas tokens for that network.
3. Configure a transaction endpoint by supplying a contract address and configuring the function on the contract the endpoint will call. You can also optionally set a webhook callback which will trigger when a transaction from this endpoint is confirmed.
4. Call your newly configured API endpoint from your application.

.. toctree::
   :hidden:
   :maxdepth: 2

   org-creation
   escrow-wallets
   transactions
