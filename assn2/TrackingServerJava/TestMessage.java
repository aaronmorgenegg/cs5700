import org.junit.Before;
import org.junit.Test;

import java.net.InetAddress;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class TestMessage{
    private TrackingServer testTrackingServer;
    private Communicator testCommunicator;
    private InetAddress address;
    private int port;

    @Before
    public void init() {
        try {
            address = InetAddress.getByName("127.0.0.1");
            port = 12000;
            testTrackingServer = new TrackingServer(port);
            testCommunicator = new Communicator(port+5);
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        testTrackingServer.start();
    }

    @Test
    public void testMessageRaceStart() throws Exception {
        String message = "Race,TestRace,100";
        try {
            testCommunicator.send(message, address, port);
        }
        catch(Exception e){
            e.printStackTrace();
        }
        Thread.sleep(100);
        Race result = testTrackingServer.getRaceByTitle("TestRace");
        assertEquals(result.getDistance(), 100);
    }
}