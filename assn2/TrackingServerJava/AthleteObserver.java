import java.util.Observable;

public class AthleteObserver implements java.util.Observer{
    public void update(Observable o, Object arg) {
        System.out.println("Something has changed");
    }
}