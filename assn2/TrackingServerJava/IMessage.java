import java.util.List;

public interface IMessage {
    void process(List<String> message, RaceManager raceManager);
}
