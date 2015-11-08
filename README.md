# PacketVR Example Apps 

# Note about PacketVR SSH limitations:

Because Unity 5 is STILL using an old version of the C# (effectively using version 2.0 and sometimes 3.5 via Mono), we are limited in regards to available C# based SSH libraries are out there. Unity have said they're working on updating this but for now, it forces us to use one of the only free libraries I've found: SharpSSH

Now, because SharpSSH hasn't been updated in a while, it's not a fully functional SSH library. The immediate impact of this is that we can only connect so SSH servers configured in a specific way.

That means that the library only supports specific Ciphers, Key Exchange Algorithm(KexAlgorithms), and MAC algorithms. These are the supported types:

```
Ciphers: aes128-cbc,3des-cbc
KexAlgorithms: diffie-hellman-group1-sha1,diffie-hellman-group-exchange-sha1
MACs: hmac-md5,hmac-sha1
```

Here are the BARE MINIMUM options we'll need to configure in sshd_conf to get the library to work. Just put these at the end of the /etc/ssh/sshd_conf and restart the ssh service.

NOTE! These following settings are NOT comprehensive! They configure the server to ONLY allow these settings! It would be better to understand exactly what you need to support instead of just applying these wholesale config changes!

WARNING! These settings are not entirely secure! These have various security risks associated with them that are far to complex to explain here! Don't hold me responsible if you set these settings on an SSH server somewhere, forget about them, then get compromised! 

```
Ciphers=aes128-cbc,3des-cbc
KexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group-exchange-sha1
MACs=hmac-md5,hmac-sha1
```

And here's an sshd debug command line to test the settings (as long as you don't already have SSH running on port 22):

```
/usr/bin/sshd -Dd -oCiphers=aes128-cbc,3des-cbc -oKexAlgorithms=diffie-hellman-group1-sha1,diffie-hellman-group-exchange-sha1 -oMACs=hmac-md5,hmac-sha1
```