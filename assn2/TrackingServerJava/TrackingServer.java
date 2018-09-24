import java.net.InetAddress;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.List;

public class TrackingServer {
    private MessageProcessor messageProcessor;
    private Communicator communicator;
    private List<Client> clients = new ArrayList<>();
    private List<Athlete> athletes = new ArrayList<>();
    private List<Race> races = new ArrayList<>();

    TrackingServer() throws SocketException {
        communicator = new Communicator(12000);
        messageProcessor = new MessageProcessor(this);
        communicator.setProcessor(messageProcessor);
    }

    TrackingServer(int localPort) throws SocketException {
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
            if(client.getAddress().equals(address) & client.getPort()==port){
                return client;
            }
        }
        throw new TrackingServerException("Error: Client not found for given address:port");
    }

    public void start(){
        communicator.start();
    }

    public void raceAdd(Race race){
        races.add(race);
        sendClientsRace(race);
    }

    public void athleteAdd(Athlete athlete){
        athletes.add(athlete);
        sendClientsAthleteRegister(athlete);
    }

    public void clientAdd(InetAddress address, int port){
        Client client = new Client(address, port, communicator);
        clients.add(client);
    }

    public void athleteStart(int bib, int start_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setStartTime(start_time);
            athlete.setStatus("Started");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void athleteDidNotStart(int bib, int start_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setStartTime(start_time);
            athlete.setStatus("DidNotStart");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void athleteOnCourse(int bib, int update_time, double distance){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setUpdateTime(update_time);
            athlete.setDistance(distance);
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void athleteDidNotFinish(int bib, int end_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setEndTime(end_time);
            athlete.setStatus("DidNotFinish");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
    }

    public void athleteFinish(int bib, int end_time){
        try {
            Athlete athlete = getAthleteByBib(bib);
            athlete.setEndTime(end_time);
            athlete.setStatus("Finished");
        }
        catch (TrackingServerException e){
            e.printStackTrace();
        }
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
        client.sendMessageAthleteStatus(athlete);
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

    public void sendClientsAthleteRegister(Athlete athlete){
        int bib = athlete.getBib();
        String first_name = athlete.getFirstName();
        String last_name = athlete.getLastName();
        String gender = athlete.getGender();
        int age = athlete.getAge();
        String output_message = String.format("Athlete,%s,%s,%s,%s,%s", bib,first_name,last_name,gender,age);
        for(Client client : clients){
            client.sendClientMessage(output_message);
        }
    }

    public void sendClientsRace(Race race){
        String title = race.getTitle();
        int distance = race.getDistance();
        String output_message = String.format("Race,%s,%s", title, distance);
        for(Client client : clients){
            client.sendClientMessage(output_message);
        }
    }

    public static void main(String[] args) throws SocketException {
        TrackingServer myTrackingServer = new TrackingServer(12000);
        myTrackingServer.start();
    }
}
