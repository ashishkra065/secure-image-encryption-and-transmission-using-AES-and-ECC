**Project Overview**
**The project involves:**

**Image Encryption:**
Use AES-256 for symmetric encryption of the image.
Use Elliptic Curve Cryptography (ECC) for secure key exchange.
**Image Transmission:**
Implement a UDP-based communication channel for real-time image sharing.
Use WebSockets for efficient and low-latency transmission.
**Image Processing:**
Use OpenCV and PIL for image preprocessing and post-processing.
**Security Enhancements:**
Use HMAC for data integrity.
Use hashlib for hashing sensitive data

**Step 1: Install Required Libraries**
Install the necessary Python libraries:

**Step 2: Implement Crypto Utilities**
Created crypto_utils.py in the utils/ folder. This file handles AES, ECC, HMAC, and hashing.

**Step 3: Implement Image Utilities**
Create image_utils.py in the utils/ folder. This file handles image loading, saving, and conversion.

**Step 4: Implement the Server**
Create server.py in the server/ folder. This file handles receiving and decrypting images.

**Step 5: Implement the Client**
Create client.py in the client/ folder. This file handles sending encrypted images.

**ECC Key Exchange:**
Use ECC to securely exchange the AES key between the client and server.
**HMAC for Integrity:**
Add HMAC to ensure the encrypted data has not been tampered with.
**Real-Time Image Preview:**
Use OpenCV to display the received image in real-time on the server side

Start the server: python server/server.py
Send an image from the client:python client/client.py
