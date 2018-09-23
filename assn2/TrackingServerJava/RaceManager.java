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

    public void start(){
        communicator.start();
    }

    public void addRace(Race race){
        races.add(race);
    }

    public void addAthlete(Athlete athlete){
        athletes.add(athlete);
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
}
