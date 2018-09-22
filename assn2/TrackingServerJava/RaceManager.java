import java.net.SocketException;
import java.util.ArrayList;
import java.util.List;

public class RaceManager {
    private MessageProcessor messageProcessor;
    private Communicator communicator;
    private List<Client> clients = new ArrayList<>();
    private List<Athlete> athletes = new ArrayList<>();
    private List<Race> races = new ArrayList<>();

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
