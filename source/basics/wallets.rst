Wallets
=======

.. image:: /_static/escrow-wallet/escrow-flow-light.png
   :alt: Escrow Flow
   :align: center
   :class: only-light

.. image:: /_static/escrow-wallet/escrow-flow-dark.png
   :alt: Escrow Flow
   :align: center
   :class: only-dark

.. raw:: html

   <br />

1Shot API wallets are Ethereum-compatible signing keys managed by 1Shot API to submit transactions on your behalf when you make a REST 
call to one of your configured `contract methods <transactions.html>`_. Each of your wallets can be linked to one or 
more smart contract methods (but each contract method can only have a single default). The default wallet of a contract method can be overridden when the endpoint
is called from the api. In order to submit a transaction from any of your 1Shot API-managed wallets, you must first deposit gas tokens.

1Shot API's wallet infrastructure keeps your keys secure and encrypted at rest, but it is still good practice to only deposit 
the amount of gas tokens you need for a given period of time. When your wallet runs low on funds, 1Shot API will automatically send 
you an email notification. You can `deposit additional gas funds <#funding-your-escrow-wallet>`_ into your wallet 
at anytime which will trigger a confirmation email when the service detects the deposit.

Creating an Wallet
------------------

.. image:: /_static/escrow-wallet/create-escrow-wallet.gif
   :alt: Creating a wallet
   :align: center

.. raw:: html

   <br />
   
To create a wallet, navigate to the `Wallets <https://app.1shotapi.com/escrow-wallets>`_ page in the 1Shot API dashboard 
and click the "Create Wallet" button. You will be prompted to enter a name and description for your new wallet and the target blockchain 
the wallet will operate on.

.. _funding-your-wallet:

Funding Your Wallet
-------------------

You must deposit native tokens into your wallet to pay for transactions signed by its key. Only fund your wallet with 
assets on the target blockchain the wallet is configured for. 

For example, if you are setting up a wallet for the Ethereum mainnet, you should only deposit ETH to pay for gas into the 
wallet. If you are configuring a wallet for the Polygon network, you should only deposit Polygon gas tokens into the wallet.

.. hint:: 
   
   You can deposit ERC-20 tokens, ERC-721 NFTs or other similar assets into a wallet to make it easier to perform airdrops or DeFi trades. Another strategy would be to leave
   the tokens in a cold (or soft wallet) that you personally control and `approve <https://eips.ethereum.org/EIPS/eip-20#approve>`_ the 1Shot escrow wallet to spend them when needed.

Withdrawing funds
-----------------

.. image:: /_static/escrow-wallet/withdraw.png
   :alt: Initiate funds withdrawal
   :align: center

.. raw:: html

   <br />

You can withdraw funds from your wallet at any time by clicking the "Withdraw" button on the wallet's detail page. Enter the amount of gas (native)
tokens you want to withdraw and click "Send". You'll be prompted to confirm the withdrawal details before the transaction is submitted.

.. image:: /_static/escrow-wallet/withdraw-confirmation.png
   :alt: Confirming funds withdrawal
   :align: center