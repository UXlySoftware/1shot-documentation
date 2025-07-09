..  youtube:: 2rZ81sR4eEg
   :align: center
   
.. raw:: html

   <br />
   
IFTTT
=====

`If This Then That <https://ifttt.com/>`_ (IFTTT) is a web-based service that allows users to create chains of simple conditional statements, called applets. These applets can connect various web services and devices, enabling automation of tasks across different platforms. For example, with 1Shot API's IFTTT service, you can create an applet that automatically sends ERC-20 tokens to users whenever they follow your company's social media account. 

Triggers, Actions, and Queries
-------------------------------

1Shot API has three components with which you can build IFTTT applets: Triggers, Queries, and Actions.

- **Triggers**: These are events that can initiate an applet. 1Shot API currently provides two triggers: *On Successful Transaction* and *On Failed Transaction*. These triggers function as a virtual webhook callback; they allow you to trigger new IFTTT workflows based on the outcome of a transaction submitted from 1Shot API in a different context or workflow. 
- **Actions**: These are tasks that are performed in response to a trigger. 1Shot API lets you execute any contract method you have imported into your business. 
- **Queries**: These allow you to retrieve additional data from triggers and feed this into the subsequent action. 1Shot API lets you call any smart contract read method as a query and pass this information on as an *ingredient*.

.. note::

    You can mix and match the 1Shot API triggers, actions, and queries with any other IFTTT service. For example, you can trigger on a user sending a message to a Discord channel, then execute a token transfer to send ERC-20 tokens to their wallet address, and finally query the balance of that wallet to send a confirmation message back to the Discord channel.

Building 1Shot API Applets
---------------------------

..  youtube:: 6vTXujMI3k4
   :align: center

Check out our applet tutorial that shows step-by-step how to create a token faucet in a Telegram group from scratch. The tutorial covers how to authenticate Telegram, set up the group, and add a 1Shot API query and action with filter code. Besides acting as a faucet, this applet could also be used to distribute creator tokens with `Star Messages <https://telegram.org/blog/star-messages-gateway-2-0-and-more>`_. 

Ready-to-Use Applets
----------------------

Check out our pre-published IFTTT applets and the their associated getting started guides:

Telegram ERC-20 Token Faucet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`This applet <https://ift.tt/2B98sNi>`_ allows you to create a token faucet within a Telegram group. Users can request tokens by sending a specific message like `/ifttt #mywallet 0x55680c6b69d598c0b42f93cd53dff3d20e069b5b` and the applet will automatically send the configured amount of tokens to the specified wallet address. The applet also implements a *cool-down* period to prevent abuse, ensuring that users can only request tokens once in the configured time period. 