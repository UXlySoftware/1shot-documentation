IFTTT
=====

`If This Then That <https://ifttt.com/>`_ (IFTTT) is a web-based service that allows users to create chains of simple conditional statements, called applets. These applets can connect various web services and devices, enabling automation of tasks across different platforms. For example, with 1Shot API's IFTTT service, you can create an applet that automatically sends ERC-20 tokens to users whenever they follow your company's social media account. 

Triggers, Actions, and Queries
-------------------------------

1Shot API has three types of IFTTT services: Triggers, Queries, and Actions.

- **Triggers**: These are events that can initiate an action. 1Shot API currently provides two triggers: *On Successful Transaction* and *On Failed Transaction*. These triggers function as a virtual webhook callback; they allow you to trigger new IFTTT workflows based on the outcome of a transaction submitted from 1Shot API in a different context or workflow. 
- **Actions**: These are tasks that are performed in response to a trigger. 1Shot API lets you execute any contract method you have imported into your business. 
- **Queries**: These allow you to retrieve additional data from triggers and feed this into the subsequent action. 1Shot API lets you call any smart contract read method as a query and pass this information on as an *ingredient*.