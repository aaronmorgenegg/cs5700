import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Message implements IMessage {

    public void process(List<String> message, RaceManager raceManager){
        System.out.println(Arrays.toString(message.toArray()));
    }

    static void initializeTypeMap(Map messageTypeMap){
        messageTypeMap.put("Race", new MessageRaceStart());
        messageTypeMap.put("Registered", new MessageAthleteRegister());
        messageTypeMap.put("Started", new MessageAthleteStart());
        messageTypeMap.put("DidNotStart", new MessageAthleteDidNotStart());
        messageTypeMap.put("OnCourse", new MessageAthleteOnCourse());
        messageTypeMap.put("DidNotFinish", new MessageAthleteDidNotFinish());
        messageTypeMap.put("Finished", new MessageAthleteFinish());
    }
}

class MessageRaceStart extends Message{
    public void process(List<String> message, RaceManager raceManager){
        String title = message.get(1);
        double distance = Double.parseDouble(message.get(2));
        Race newRace = new Race(title, distance);
        raceManager.addRace(newRace);
    }
}

class MessageAthleteRegister extends Message{
    public void process(List<String> message, RaceManager raceManager){
        int bib = Integer.parseInt(message.get(1));
        double time = Double.parseDouble(message.get(2));
        String first_name = message.get(3);
        String last_name = message.get(4);
        String gender = message.get(5);
        int age = Integer.parseInt(message.get(6);
        Athlete newAthlete = new Athlete(bib,time,first_name,last_name,gender,age);
        raceManager.addAthlete(newAthlete);
    }
}

class MessageAthleteStart extends Message{
    public void process(List<String> message, RaceManager raceManager){
        int bib = Integer.parseInt(message.get(1));
        double time = Double.parseDouble(message.get(2));
        raceManager.startAthlete(bib, time);
    }
}

class MessageAthleteDidNotStart extends Message{
    public void process(List<String> message, RaceManager raceManager){
        int bib = Integer.parseInt(message.get(1));
        double time = Double.parseDouble(message.get(2));
        raceManager.didNotStartAthlete(bib, time);
    }
}

class MessageAthleteOnCourse extends Message{
    public void process(List<String> message, RaceManager raceManager){
        int bib = Integer.parseInt(message.get(1));
        double time = Double.parseDouble(message.get(2));
        double distance = Double.parseDouble(message.get(3));
    }
}

class MessageAthleteDidNotFinish extends Message{
    public void process(List<String> message, RaceManager raceManager){

    }
}

class MessageAthleteFinish extends Message{
    public void process(List<String> message, RaceManager raceManager){

    }
}
