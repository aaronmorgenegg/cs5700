import java.net.SocketException;

public class TrackingServer {
    public static void main(String[] args) throws SocketException {
        Communicator myCommunicator = new Communicator(12000);
        MessageProcessor myMessageProcessor = new MessageProcessor("Message Processor");
        myCommunicator.setProcessor(myMessageProcessor);

        myCommunicator.start();
    }
}