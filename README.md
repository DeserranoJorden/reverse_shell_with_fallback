This repo can create a Master-slave connection remotely
	it sends a heartbeat every minute with some info and tries to make a reverse shell connection (first HTTP, then TCP)
	
it also consist of some experimental reverse shells on ICMP
	
	
	Master:
		1)  host the php file on a remote server.
		2) (4444)Start the listener you want
			i. HTTP listener support multiple slaves (sudo python /FindThePwnie/TCP-shell/TCPshellServer.py)
			ii. TCP is the only fallback right now (sudo python3 /FindThePwnie/HTTP-shell/HTTPshellServer.py)
	
	Slave:
		1) Start the fallbackmechanism with:
		Python FallBackMechanism.py Heartbeat/HBhttpclient.py HTTP-shell/HTTPshellClient.py TCP-shell/TCPshellClient.py
		
		This will retest connection and send a heartbeat every 60 seconds
		
		
	Remarks:
		1) Might want to implement more fallbacks (UDP/DNS/ICMP) later, but these are unreliable
		2) Heartbeat only works on http right now
	
		
