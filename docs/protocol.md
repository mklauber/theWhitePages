Protocol involves three components.  Theoretically, one is optional.



Bob wants Alice's contact info.

1. Bob shares his public key with Alice.
2. Alice looks Bob's server in the DHT.
3. Alice encrypts her contact info with Bob's public key.
4. Alice sends her public key and the encrypted information to Bob's Server
5. Bob's server sends her information to Bob at next available opportunity.
6. Bob decrypts Alice's information with his private key.
7. Alice stores Bob's public key for future updates.


Alice updates her contact info.

1. Alice changes her contact info.
2. for each contact Alice has shared her contact info with, she sends her 
   contact info per The standard sharing protocol.


Actors:
DHT - Used to route requests for users to Servers
Server - Servers are always-available nodes to accept messages and pass them to Users  
User - Users are devices which contain encryption keys and manage address books.


DHT Protocol:
    associate(pubkey, sign(privkey, server))
        Sent by User(pubkey) to DHT(pubkey)-nearest neighbors.  
    
    query(pubkey):
        returns a server
        
        User explores the DHT, navigating towards DHT(pubkey) until a node 
        responds that it knows the server of pubkey.  It returns the 
        sign(privkey, server), which is used to validate that the server has not
        been changed.

Server:
    inform

Where is data maintained?:
    Phone: Unencrypted Contact Info, public/private keys
    Server: Encrypted Contact Info
    DHT:    List of IDs-> Servers