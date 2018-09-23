import java.net.InetAddress;
import java.util.List;

public interface IMessage {
    void process(List<String> message, InetAddress address, int port, RaceManager raceManager);
}
