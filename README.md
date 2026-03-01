# Aether Sync chronozisation

# Netrix – Aether Synchronisation System

## The Story
This project was done with my friend P.Sujith

## What This Project Is

Netrix is a lightweight peer-to-peer synchronisation system written in Python.

It simulates multiple peers communicating over UDP. The system includes mechanisms for:

- Peer discovery and management
- Heartbeat signals to detect active peers
- Gossip-style state propagation
- Retransmission logic for lost packets
- Configurable network behaviour such as packet loss rate and timeouts

The goal of this project is to demonstrate core distributed system concepts in a simplified and understandable way.

## How It Works

- Each peer runs independently.
- Communication happens using UDP sockets.
- A heartbeat mechanism checks whether peers are alive.
- Gossip messages spread updates across nodes.
- If a packet is not acknowledged within a timeout period, retransmission logic is triggered.
- Network behaviour can be adjusted using configuration parameters like loss rate, retransmission timeout, gossip interval, and heartbeat interval.

## Tech Stack

- Python
- UDP Sockets
- Modular Python architecture

## Features

- Peer-to-peer communication
- Failure detection using heartbeat
- Packet retransmission mechanism
- Configurable network simulation
- Modular and structured codebase

## What I Learned

Through this project, I learned:

- How unreliable transport protocols like UDP behave
- How retransmission systems are designed
- How heartbeat mechanisms detect failures
- How distributed systems maintain consistency
- How to structure a multi-file Python networking project

## Future Improvements

- Add a monitoring dashboard to visualize peer states
- Add logging and analytics tools
- Improve fault tolerance
- Implement more advanced consensus mechanisms
