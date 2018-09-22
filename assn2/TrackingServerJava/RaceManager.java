import java.net.SocketException;

public class RaceManager {
    private MessageProcessor messageProcessor;
    private Communicator communicator;

    RaceManager() throws SocketException {
        communicator = new Communicator(12000);
        messageProcessor = new MessageProcessor("Message Processor");
        communicator.setProcessor(messageProcessor);
    }
    
    RaceManager(int localPort) throws SocketException {
        communicator = new Communicator(localPort);
        messageProcessor = new MessageProcessor("Message Processor");
        communicator.setProcessor(messageProcessor);
    }

    public void start(){
        communicator.start();
    }
}
