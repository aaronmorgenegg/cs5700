import java.net.InetAddress;
import java.util.Observable;

public class Client implements java.util.Observer{
    private InetAddress address;
    private int port;

    Client(InetAddress address, int port){
        this.address = address;
        this.port = port;
    }

    public InetAddress getAddress() { return address; }

    public int getPort() { return port; }

    public void update(Observable o, Object arg) {
        System.out.println("Client: Something has changed");
    }
}