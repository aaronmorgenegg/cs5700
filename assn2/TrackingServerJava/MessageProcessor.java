import java.net.InetAddress;

public class MessageProcessor implements IMessageProcessor {

    private String name;
    private int receiveCount;

    public MessageProcessor(String name) {
        this.name = name;
    }
    @Override
    public void process(String message, InetAddress address, int port) {
        IMessage newMessage = new Message(message);
        newMessage.process();
        receiveCount++;
    }

    public int ReceiveCount() { return receiveCount; }
}
