import java.net.InetAddress;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MessageProcessor implements IMessageProcessor {

    private int receiveCount;
    private RaceManager raceManager;
    Map<String, Message> messageTypeMap = new HashMap<>();

    public MessageProcessor(RaceManager raceManager) {
        this.raceManager = raceManager;
        Message.initializeTypeMap(messageTypeMap);
    }
    @Override
    public void process(String message, InetAddress address, int port) {
        List<String> message_args = Arrays.asList(message.split("\\s*,\\s*"));
        String message_type = message_args.get(0);
        IMessage newMessage = messageTypeMap.get(message_type);
        newMessage.process(message_args, address, port, raceManager);
        receiveCount++;
    }

    public int ReceiveCount() { return receiveCount; }
}
