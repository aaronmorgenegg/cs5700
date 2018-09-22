import java.util.Arrays;
import java.util.List;

public class Message implements IMessage{
    public void process(String message, RaceManager raceManager){
        List<String> args = Arrays.asList(message.split("\\s*,\\s*"));
        System.out.println(Arrays.toString(args.toArray()));
        if(args.get(0).equals("Race")){
            Race newRace = new Race(
                    args.get(1),
                    Integer.parseInt(args.get(2))
            );
            raceManager.addRace(newRace);
        } else if (args.get(0).equals("Registered")){
            Athlete newAthlete = new Athlete(
                    Integer.parseInt(args.get(1)),
                    Double.parseDouble(args.get(2)),
                    args.get(3),
                    args.get(4),
                    args.get(5),
                    Integer.parseInt(args.get(6))
            );
            raceManager.addAthlete(newAthlete);
        } else if (args.get(0).equals("")){

        }
    }
}

class MessageRaceStarted implements IMessage{
    public void process(String message, RaceManager raceManager){

    }
}
