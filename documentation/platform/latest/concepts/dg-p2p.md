---
title: Peer-to-Peer Networking
---

Peer-to-Peer (P2P) networking allows your app to establish a connection and send data directly between users.

There are a number of uses for P2P networking. Some common implementations include, using P2P to exchange chat messages between users, updating gameplay data in lower latency, or update avatar positions in real-time. Our P2P service connects users to exchange data directly.

The Oculus Platform P2P allows you to choose between two send policies to transmit data depending on your use-case and the needs of your app.

* Reliable connections transmit data that will be delivered once and in the order that messages are sent. The networking layer retries until each message is acknowledged by the peer. Outgoing messages are buffered until a working connection to the peer is established. Reliable messages are useful when using P2P to send text chat messages that need to be delivered once and in the order that the user sent them, but not necessarily instantaneously. 
* Unreliable connections transmit data as best-effort, but cannot guarantee delivery in a specific order or time-frame. Any messages sent before a connected state is established will be dropped. Unreliable messages are useful when you're using P2P to update game data in realtime and transmitting data quickly is more important than guaranteeing delivery once and in order. Note that messages sent over unreliable connections should be limited to 1200 bytes.


## Integrate Peer-to-Peer Networking - Native &amp; Unity

The following methods are available to call from your client app. Detail about each function can be found on the Platform SDK OVR_Functions_Networking.h [reference content](/reference/platform/1.28/o_v_r_functions_networking_8h/).

* **Establish a connection:**

Native - ovr\_Net\_Connect()

Unity - Platform.Net.Connect()

This sends a ovrMessage\_NetworkingPeerConnectRequest to the specified user. It returns a ovrMessage\_NetworkingPeerConnectionStateChange notification when the connection is established, youâ€™ll need to be listening for this notification.


* **Accept and open a connection:**

Native - ovr\_Net\_Accept()

Unity - Platform.Net.Accept()

This should be called after receiving a ovrMessage\_NetworkingPeerConnectRequest message.


* **Accept and open a connection for a room:**

Native - ovr\_Net\_AcceptForCurrentRoom()

Unity - Platform.Net.AcceptForCurrentRoom()

Accept connection attempts from members of the current room. Please see the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") page for information about creating and joining rooms. Returns false if the user currently isn't in a room.


* **Check a connection with a user:**

Native - ovr\_Net\_IsConnected()

Unity - Platform.Net.IsConnected()

Checks if the current users is connected to another specific user, returns a true or false.


* **Ping a user:**

Native - ovr\_Net\_Ping()

Unity - Platform.Net.Ping()

Ping a user to determine network connection quality.


* **Send data to a user:**

Native - ovr\_Net\_SendPacket()

Unity - Platform.Net.SendPacket()

Send a sequence of bytes to a specified user. You also specify the length of the packet, the packet contents in bytes and the policy to apply to the packet; whether the connection is reliable, unreliable or unknown. The specified length must be less than or equal to the allocated length of the bytes. For a reliable connection, the max number of bytes allowed in the packet is 65535 bytes, which includes any descriptive information (headers) as well as the user data. If the connection is unreliable or unknown, the recommended max size is 1200 bytes. A new connection to userID will be established (asynchronously) unless one already exists. 


* **Send data to a room:**

Native - ovr\_Net\_SendPacketToCurrentRoom()

Unity - Platform.Net.SendPacketToCurrentRoom()

Sends a packet to all members of the room, excluding the currently logged in user. You specify the length of the packet, the bytes in the packet and the policy to apply to the packet; whether the connection is reliable, unreliable or unknown. For a reliable connection, the max number of bytes allowed in the packet is 65535 bytes, which includes any descriptive information (headers) as well as the user data. If the connection is unreliable or unknown, the recommended max size is 1200 bytes. The room has to be created or joined by calling one of the room/matchmaking functions. This function returns false if the user currently isn't in a room.


* **Read a data packet:**

Native - ovr\_Net\_ReadPacket()

Unity - Platform.Net.ReadPacket()

Read the next incoming data packet. The return handle will point to an object that represents some data read from the network. This returns the ovrMessage\_ReadPacket message type. Use ovr\_Packet\_GetSenderID() to get the sender ID, ovr\_Packet\_GetSize to get the size of the packet, or ovr\_Packet\_GetBytes to get the contents of the packet.


* **Release the data packet from memory:**

Native - ovr\_Packet\_Free()

Unity - Platform.Packet.Free()

Once the message has been read, release the packet and free the memory used by the packet. 


* **Close a connection:**

Native - ovr\_Net\_Close()

Unity - Platform.Net.Close()

When the session is complete, close the connection. 


* **Close a connection for a room:**

Native - ovr\_Net\_CloseForCurrentRoom()

Unity - Platform.Net.CloseForCurrentRoom()

Close the connection with everyone in the current room. Call this before leaving the room.




**Listening for Messages**

Integrating Peer-to-Peer networking involves handling the notifications that are sent as part of the networking process. These notifications could be connection requests and notifications that the state has changed. Please review the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/) page for more information about how notifications work in the Platform SDK.

Specifically, for P2P you should be listening and able to handle the following notifications:

* ovrMessage\_Notification\_Networking\_ConnectionStateChange
* ovrMessage\_Notification\_Networking\_PeerConnectRequest
* ovrMessage\_Notification\_Networking\_PingResult


## Example Implementation - Native &amp; Unity

In general, a P2P connection between two users, users A and B, would follow:

1. Initiate a connection between two users. Explicitly connecting users by calling ovr\_Net\_Connect() ensures that all packets will received. You can skip this step and allow the service to implicitly connect when the first packet is received. Unreliable messages received before a connection, and a state change to ovrPeerState\_Connected, is established may be dropped. 
	1.  User A sends a connection request by calling ovr\_Net\_Connect() with the user B's userID. 
	2. User B calls ovr\_Net\_Accept() to accept and initiate the networking session.
	
2. Both users receive the ovrMessage\_NetworkingPeerConnectionStateChange notification that the state has changed to ovrPeerState\_Connected. User A can now call ovr\_Net\_SendPacket() to send the message or data. When calling ovr\_Net\_SendPacket() you'll define one of the policies described above, reliable or unreliable. Please see ovrSendPolicy for more information.
3. User B's application parses the message using ovr\_Net\_ReadPacket() and ovr\_Packet\_GetBytes(). The application frees the memory used by the message on both clients with ovr\_Packet\_Free().
4. (Optional) Destroy the connection by calling ovr\_Net\_Close(). The SDK manages the pool of connections and will discard unused connections.


 The following example comes from the VRVoiceChat [Sample App](/documentation/platform/latest/concepts/book-sampleapp/), a Unity app that uses P2P to transmit real-time avatar location and movement of other users.

More information about Avatars can be found in the [Avatar SDK](/documentation/avatarsdk/latest/) documentation.

```
using UnityEngine;
using System;
using Oculus.Platform;
using Oculus.Platform.Models;

// Helper class to manage a Peer-to-Peer connection to the other user.
// The connection is used to send and received the Transforms for the
// Avatars.  The Transforms are sent via unreliable UDP at a fixed
// frequency.
public class P2PManager
{
    // number of seconds to delay between transform updates
    private static readonly float UPDATE_DELAY = 0.1f;

    // the ID of the remote player we expect to be connected to
    private ulong m_remoteID;

    // the result of the last connection state update message
    private PeerConnectionState m_state = PeerConnectionState.Unknown;

    // the next time to send an updated transform to the remote User
    private float m_timeForNextUpdate;

    // the size of the packet we are sending and receiving
    private static readonly byte PACKET_SIZE = 29;

    // packet format type just in case we want to add new future packet types
    private static readonly byte PACKET_FORMAT = 0;

    // reusable buffer to serialize the Transform into
    private readonly byte[] sendTransformBuffer = new byte[PACKET_SIZE];

    // reusable buffer to deserialize the Transform into
    private readonly byte[] receiveTransformBuffer = new byte[PACKET_SIZE];

    // the last received position update
    private Vector3 receivedPosition;

    // the previous received position to interpolate from
    private Vector3 receivedPositionPrior;

    // the last received rotation update
    private Quaternion receivedRotation;

    // the previous received rotation to interpolate from
    private Quaternion receivedRotationPrior;

    // when the last transform was received
    private float receivedTime;

    public P2PManager(Transform initialHeadTransform)
    {
        receivedPositionPrior = receivedPosition = initialHeadTransform.localPosition;
        receivedRotationPrior = receivedRotation = initialHeadTransform.localRotation;

        Net.SetPeerConnectRequestCallback(PeerConnectRequestCallback);
        Net.SetConnectionStateChangedCallback(ConnectionStateChangedCallback);
    }

    #region Connection Management

    public void ConnectTo(ulong userID)
    {
        m_remoteID = userID;

        // ID comparison is used to decide who calls Connect and who calls Accept
        if (PlatformManager.MyID &lt; userID)
        {
            Net.Connect(userID);
        }
    }

    public void Disconnect()
    {
        if (m_remoteID != 0)
        {
            Net.Close(m_remoteID);
            m_remoteID = 0;
            m_state = PeerConnectionState.Unknown;
        }
    }

    public bool Connected
    {
        get
        {
            return m_state == PeerConnectionState.Connected;
        }
    }

    void PeerConnectRequestCallback(Message&lt;NetworkingPeer&gt; msg)
    {
        Debug.LogFormat("Connection request from {0}, authorized is {1}", msg.Data.ID, m_remoteID);

        if (msg.Data.ID == m_remoteID)
        {
            Net.Accept(msg.Data.ID);
        }
    }

    void ConnectionStateChangedCallback(Message&lt;NetworkingPeer&gt; msg)
    {
        Debug.LogFormat("Connection state to {0} changed to {1}", msg.Data.ID, msg.Data.State);

        if (msg.Data.ID == m_remoteID)
        {
            m_state = msg.Data.State;

            if (m_state == PeerConnectionState.Timeout &amp;&amp;
                // ID comparison is used to decide who calls Connect and who calls Accept
                PlatformManager.MyID &lt; m_remoteID)
            {
                // keep trying until hangup!
                Net.Connect(m_remoteID);
            }
        }

        PlatformManager.SetBackgroundColorForState();
    }

    #endregion

    #region Send Update

    public bool ShouldSendHeadUpdate
    {
        get
        {
            return Time.time &gt;= m_timeForNextUpdate &amp;&amp; m_state == PeerConnectionState.Connected;
        }
    }

    public void SendHeadTransform(Transform headTransform)
    {
        m_timeForNextUpdate = Time.time + UPDATE_DELAY;

        sendTransformBuffer[0] = PACKET_FORMAT;
        int offset = 1;

        PackFloat(headTransform.localPosition.x, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localPosition.y, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localPosition.z, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localRotation.x, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localRotation.y, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localRotation.z, sendTransformBuffer, ref offset);
        PackFloat(headTransform.localRotation.w, sendTransformBuffer, ref offset);

        Net.SendPacket(m_remoteID, sendTransformBuffer, SendPolicy.Unreliable);
    }

    void PackFloat(float f, byte[] buf, ref int offset)
    {
        Buffer.BlockCopy(BitConverter.GetBytes(f), 0, buf, offset, 4);
        offset = offset + 4;
    }

    #endregion

    #region Receive Update

    public void GetRemoteHeadTransform(Transform headTransform)
    {
        bool hasNewTransform = false;

        Packet packet;
        while ((packet = Net.ReadPacket()) != null)
        {
            if (packet.Size != PACKET_SIZE)
            {
                Debug.Log("Invalid packet size: " + packet.Size);
                continue;
            }

            packet.ReadBytes(receiveTransformBuffer);

            if (receiveTransformBuffer[0] != PACKET_FORMAT)
            {
                Debug.Log("Invalid packet type: " + packet.Size);
                continue;
            }
            hasNewTransform = true;
        }

        if (hasNewTransform)
        {
            receivedPositionPrior = receivedPosition;
            receivedPosition.x = BitConverter.ToSingle(receiveTransformBuffer, 1);
            receivedPosition.y = BitConverter.ToSingle(receiveTransformBuffer, 5);
            receivedPosition.z = BitConverter.ToSingle(receiveTransformBuffer, 9);

            receivedRotationPrior = receivedRotation;
            receivedRotation.x = BitConverter.ToSingle(receiveTransformBuffer, 13);
            receivedRotation.y = BitConverter.ToSingle(receiveTransformBuffer, 17) * -1.0f;
            receivedRotation.z = BitConverter.ToSingle(receiveTransformBuffer, 21);
            receivedRotation.w = BitConverter.ToSingle(receiveTransformBuffer, 25) * -1.0f;

            receivedTime = Time.time;
        }

        // since we're receiving updates at a slower rate than we render,
        // interpolate to make the motion look smoother
        float completed = Math.Min(Time.time - receivedTime, UPDATE_DELAY) / UPDATE_DELAY;
        headTransform.localPosition =
            Vector3.Lerp(receivedPositionPrior, receivedPosition, completed);
        headTransform.localRotation =
            Quaternion.Slerp(receivedRotationPrior, receivedRotation, completed);
    }

    #endregion
}
```

## Integrate Peer-to-Peer Networking - Unreal

 P2P networking between users is handled by Unreal's [UNetDriver](https://docs.unrealengine.com/latest/INT/API/Runtime/Engine/Engine/UNetDriver/index.html) and most situations do not require any additional integration. To enable P2P ensure that the following is added to your DefaultEngine.ini file.

```
[/Script/Engine.GameEngine]
+NetDriverDefinitions=(DefName="GameNetDriver",DriverClassName="OnlineSubsystemOculus.OculusNetDriver",DriverClassNameFallback="OnlineSubsystemUtils.IpNetDriver")
                
[/Script/OnlineSubsystemOculus.OculusNetDriver]
NetConnectionClassName="OnlineSubsystemOculus.OculusNetConnection"
```

If you'd like the client to act as the host of a game, you may add **Set Is Server** to your map.
