import java.net.InetAddress;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MessageProcessor implements IMessageProcessor {

    private int receiveCount;
    private TrackingServer trackingServer;
    Map<String, Message> messageTypeMap = new HashMap<>();

    public MessageProcessor(TrackingServer trackingServer) {
        this.trackingServer = trackingServer;
        Message.initializeTypeMap(messageTypeMap);
    }
    @Override
    public void process(String message, InetAddress address, int port) {
        List<String> message_args = Arrays.asList(message.split("\\s*,\\s*"));
        System.out.println("IN: " + Arrays.toString(message_args.toArray()));
        String message_type = message_args.get(0);
        IMessage newMessage = messageTypeMap.get(message_type);
        newMessage.process(message_args, address, port, trackingServer);
        receiveCount++;
    }

    public int ReceiveCount() { return receiveCount; }
}
