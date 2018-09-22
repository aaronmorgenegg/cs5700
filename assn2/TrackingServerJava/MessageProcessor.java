import java.net.InetAddress;

public class MessageProcessor implements IMessageProcessor {

    private int receiveCount;
    private RaceManager raceManager;

    public MessageProcessor(RaceManager raceManager) {
        this.raceManager = raceManager;
    }
    @Override
    public void process(String message, InetAddress address, int port) {
        IMessage newMessage = new Message();
        newMessage.process(message, raceManager);
        receiveCount++;
    }

    public int ReceiveCount() { return receiveCount; }
}
