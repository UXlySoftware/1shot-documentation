.. 1shot-documentation documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:54:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/test-image.png
   :alt: 1Shot Logo
   :align: center
   :width: 400px

Welcome to 1Shot!
=================================

The `1Shot API <https://1shotapi.com>`_ is the first fully managed transaction service for the Etherum mainnet and L2 ecosystem. It provides a simple REST interface
to trigger state-changing transactions on your target network with a single API call. This greatly simplifies adding digital assets or on-chain 
logic to any application, regardless of the blockchain network, or the language your application is developed in. 

1Shot provides helpful client sdks for popular languages like Python, Typescript, C#, and PHP, so you can one shot your next app in no time,
leaving the complexities of transaction submission and monitoring to us.

Getting Started
----------------------------------

You can start using 1Shot by making an account at `1shotapi.com <https://1shotapi.com>`_. You'll need to:

1. Select the target blochchain network where you wish to trigger transactions.
2. Generate an escrow wallet and fund with gas tokens for that network.
3. Configure a transaction endpoint by supplying a contract address and configuring the function on the contract the endpoint will call. You can also optionally set a webhook callback which will trigger when you transaction is confirmed.
4. Call your newly configured API endpoint from your application.

.. toctree::
   :hidden:
   :maxdepth: 2

   index
   escrow-wallets
   transactions
   teams
