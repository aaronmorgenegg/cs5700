import java.util.Arrays;
import java.util.List;

public class Message implements IMessage{
    private String message;

    Message(String message){
        this.message = message;
    }

    public void process(){
        List<String> args = Arrays.asList(this.message.split("\\s*,\\s*"));
        System.out.println(Arrays.toString(args.toArray()));
    }
}

//class MessageRaceStarted implements IMessage{
//    public void process(String message){
//
//    }
//}
