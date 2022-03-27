# Log4Shell Callback Server
This is a simple Python callback server to proof if a client is vulnerable of Log4Shell.  
## Usage
1. Start the server (default port is 5000)
    ```
    python callback.py
    ```
1. Inject your crafted JNDI string into the target server
1. Observe connections (will also be written to `catcher.log`)
