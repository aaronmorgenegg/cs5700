import java.net.InetAddress;
import java.util.Observable;

public class Client implements java.util.Observer{
    private InetAddress address;
    private int port;
    private Communicator communicator;

    Client(InetAddress address, int port, Communicator communicator){
        this.address = address;
        this.port = port;
        this.communicator = communicator;
    }

    public InetAddress getAddress() { return address; }

    public int getPort() { return port; }

    public void update(Observable o, Object arg) {
        if(o instanceof Athlete) {
            sendMessageAthleteStatus((Athlete)o);
        }
    }

    public void sendMessageAthleteStatus(Athlete athlete){
        int bib = athlete.getBib();
        String status = athlete.getStatus();
        int start_time = athlete.getStartTime();
        double distance = athlete.getDistance();
        int update_time = athlete.getUpdateTime();
        int end_time = athlete.getEndTime();

        String output_message = String.format("Status,%s,%s,%s,%s,%s,%s", bib,status,start_time,distance,update_time,end_time);
        sendClientMessage(output_message);
    }

    public void sendClientMessage(String message){
        System.out.println("OUT: " + message);
        try {
            communicator.send(message, address, port);
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}