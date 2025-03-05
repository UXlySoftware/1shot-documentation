Escrow Wallets
======================

.. image:: ./_static/escrow-wallet/escrow-flow-light.png
   :alt: Escrow Flow
   :align: center
   :class: only-light

.. image:: ./_static/escrow-wallet/escrow-flow-dark.png
   :alt: Escrow Flow
   :align: center
   :class: only-dark

Escrow wallets are Ethereum-compatible signing keys managed by 1Shot to submit transactions on your behalf when you make a REST 
call to one of your configured `transaction endpoints <transactions.html>`_. Each of your escrow wallets can be linked to one or 
more transaction endpoints (but each endpoint can only have a single escrow wallet). In order to submit a transaction from any 
of your 1Shot-managed escrow wallets, you must first deposit gas tokens.

1Shot keeps your keys secure and encrypted at rest, but it is still good practice to only deposit the amount of gas tokens you 
need for a given period of time. You can `deposit additional gas funds <#funding-your-escrow-wallet>`_ into your escrow wallet 
at anytime which will trigger a confirmation email when 1Shot detects the deposit.

Creating an Escrow Wallet
--------------------------

.. image:: ./_static/escrow-wallet/escrow-wallets-getting-started.png
   :alt: Creating your first escrow wallet
   :align: center

To create an escrow wallet, navigate to the `Escrow Wallets <https://app.1shotapi.com/escrow-wallets>`_ page in the 1Shot dashboard 
and click the "Create Wallet" button. You will be prompted to enter a name and description for your new wallet and the target blockchain 
the wallet will operate on.

.. _funding-your-escrow-wallet:

Funding Your Escrow Wallet
---------------------------

Only fund your escrow wallet with assets on the target blockchain the wallet is configured for. For example, if you are configuring a 
transaction endpoint for the Ethereum mainnet, you should only deposit Ethereum gas tokens into the wallet. If you are configuring 
a transaction endpoint for the Polygon network, you should only deposit Polygon gas tokens into the wallet.

Withdrawing funds
-----------------