IFTTT
=====

..  youtube:: 2rZ81sR4eEg
   :align: center

`If This Then That <https://ifttt.com/>`_ (IFTTT) is a web-based service that allows users to create chains of simple conditional statements, called applets. These applets can connect various web services and devices, enabling automation of tasks across different platforms. For example, with 1Shot API's IFTTT service, you can create an applet that automatically sends ERC-20 tokens to users whenever they follow your company's social media account. 

Triggers, Actions, and Queries
-------------------------------

1Shot API has three components with which you can build IFTTT applets: Triggers, Queries, and Actions.

- **Triggers**: These are events that can initiate an applet. 1Shot API currently provides two triggers: *On Successful Transaction* and *On Failed Transaction*. These triggers function as a virtual webhook callback; they allow you to trigger new IFTTT workflows based on the outcome of a transaction submitted from 1Shot API in a different context or workflow. 
- **Actions**: These are tasks that are performed in response to a trigger. 1Shot API lets you execute any contract method you have imported into your business. 
- **Queries**: These allow you to retrieve additional data from triggers and feed this into the subsequent action. 1Shot API lets you call any smart contract read method as a query and pass this information on as an *ingredient*.

.. note::

    You can mix and match the 1Shot API triggers, actions, and queries with any other IFTTT service. For example, you can trigger on a user sending a message to a Discord channel, then execute a token transfer to send ERC-20 tokens to their wallet address, and finally query the balance of that wallet to send a confirmation message back to the Discord channel.