import java.net.SocketException;

public class TrackingServer {
    public static void main(String[] args) throws SocketException {
        RaceManager myRaceManager = new RaceManager(12000);
        myRaceManager.start();
    }
}