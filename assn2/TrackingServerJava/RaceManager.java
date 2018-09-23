import java.net.InetAddress;
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
        messageProcessor = new MessageProcessor(this);
        communicator.setProcessor(messageProcessor);
    }

    RaceManager(int localPort) throws SocketException {
        communicator = new Communicator(localPort);
        messageProcessor = new MessageProcessor(this);
        communicator.setProcessor(messageProcessor);
    }

    public Athlete getAthleteByBib(int bib) throws TrackingServerException{
        for(Athlete athlete : athletes){
            if(athlete.getBib()==bib){
                return athlete;
            }
        }
        throw new TrackingServerException("Error: Athlete not found for given bib");
    }

    public Client getClientByAddressPort(InetAddress address, int port) throws TrackingServerException{
        for(Client client : clients){
            if(client.getAddress()==address & client.getPort()==port){
                return client;
            }
        }
        throw new TrackingServerException("Error: Client not found for given address:port");
    }

    public void start(){
        communicator.start();
    }

    public void addRace(Race race){
        races.add(race);
    }

    public void addAthlete(Athlete athlete){
        athletes.add(athlete);
        sendClientsAthleteRegister(athlete);
    }

    public void startAthlete(int bib, double start_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setStartTime(start_time);
            athlete.setStatus("Started");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void didNotStartAthlete(int bib, double start_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setStartTime(start_time);
            athlete.setStatus("DidNotStart");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void onCourseAthlete(int bib, double update_time, double distance){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setUpdateTime(update_time);
            athlete.setDistance(distance);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void didNotFinishAthlete(int bib, double end_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setEndTime(end_time);
            athlete.setStatus("DidNotFinish");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void finishAthlete(int bib, double end_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setEndTime(end_time);
            athlete.setStatus("Finished");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void addClient(InetAddress address, int port){
        Client client = new Client(address, port, this);
        clients.add(client);
    }

    public void clientSubscribe(InetAddress address, int port, int bib){
        Client client;
        Athlete athlete;
        try {
            client = getClientByAddressPort(address, port);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
            return;
        }
        try {
            athlete = getAthleteByBib(bib);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
            return;
        }
        athlete.addObserver(client);
    }

    public void clientUnsubscribe(InetAddress address, int port, int bib){
        Client client;
        Athlete athlete;
        try {
            client = getClientByAddressPort(address, port);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
            return;
        }
        try {
            athlete = getAthleteByBib(bib);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
            return;
        }
        athlete.deleteObserver(client);
    }

    public void sendClientMessage(Client client, String message){
        try {
            communicator.send(message, client.getAddress(), client.getPort());
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }

    public void sendClientsAthleteRegister(Athlete athlete){
        int bib = athlete.getBib();
        String first_name = athlete.getFirstName();
        String last_name = athlete.getLastName();
        String gender = athlete.getGender();
        int age = athlete.getAge();
        String output_message = String.format("Athlete,%s,%s,%s,%s,%s", bib,first_name,last_name,gender,age);
        for(Client client : clients){
            sendClientMessage(client,output_message);
        }
    }
}
