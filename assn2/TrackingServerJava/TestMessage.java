import org.junit.Before;
import org.junit.Test;

import java.net.InetAddress;

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
    public void testMessageProcessing() throws Exception {
        // Race Start
        String message = "Race,TestRace,100";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        Race race = testTrackingServer.getRaceByTitle("TestRace");
        assertEquals(race.getDistance(), 100);

        // Athlete Register
        message = "Registered,1,2,Elvis,Presley,male,35";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        Athlete athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getAge(), 35);
        assertEquals(athlete.getUpdateTime(), 2);
        assertEquals(athlete.getFirstName(), "Elvis");
        assertEquals(athlete.getLastName(), "Presley");
        assertEquals(athlete.getGender(), "male");

        // Athlete Did not Start
        message = "DidNotStart,1,3";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getStatus(), "DidNotStart");
        assertEquals(athlete.getStartTime(), 3);

        // Athlete Started
        message = "Started,1,4";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getStatus(), "Started");
        assertEquals(athlete.getStartTime(), 4);

        // Athlete On Course Update
        message = "OnCourse,1,5,2";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getDistance(), 2, 0.01);
        assertEquals(athlete.getUpdateTime(), 5);

        // Athlete Did not finish
        message = "DidNotFinish,1,6";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getStatus(), "DidNotFinish");
        assertEquals(athlete.getEndTime(), 6);

        // Athlete finish
        message = "Finished,1,7";
        testCommunicator.send(message, address, port);
        Thread.sleep(100);
        athlete = testTrackingServer.getAthleteByBib(1);
        assertEquals(athlete.getStatus(), "Finished");
        assertEquals(athlete.getEndTime(), 7);

    }

}