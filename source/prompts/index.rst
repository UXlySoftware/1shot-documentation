1Shot Prompts
=============

..  youtube:: ViNfYVmGM8w
   :align: center

.. raw:: html

   <br />

There are millions of smart contracts across various EVM networks, some of them are better documented than others. 1Shot Prompts is a community driven effort to document smart contracts, their functions, and the function inputs and outputs in a way that makes them consumable by AI agents.

Smart contracts must have verified ABI and source code available on Etherscan in order to be published as a prompt. A prompt is a collection of human readable text that describes how the smart contract is to be used in a specific context plus descriptions of the contract functions that would be used in that context along with descriptions of the function inputs and outputs. A single smart contract can have multiple prompts, each describing a different use case or context for the contract.

Smart Contracts as Tools 
------------------------

Smart contract prompts can be turned into tools by importing them into your `business </basics/businesses-and-teams.thml>`_. You can then list all the tools available in your business by `listing the contract methods </api/api.html#list-available-contract-methods>`_ in your business. The description fields of the contract methods and their inputs and outputs can be passed to an LLM to help it reason about how to use the contract method and what to expect from the transaction execution.
