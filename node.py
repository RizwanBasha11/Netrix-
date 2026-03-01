def receive_loop():
    while True:
        data, addr = udp.receive()
        msg = decode_message(data)

        if msg["type"] == "ACK":
            reliable.ack_received(msg["seq"])

        elif msg["type"] == "DELTA":
            print("DELTA received")
            state_engine.merge(msg["payload"])

        elif msg["type"] == "REQUEST":
            full_state = state_engine.get_state()

            packet = {
                "type": "DELTA",
                "payload": full_state
            }

            raw = encode_message(packet)
            packet["raw"] = raw
            reliable.send(packet, addr)

        elif msg["type"] == "SUMMARY":

            remote_summary = msg["payload"]
            local_summary = state_engine.get_summary()

            delta_to_send = {}
            we_are_behind = False

            for key, local_vector in local_summary.items():

                if key not in remote_summary:
                    delta_to_send[key] = state_engine.get_state()[key]

                else:
                    comparison = state_engine.compare_vectors(
                        local_vector,
                        remote_summary[key]
                    )

                    if comparison == "local_dominates":
                        delta_to_send[key] = state_engine.get_state()[key]

                    elif comparison == "remote_dominates":
                        we_are_behind = True

            if delta_to_send:
                packet = {
                    "type": "DELTA",
                    "payload": delta_to_send
                }

                raw = encode_message(packet)
                packet["raw"] = raw
                reliable.send(packet, addr)

            elif we_are_behind:
                request_packet = {
                    "type": "REQUEST"
                }

                raw = encode_message(request_packet)
                request_packet["raw"] = raw
                reliable.send(request_packet, addr)